# Systematic Debugging Methodology

## Guiding Principle: Occam's Razor for Debugging

**When facing mysterious errors, the root cause is almost always simpler than it appears.**

Common error distribution in real-world debugging:
- **70%**: Configuration issues (wrong parameters, missing flags, incorrect paths)
- **20%**: Environment issues (missing dependencies, version mismatches, path problems)
- **8%**: Data format issues (encoding, structure assumptions)
- **2%**: Actual bugs in external APIs or fundamental incompatibilities

**Core Rule**: Exhaust simple hypotheses before considering complex ones. Authentication failures are configuration problems 99% of the time, not API design flaws.

---

## 1. Hypothesis Priority Framework

### Always Start Here: The "Boring Checklist"

Before investigating complex hypotheses, verify these fundamentals:

1. **Configuration Loading**
   - Are environment variables actually loaded? (Not just "file exists")
   - Are config files in the correct location relative to execution path?
   - Are there hidden default parameters overriding your explicit config?

2. **Exact Version/Name Matching**
   - Library versions exact match with documentation examples?
   - API endpoint names exactly correct (not similar, not partially matching)?
   - Model/service names character-perfect? (e.g., `preview-09-2025` ≠ `preview-2025-09`)

3. **First-Hand Error Visibility**
   - Have you personally executed the failing code?
   - Have you seen the complete error output (not summarized or truncated)?
   - Are there error details hidden in non-obvious places (WebSocket close codes, HTTP headers)?

### Hypothesis Ordering Template

```markdown
## Problem: [Description]

### Priority 1: Configuration Issues (Check First)
- [ ] Hypothesis 1a: Config file not loaded from expected path
      Verification: Add logging immediately after config load
- [ ] Hypothesis 1b: SDK using unexpected default parameters
      Verification: Log all parameters passed to SDK constructor
- [ ] Hypothesis 1c: Authentication credentials format issue
      Verification: Check credential string length, prefix, encoding

### Priority 2: Environment Issues
- [ ] Hypothesis 2a: Dependency version mismatch
      Verification: Check package.json vs installed versions
- [ ] Hypothesis 2b: Runtime environment differences
      Verification: Compare working vs failing environment variables

### Priority 3: Data Format Issues
- [ ] Hypothesis 3a: Incorrect data structure assumptions
      Verification: Log raw data structure, don't assume
- [ ] Hypothesis 3b: Encoding mismatch (UTF-8, base64, binary)
      Verification: Inspect first few bytes/characters

### Priority 4: Complex Issues (Only After Above Exhausted)
- [ ] Hypothesis 4a: API limitation or bug
      Verification: Find official documentation or working examples
- [ ] Hypothesis 4b: Fundamental incompatibility
      Verification: Find counter-examples proving it can work
```

---

## 2. Isolation Strategy: Diagnostic Scripts

**The Most Powerful Debugging Technique**: Create minimal, single-purpose scripts that test ONE thing at a time.

### Why This Works

- **Eliminates confounding variables**: Complex scripts have multiple failure points
- **Provides clear pass/fail criteria**: If this 10-line script fails, the problem is X
- **Builds confidence incrementally**: Each passing diagnostic narrows the search space
- **Creates reusable verification tools**: Same scripts can verify fixes

### Diagnostic Script Principles

1. **One Variable Per Script**: Test configuration loading separately from API calls separately from data processing
2. **Verbose Logging**: Log every step, every value, every assumption
3. **Explicit Success Criteria**: Script should clearly output PASS or FAIL
4. **No Assumptions**: Check everything explicitly, even "obvious" things

### Template: Configuration Diagnostic

