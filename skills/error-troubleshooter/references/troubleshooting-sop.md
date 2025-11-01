# Troubleshooting Standard Operating Procedures

This document provides detailed, step-by-step procedures for systematic error troubleshooting.

## Core Troubleshooting Workflow

### Phase 1: Error Recognition and Initial Response

When a tool, script, or command fails:

1. **Capture Complete Error Information**
   - Full error message (stdout and stderr)
   - Tool/command that was executed
   - Context of what was being attempted
   - Any stack traces or error codes

2. **Assess Error Clarity**
   - Is the error message self-explanatory?
   - Does it explicitly state what went wrong and how to fix it?
   - Is this a commonly encountered error pattern?

3. **Decide on Investigation Depth**
   - **Trivial/Clear**: Apply quick fix
   - **Non-trivial/Ambiguous**: Proceed to rigorous investigation

### Phase 2: Quick Fix Attempt (Happy Case)

**Criteria for attempting quick fix:**
- Error message explicitly describes the problem and solution
- Error matches a well-known trivial pattern
- Fix requires minimal changes with low risk

**Procedure:**
1. Apply the fix based on error message or experience
2. Re-execute the failing command
3. Evaluate the result:
   - **Success**: Error is resolved → Done
   - **No change**: Error message identical → Revert and escalate
   - **Worse**: New errors or degraded state → Revert immediately and escalate

**Reversion Protocol:**
- Undo all changes made during quick fix attempt
- Verify system is back to pre-fix state
- Document what was attempted (if creating debug notes)

### Phase 3: Rigorous Investigation

Enter this phase when:
- Quick fix failed
- Error is non-trivial from the start
- Multiple potential causes exist
- Context is ambiguous

#### Step 1: Error Template Extraction

**Purpose**: Prepare error message for effective searching by removing variable components.

**Procedure:**
1. Identify the error type/category (e.g., FileNotFoundError, TypeError, ConnectionError)
2. Locate the core error message
3. Remove variable components:
   - File paths: `/home/user/project/file.py` → (remove)
   - Usernames: `user@example.com` → (remove)
   - IDs/numbers: `id=12345` → (remove)
   - Timestamps: `2024-01-15 10:30:45` → (remove)
   - User inputs: `input='value'` → (remove)
   - Line numbers: `line 42` → (keep only if part of standard template)

4. Retain:
   - Error type/class names
   - Standard error message structure
   - Function/method names from standard library/SDK
   - Standard error codes

**Example Transformations:**
```
Original:
  ValueError: invalid literal for int() with base 10: 'abc' at line 42 in /home/user/script.py

Template:
  ValueError invalid literal for int() with base 10

Original:
  requests.exceptions.ConnectionError: HTTPConnectionPool(host='api.example.com', port=443): Max retries exceeded with url: /v1/users

Template:
  requests.exceptions.ConnectionError HTTPConnectionPool Max retries exceeded

Original:
  ModuleNotFoundError: No module named 'pandas'

Template:
  ModuleNotFoundError No module named
```

#### Step 2: Environment Information Collection

**Purpose**: Gather context needed to understand and resolve the error.

**Collection Strategy:**
1. **Start Minimal**: Only collect what's clearly relevant
2. **Expand as Needed**: Add more context if initial research is inconclusive
3. **Always Protect Privacy**: Never collect passwords, API keys, personal data without explicit permission

**Standard Environment Information:**

**System Context:**
- Operating system and version
- Shell/terminal environment
- Current working directory (if relevant)

**Runtime Context:**
- Language/SDK versions (Python, Node.js, etc.)
- Package manager versions (pip, npm, etc.)
- Virtual environment status

**Dependency Context:**
- Installed package versions (for error-related packages)
- Package lock file status
- Dependency conflicts

**Configuration Context:**
- Relevant configuration files (only if directly related to error)
- Environment variables (only non-sensitive ones)

**Collection Commands by Context:**

```bash
# Python environment
python --version
pip --version
pip list | grep <package-name>

# Node.js environment
node --version
npm --version
npm list <package-name>

# System information
uname -a  # Unix/Linux/Mac
ver  # Windows

# Package conflicts
pip check  # Python
npm doctor  # Node.js

# Environment variables (careful with sensitive data)
env | grep <RELEVANT_VAR>
```

**Privacy Protection:**
- **Never collect**: Passwords, API keys, tokens, private keys, personal identifiable information
- **Request permission before collecting**: Project-specific paths, configuration files, custom environment variables
- **Sanitize output**: Remove sensitive data before recording

#### Step 3: Research and Information Gathering

**Research Sources (in order of efficiency):**

1. **Web Search with Error Template**
   - Search the extracted template (not full error)
   - Add language/framework name to query
   - Example: "ModuleNotFoundError No module named python"

2. **Official Documentation**
   - Error code references
   - SDK/API documentation
   - Known issues and breaking changes

3. **Community Resources**
   - Stack Overflow
   - GitHub Issues (especially for specific libraries)
   - Framework-specific forums

**Parallel Research Strategy:**

For complex problems, launch multiple research angles simultaneously using subagents:

```
Investigation Angles:
├─ Subagent 1: Web search for error template
├─ Subagent 2: Search GitHub Issues for affected package
├─ Subagent 3: Check official documentation for breaking changes
└─ Subagent 4: Search for similar errors in codebase history
```

**Research Efficiency:**
- Delegate broad searches to subagents
- Keep main context focused on synthesis and decision-making
- Use file-based notes to accumulate findings

#### Step 4: Debug Notes Creation

**When to create debug notes:**
- Investigation is expected to be complex
- Multiple theories need tracking
- Context is being consumed quickly
- Investigation may span multiple sessions

**Debug Notes Structure:**

```markdown
# Debug Session: [Error Summary]

## Error Information
[Full error details]

## Environment
[Relevant environment information]

## Theories
1. [Theory 1]: [likelihood: high/medium/low]
   - Evidence: [supporting information]
   - Test: [how to verify]
   - Result: [pending/confirmed/rejected]

2. [Theory 2]: ...

## Research Findings
- [Source]: [key information]
- [Source]: [key information]

## Tests Conducted
1. [Test description]
   - Command: [test command]
   - Result: [outcome]
   - Conclusion: [what was learned]

## Solution
[Final solution that resolved the issue]
```

Use the template in `assets/debug-notes-template.md` as a starting point.

#### Step 5: Theory Formulation and Testing

**Theory Development:**

Based on research and environment analysis:
1. List all plausible explanations for the error
2. Assess likelihood of each (high/medium/low)
3. Identify evidence supporting or contradicting each theory
4. Order theories by likelihood and ease of testing

**Theory Testing Protocol:**

For each theory (starting with most likely):

1. **Design Test**
   - What command/change will verify or reject this theory?
   - What outcome would confirm the theory?
   - What outcome would reject the theory?

2. **Execute Test**
   - Run the test in a controlled manner
   - Capture all output
   - Note any side effects

3. **Evaluate Result**
   - Does the result confirm or reject the theory?
   - Are there unexpected outcomes?
   - What new information was gained?

4. **Document in Debug Notes**
   - Record test and result
   - Update theory status
   - Note any new theories generated

5. **Iterate**
   - If theory confirmed: proceed to solution implementation
   - If theory rejected: move to next theory
   - If inconclusive: gather more information

**Testing Best Practices:**
- Test one variable at a time
- Use minimal reproducible cases when possible
- Revert changes between theory tests
- Document negative results (what didn't work is valuable information)

### Phase 4: Solution Implementation

Once the correct theory is identified:

1. **Plan Implementation**
   - What changes are needed?
   - Are there risks or side effects?
   - Can the solution be tested incrementally?

2. **Apply Fix**
   - Make the necessary changes
   - Document what was changed
   - Keep changes minimal and focused

3. **Verify Resolution**
   - Re-run the original failing command
   - Confirm error is completely resolved
   - Check for new errors or warnings

4. **Document Solution**
   - Record the fix in debug notes (if created)
   - Note root cause and solution for future reference
   - Consider adding to common error patterns if widely applicable

### Phase 5: Post-Resolution

1. **Clean Up**
   - Remove temporary debug files (if any)
   - Clean up test artifacts
   - Restore any temporary changes

2. **Knowledge Capture**
   - If this was a difficult problem with a general solution, consider documenting it
   - Update `references/common-error-patterns.md` if appropriate
   - Note any tools or techniques that were particularly effective

## Advanced Investigation Techniques

### Bisection Method

For errors introduced by recent changes:
1. Identify last known good state
2. Bisect the changes between good and bad state
3. Test each bisection point
4. Narrow down to the specific change that introduced the error

### Differential Diagnosis

When multiple theories seem equally plausible:
1. Identify distinguishing characteristics of each theory
2. Design tests that differentiate between theories
3. Execute targeted tests to rule out theories
4. Converge on the correct diagnosis through elimination

### Reproduction Reduction

For complex errors:
1. Create minimal reproducible example
2. Strip away unrelated code/configuration
3. Isolate the essential elements that trigger the error
4. Use reduced case for easier investigation

## Communication and Escalation

### When to Request User Input

Request user input when:
- Multiple equally valid solutions exist
- User preference affects solution choice
- Sensitive information access is needed
- Problem domain knowledge is required
- Verification of fix needs user testing

### How to Present Findings

When communicating with user:
1. **Summarize**: Brief description of the error and its cause
2. **Explain**: Why the error occurred
3. **Solution**: What was done to fix it
4. **Verification**: How to confirm it's resolved
5. **Prevention**: How to avoid in the future (if applicable)

## Common Pitfalls to Avoid

1. **Assumption Paralysis**: Don't assume too much; verify theories with tests
2. **Fix Stacking**: Don't apply multiple fixes simultaneously; test one at a time
3. **Context Drift**: Stay focused on the original error; avoid rabbit holes
4. **Incomplete Reversion**: Always fully revert failed fixes
5. **Premature Success**: Verify the error is truly resolved, not just hidden
6. **Privacy Violations**: Never collect sensitive data without permission

## Success Criteria

A troubleshooting session is successful when:
1. The original error is completely resolved
2. The fix is understood and documented
3. No new errors were introduced
4. The solution is appropriate and maintainable
5. Lessons learned are captured for future reference