```javascript
// diagnose-config.js
// Purpose: Verify configuration loading and format
// Success criteria: All checks pass with ✓

console.log('=== Configuration Diagnostic ===\n');

// 1. Environment
console.log('--- Environment ---');
console.log('Node version:', process.version);
console.log('Working directory:', process.cwd());
console.log('Script location:', __dirname);

// 2. Config File Loading
console.log('\n--- Config File ---');
const fs = require('fs');
const path = require('path');

const configPath = path.join(__dirname, '.env');
console.log('Expected path:', configPath);
console.log('File exists:', fs.existsSync(configPath));

if (fs.existsSync(configPath)) {
  const content = fs.readFileSync(configPath, 'utf-8');
  console.log('File size:', content.length, 'bytes');
  console.log('Lines:', content.split('\n').length);
}

// 3. Environment Variable
require('dotenv').config({ path: configPath });
console.log('\n--- Environment Variable ---');
console.log('API_KEY defined:', !!process.env.API_KEY);
console.log('API_KEY length:', process.env.API_KEY?.length);
console.log('API_KEY prefix:', process.env.API_KEY?.slice(0, 4));
console.log('API_KEY has whitespace:', /\s/.test(process.env.API_KEY || ''));

// 4. Format Validation
console.log('\n--- Format Validation ---');
const expectedPrefix = 'AIza'; // Example for Google API keys
const expectedLength = 39;

const prefixMatch = process.env.API_KEY?.startsWith(expectedPrefix);
const lengthMatch = process.env.API_KEY?.length === expectedLength;

console.log(prefixMatch ? '✓' : '✗', 'Prefix matches expected format');
console.log(lengthMatch ? '✓' : '✗', 'Length matches expected format');

// 5. SDK Constructor (No Network Call)
console.log('\n--- SDK Initialization ---');
try {
  const SDK = require('./sdk'); // Your SDK
  const client = new SDK({
    apiKey: process.env.API_KEY,
    // Log all parameters, including defaults
  });
  console.log('✓ SDK initialized without errors');
  console.log('Client config:', JSON.stringify(client.config, null, 2));
} catch (error) {
  console.log('✗ SDK initialization failed:', error.message);
}

console.log('\n=== Diagnostic Complete ===');
```

### Template: Data Structure Diagnostic

```javascript
// diagnose-data-structure.js
// Purpose: Inspect actual data structure without assumptions
// Success criteria: Understand exact structure and location of target data

function inspectObject(obj, path = 'root', maxDepth = 3, currentDepth = 0) {
  const indent = '  '.repeat(currentDepth);

  console.log(`${indent}${path}:`);
  console.log(`${indent}  Type: ${typeof obj}`);
  console.log(`${indent}  Null: ${obj === null}`);
  console.log(`${indent}  Undefined: ${obj === undefined}`);

  if (obj === null || obj === undefined) return;

  if (typeof obj === 'object') {
    if (Buffer.isBuffer(obj)) {
      console.log(`${indent}  [Buffer: ${obj.length} bytes]`);
      console.log(`${indent}  First 20 bytes: ${obj.slice(0, 20).toString('hex')}`);
      return;
    }

    if (Array.isArray(obj)) {
      console.log(`${indent}  [Array: ${obj.length} items]`);
      if (obj.length > 0 && currentDepth < maxDepth) {
        inspectObject(obj[0], `${path}[0]`, maxDepth, currentDepth + 1);
      }
      return;
    }

    const keys = Object.keys(obj);
    console.log(`${indent}  Keys: [${keys.join(', ')}]`);

    if (currentDepth < maxDepth) {
      for (const key of keys.slice(0, 5)) { // Limit to first 5 keys
        inspectObject(obj[key], `${path}.${key}`, maxDepth, currentDepth + 1);
      }
    }
  } else if (typeof obj === 'string') {
    console.log(`${indent}  Length: ${obj.length}`);
    console.log(`${indent}  Preview: "${obj.slice(0, 50)}${obj.length > 50 ? '...' : ''}"`);

    // Check encoding hints
    const isBase64Like = /^[A-Za-z0-9+/=]+$/.test(obj);
    const isHexLike = /^[0-9a-fA-F]+$/.test(obj);
    console.log(`${indent}  Looks like base64: ${isBase64Like}`);
    console.log(`${indent}  Looks like hex: ${isHexLike}`);
  } else {
    console.log(`${indent}  Value: ${obj}`);
  }
}

// Usage example with API response
const response = getAPIResponse(); // Your actual API call
console.log('=== Raw Response Structure ===\n');
inspectObject(response);

// Specific path investigation
console.log('\n=== Investigating Suspected Path ===');
console.log('response.data exists:', !!response.data);
console.log('response.body exists:', !!response.body);
console.log('response.payload exists:', !!response.payload);

// If you're looking for binary data
console.log('\n=== Binary Data Search ===');
function findBuffers(obj, path = 'root') {
  if (Buffer.isBuffer(obj)) {
    console.log(`Found Buffer at: ${path} (${obj.length} bytes)`);
    return;
  }
  if (typeof obj === 'object' && obj !== null) {
    for (const key in obj) {
      findBuffers(obj[key], `${path}.${key}`);
    }
  }
}
findBuffers(response);
```

### Template: API Interaction Diagnostic

```javascript
// diagnose-api-minimal.js
// Purpose: Minimal API call to isolate authentication from functionality
// Success criteria: Connection succeeds, response received (any response)

console.log('=== Minimal API Test ===\n');

const API = require('./api-client');

async function testMinimalConnection() {
  console.log('1. Creating client...');
  const client = new API({
    apiKey: process.env.API_KEY,
    // Start with absolute minimal config
  });

  console.log('2. Attempting connection...');
  try {
    await client.connect();
    console.log('✓ Connection established');
  } catch (error) {
    console.log('✗ Connection failed:', error.message);
    console.log('Error code:', error.code);
    console.log('Error details:', JSON.stringify(error, null, 2));
    process.exit(1);
  }

  console.log('3. Sending minimal request...');
  try {
    // Simplest possible request
    const response = await client.send({ message: 'ping' });
    console.log('✓ Response received');
    console.log('Response type:', typeof response);
    console.log('Response keys:', Object.keys(response));
  } catch (error) {
    console.log('✗ Request failed:', error.message);
  }

  console.log('4. Closing connection...');
  await client.close();
  console.log('✓ Test complete');
}

testMinimalConnection().catch(console.error);
```

### Real-World Example: WebSocket Authentication Mystery

**Problem**: WebSocket connection immediately closes with code 1007 "API key not valid"

**❌ Initial Approach** (jumping to complex hypotheses):
- "Maybe the API doesn't support this model"
- "Maybe the feature flag is disabled for my account"
- "Maybe there's a rate limit"

**✅ Diagnostic Script Approach**:

```javascript
// diagnose-websocket-auth.js
console.log('=== WebSocket Auth Diagnostic ===\n');

// Step 1: Verify API key loading
console.log('--- API Key ---');
console.log('Loaded:', !!process.env.API_KEY);
console.log('Length:', process.env.API_KEY?.length);
console.log('Format:', process.env.API_KEY?.slice(0, 4) + '...' + process.env.API_KEY?.slice(-4));

// Step 2: Check SDK configuration
console.log('\n--- SDK Config ---');
const sdk = new SDK({
  apiKey: process.env.API_KEY,
});

// KEY DISCOVERY: Log the actual endpoint being used
console.log('Endpoint:', sdk.endpoint); // Revealed: Using Vertex AI endpoint!

// Step 3: Check SDK defaults
console.log('Default vertexai:', sdk.config.vertexai); // Revealed: true by default!

// Step 4: Test with explicit configuration
console.log('\n--- Testing explicit vertexai: false ---');
const sdkFixed = new SDK({
  apiKey: process.env.API_KEY,
  vertexai: false, // Explicit override
});
console.log('Endpoint:', sdkFixed.endpoint); // Now using correct endpoint!
```

**Result**: The diagnostic revealed that the SDK defaulted to `vertexai: true`, sending requests to Vertex AI endpoint instead of the Gemini Developer API endpoint. The fix was a single parameter.

**Time saved**: This 15-line diagnostic script found the issue in 2 minutes. The alternative (reading SDK source code or trial-and-error config changes) would have taken hours.

---

## 3. Comparison with Working Examples

### Why This Is Critical

When you have a working example (different language, different version, official sample), it's a **treasure map** showing the correct configuration.

**Working example exists → Problem is in the differences**

### Systematic Comparison Process

1. **Find the Working Example**
   - Official SDK examples (preferred)
   - Successful previous implementations in your codebase
   - Community examples with verified success (check issues/discussions)

2. **Compare Layer by Layer**
   ```markdown
   ## Comparison Checklist

   ### Language/Runtime
   - [ ] Working: Python 3.11, Failing: Node.js 20
   - [ ] Any known language-specific issues?

   ### SDK Versions
   - [ ] Working: v2.1.0, Failing: v2.3.1
   - [ ] Check changelog between versions

   ### Configuration Parameters
   Working:
   ```python
   client = Client(api_key=key)  # Only 1 parameter
   ```

   Failing:
   ```javascript
   const client = new Client({ apiKey: key, ...manyOtherParams });
   ```
   - [ ] What are those other params? What are their defaults?

   ### API Endpoint
   - [ ] Working: api.service.com, Failing: ???
   - [ ] Log actual endpoint used by SDK

   ### Request Format
   - [ ] Compare actual HTTP/WebSocket frames sent (use network inspector)
   ```

3. **Identify Hidden Differences**

   Common gotchas:
   - **Default parameters**: JavaScript SDK has `vertexai: true` default, Python doesn't have this parameter
   - **Authentication methods**: One uses header, another uses query param
   - **Endpoint URLs**: SDKs may auto-select endpoints based on config
   - **Retry behavior**: One SDK retries automatically, hiding transient failures

### Example: Cross-Language Comparison

**Problem**: Python POC works, JavaScript POC fails with authentication error

**Comparison**:

```python
# Python (WORKING)
import google.generativeai as genai

genai.configure(api_key=api_key)  # Simple, one-line config
model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content('Hello')
```

```javascript
// JavaScript (FAILING)
const { GoogleGenerativeAI } = require('@google/generative-ai');

const ai = new GoogleGenerativeAI({
  apiKey: process.env.API_KEY,
  // What's different?
});
```

**Investigation**:
1. Python library source: `genai.configure()` only sets API key, no other parameters
2. JavaScript SDK docs: Constructor accepts `vertexai` parameter (default: `true`)
3. Hypothesis: JavaScript defaulting to Vertex AI endpoint

**Verification**:
```javascript
const ai = new GoogleGenerativeAI({
  apiKey: process.env.API_KEY,
  vertexai: false,  // Match Python's implicit behavior
});
```

**Result**: Fixed. The difference was an implicit vs explicit endpoint selection.

---

## 4. Data Structure Verification: Never Assume

### The Anti-Pattern

```javascript
// ❌ Assumption-based code
const audioData = response.data; // Assuming 'data' contains audio
audioFile.write(audioData);
// Result: Writes undefined or wrong data, produces corrupted file
```

### The Correct Pattern

```javascript
// ✅ Verification-first code

// Step 1: Inspect actual structure
console.log('Response keys:', Object.keys(response));
console.log('Response structure:', JSON.stringify(response, null, 2).slice(0, 500));

// Step 2: Search for target data
function findAudioData(obj, path = 'response') {
  if (Buffer.isBuffer(obj)) {
    console.log(`Found Buffer at ${path}: ${obj.length} bytes`);
  }
  if (typeof obj === 'object' && obj !== null) {
    for (const [key, value] of Object.entries(obj)) {
      if (key.includes('audio') || key.includes('data')) {
        console.log(`Candidate at ${path}.${key}:`, typeof value);
      }
      findAudioData(value, `${path}.${key}`);
    }
  }
}
findAudioData(response);

// Step 3: Verify encoding
const candidateData = response.serverContent.modelTurn.parts[0].inlineData.data;
console.log('Data type:', typeof candidateData);
console.log('First 50 chars:', candidateData.slice(0, 50));
console.log('Looks like base64:', /^[A-Za-z0-9+/=]+$/.test(candidateData));

// Step 4: Test decoding
const decoded = Buffer.from(candidateData, 'base64');
console.log('Decoded size:', decoded.length, 'bytes');
console.log('First 10 bytes (hex):', decoded.slice(0, 10).toString('hex'));

// Step 5: Use verified data
audioFile.write(decoded); // Now confident this is correct
```

### Layer-by-Layer Verification Template

```javascript
// For nested data structures (e.g., API responses, message objects)

function verifyPath(obj, pathString) {
  console.log(`\n=== Verifying: ${pathString} ===`);

  const parts = pathString.split('.');
  let current = obj;
  let currentPath = 'root';

  for (const part of parts) {
    currentPath += `.${part}`;

    console.log(`Checking ${currentPath}...`);

    if (current === null || current === undefined) {
      console.log(`✗ Path broken at ${currentPath}: value is ${current}`);
      return null;
    }

    if (typeof current !== 'object') {
      console.log(`✗ Path broken at ${currentPath}: not an object (${typeof current})`);
      return null;
    }

    if (!(part in current)) {
      console.log(`✗ Key "${part}" doesn't exist`);
      console.log(`  Available keys:`, Object.keys(current));
      return null;
    }

    console.log(`✓ ${part} exists`);
    current = current[part];

    if (Array.isArray(current)) {
      console.log(`  (Array with ${current.length} items)`);
    } else if (Buffer.isBuffer(current)) {
      console.log(`  (Buffer with ${current.length} bytes)`);
    } else {
      console.log(`  (${typeof current})`);
    }
  }

  console.log(`\n✓ Full path verified: ${pathString}`);
  return current;
}

// Usage
const audioData = verifyPath(
  response,
  'serverContent.modelTurn.parts.0.inlineData.data'
);
```

---

## 5. Evidence Quality Hierarchy

Not all evidence is equal. Rank your evidence sources:

### Tier 1: Direct Verification (Strongest)
- Running code that succeeds/fails in front of you
- Network traffic you personally captured
- Logs you personally generated with verbose flags
- Binary data you inspected byte-by-byte

### Tier 2: Official Sources
- Official API documentation (with version number matching yours)
- Official SDK examples (with version number matching yours)
- Official changelog entries

### Tier 3: Working Examples
- Community examples with verified success (stars, recent activity)
- Stack Overflow answers with upvotes and recent dates
- Your own previous successful implementations

### Tier 4: Problem Reports
- GitHub Issues (open or closed)
- Stack Overflow questions (problems, not solutions)
- Forum discussions

### Tier 5: Speculation (Weakest)
- "I think this API doesn't support..."
- "This probably means..."
- Assumptions based on API names or parameter names

### Applying the Hierarchy

**Scenario**: Investigating why authentication fails

```markdown
## Evidence Analysis

### Hypothesis: API doesn't support this authentication method

Evidence collected:
1. [Tier 4] GitHub Issue #123: User reports auth failure (OPEN, no resolution)
2. [Tier 5] Parameter named "beta" suggests experimental feature
3. [Tier 2] Official docs state: "Authentication via API key is supported"
4. [Tier 3] Example repo uses API key successfully (last updated 2 months ago)

Conclusion:
- Tier 2 (official docs) contradicts hypothesis
- Tier 3 (working example) disproves hypothesis
- Tier 4 evidence (open issue) indicates others hit same problem, but doesn't prove API limitation
- Hypothesis REJECTED: Auth method IS supported, problem is likely in configuration
```

**Key Principle**: Higher-tier evidence always overrules lower-tier evidence.

---

## 6. The First-Hand Execution Rule

**Rule**: Before forming conclusions, personally execute the failing code and observe the complete output.

### Why This Matters

Second-hand error reports often omit critical details:
- Full error messages (users summarize or truncate)
- Error codes (users paste message but not code)
- Preceding warnings (users skip "unimportant" output)
- Environment differences (users assume their env is "normal")

### Checklist Before Forming Hypothesis

- [ ] Have I executed the failing code myself?
- [ ] Have I seen the complete console output (not summarized)?
- [ ] Have I checked for errors in non-obvious places (close codes, HTTP status, exit codes)?
- [ ] Have I added extra logging to expose internal state?

### Example: The Hidden Close Code

**Second-hand report**: "The WebSocket connection closes immediately with no error"

**Assumptions formed**:
- "No error" → Maybe timeout?
- "Closes immediately" → Maybe connection refused?

**First-hand execution**:
```javascript
// Added logging
websocket.on('close', (code, reason) => {
  console.log('Close code:', code);      // Revealed: 1007
  console.log('Close reason:', reason);  // Revealed: "API key not valid"
});
```

**Result**: Error WAS present, just not logged by default. The close code (1007) immediately pointed to authentication issue.

---

## 7. Debugging Session Template

Use this template to structure your investigation:

```markdown
## Problem Statement
[Concise description of unexpected behavior]

## Environment
- Runtime: [Node.js 20.11.0, Python 3.11, etc.]
- Library versions: [Exact versions from package.json/requirements.txt]
- OS: [If potentially relevant]

## Reproduction
[Minimal code that reproduces the issue]

## Expected vs Actual
- Expected: [What should happen]
- Actual: [What actually happens, with exact error messages]

## Hypothesis Priority List

### Priority 1: Configuration (Check First)
- [ ] Hypothesis 1a: [Specific config issue]
      Evidence needed: [What would prove/disprove this]
      Diagnostic: [Script or test to verify]

### Priority 2: Environment
- [ ] Hypothesis 2a: [Specific env issue]
      Evidence needed: [...]
      Diagnostic: [...]

### Priority 3: Data Format
[...]

### Priority 4: Complex Issues (Only if above exhausted)
[...]

## Evidence Collected

### [Hypothesis 1a]
- **Status**: ✓ PROVEN / ✗ DISPROVEN / ⚠ INCONCLUSIVE
- **Evidence tier**: [1-5]
- **Details**: [What you found]
- **Source**: [Where this evidence came from]

[Repeat for each hypothesis]

## Working Examples Comparison

### Python Implementation (WORKING)
```python
[Code]
```

### JavaScript Implementation (FAILING)
```javascript
[Code]
```

### Differences Identified
1. [Difference 1]
2. [Difference 2]

## Solution

### Root Cause
[Final verified cause, with evidence tier]

### Fix Applied
```javascript
[Exact code change]
```

### Verification
[How you verified the fix works]

## Lessons Learned
[What would make this faster next time]
```

---

## 8. Common Anti-Patterns to Avoid

### Anti-Pattern 1: "Debugging by Modification"

**❌ Wrong**:
```javascript
// Try random changes hoping something works
const client = new API({ apiKey: key, timeout: 5000 });  // Doesn't work
const client = new API({ apiKey: key, timeout: 10000 }); // Doesn't work
const client = new API({ apiKey: key, retry: true });    // Doesn't work
// [30 more random attempts...]
```

**✅ Right**:
```javascript
// Diagnose THEN fix
// 1. Create diagnostic to understand current behavior
// 2. Form hypothesis based on diagnostic output
// 3. Make targeted change
// 4. Verify with diagnostic
```

### Anti-Pattern 2: "Complex First"

**❌ Wrong**: "The API must not support this feature with this model configuration"

**✅ Right**: "Let me first check if my API key is even loading correctly"

### Anti-Pattern 3: "Assumption Stacking"

**❌ Wrong**:
```javascript
// Assuming response.data exists
// Assuming it's a Buffer
// Assuming it's in the right format
fs.writeFileSync('output.wav', response.data);
```

**✅ Right**:
```javascript
// Verify each assumption
console.log('data exists:', !!response.data);
console.log('data type:', typeof response.data);
console.log('is Buffer:', Buffer.isBuffer(response.data));
// [Then use data]
```

### Anti-Pattern 4: "Trust the Summary"

**❌ Wrong**: User says "no error", assume there's no error

**✅ Right**: Execute code yourself, log everything, find the hidden error code

---

## 9. Speed Optimization: Parallel Diagnostics

Once you've identified multiple hypotheses, test them in parallel when possible.

### Pattern: Parallel Diagnostic Scripts

```bash
# Instead of running diagnostics sequentially:
node diagnose-config.js        # 5 seconds
node diagnose-api.js           # 10 seconds
node diagnose-data-format.js   # 5 seconds
# Total: 20 seconds sequential

# Run in parallel:
node diagnose-config.js &
node diagnose-api.js &
node diagnose-data-format.js &
wait
# Total: 10 seconds (limited by slowest)
```

### Pattern: Multi-Hypothesis Test Script

```javascript
// test-all-hypotheses.js
async function testAll() {
  const tests = [
    testConfigLoading,
    testAPIEndpoint,
    testDataFormat,
    testVersionCompatibility
  ];

  const results = await Promise.allSettled(
    tests.map(test => test().catch(e => ({ error: e })))
  );

  results.forEach((result, i) => {
    console.log(`\nTest ${i + 1}: ${tests[i].name}`);
    if (result.status === 'fulfilled') {
      console.log('✓ PASSED');
    } else {
      console.log('✗ FAILED:', result.reason);
    }
  });
}
```

---

## Application to Error Troubleshooting

When using the error-troubleshooter skill:

1. **Start with Occam's Razor**: Always check configuration and environment issues first (90% of problems)
2. **Create Diagnostic Scripts**: Write minimal scripts to isolate variables
3. **Compare with Working Examples**: If it works somewhere else, find the differences
4. **Never Assume Data Structure**: Verify every layer explicitly
5. **Rank Your Evidence**: Tier 1 (direct verification) beats Tier 5 (speculation)
6. **Execute First-Hand**: Don't trust summaries, see the complete output yourself
7. **Avoid Anti-Patterns**: Diagnose first, fix second; simple first, complex later

This systematic approach leads to faster, more reliable problem resolution.
