# Error Template Pattern Recognition

This guide explains how to identify and extract error message templates for effective web searching and pattern matching.

## Why Extract Templates?

SDK and API errors typically follow fixed templates with variable components. Searching for the full error (including variables like file paths, user inputs, or IDs) rarely yields useful results. Extracting the template allows finding relevant discussions and solutions that apply to your specific case.

## Template Extraction Process

### Step 1: Identify the Error Structure

Most errors follow this general structure:

```
[Error Type/Class]: [Core Message] [Additional Context] [Variable Details]
```

**Example:**
```
FileNotFoundError: [Errno 2] No such file or directory: '/home/user/data.csv'
                   ↑          ↑                          ↑
               Error Code   Core Message           Variable (Path)
```

### Step 2: Categorize Components

Classify each part of the error message:

#### Fixed Components (Keep These)
- Error type/class names (e.g., `ValueError`, `TypeError`, `ConnectionError`)
- Standard error codes (e.g., `[Errno 2]`, `HTTP 404`, `ENOENT`)
- Core message structure (e.g., "No such file or directory")
- Standard library/SDK function names
- Generic parameter names in templates (e.g., "expected {type}, got {type}")

#### Variable Components (Remove These)
- File system paths: `/home/user/project/file.py`, `C:\Users\Name\file.txt`
- URLs: `https://api.example.com/endpoint`
- User inputs: `'user_entered_value'`, `"some string"`
- Identifiers: UUIDs, database IDs, session tokens
- Timestamps: `2024-01-15 10:30:45`, `1642234567`
- Usernames/emails: `john@example.com`, `user123`
- Line numbers: `line 42` (unless part of standard template)
- Function call arguments: `function(arg1='value', arg2=123)`
- IP addresses and ports: `192.168.1.1:8080`

### Step 3: Extract the Template

Remove all variable components while preserving the error structure.

## Template Extraction Examples

### Python Errors

#### Example 1: Import Error
```
Original:
ModuleNotFoundError: No module named 'pandas'

Template:
ModuleNotFoundError No module named

Reasoning:
- 'ModuleNotFoundError': Error class (keep)
- 'No module named': Core message (keep)
- 'pandas': Specific module name (remove - variable)
```

#### Example 2: Type Error
```
Original:
TypeError: unsupported operand type(s) for +: 'int' and 'str' at line 42 in /home/user/script.py

Template:
TypeError unsupported operand type(s) for

Reasoning:
- 'TypeError': Error class (keep)
- 'unsupported operand type(s) for': Core message (keep)
- '+: 'int' and 'str'': Specific types and operator (remove - variable)
- 'at line 42': Line number (remove - variable)
- '/home/user/script.py': File path (remove - variable)
```

#### Example 3: Value Error
```
Original:
ValueError: invalid literal for int() with base 10: 'abc'

Template:
ValueError invalid literal for int() with base 10

Reasoning:
- 'ValueError': Error class (keep)
- 'invalid literal for int() with base 10': Standard message (keep)
- 'abc': User input value (remove - variable)
```

### JavaScript/Node.js Errors

#### Example 4: Reference Error
```
Original:
ReferenceError: myVariable is not defined at Object.<anonymous> (/home/user/project/app.js:15:5)

Template:
ReferenceError is not defined

Reasoning:
- 'ReferenceError': Error type (keep)
- 'is not defined': Core message (keep)
- 'myVariable': Specific variable name (remove - variable)
- Location information: (remove - variable)
```

#### Example 5: Network Error
```
Original:
Error: connect ECONNREFUSED 127.0.0.1:3000 at TCPConnectWrap.afterConnect [as oncomplete]

Template:
Error connect ECONNREFUSED

Reasoning:
- 'Error': Error type (keep)
- 'connect': Operation (keep)
- 'ECONNREFUSED': Standard error code (keep)
- '127.0.0.1:3000': IP and port (remove - variable)
- Stack trace info: (remove - variable)
```

### HTTP/API Errors

#### Example 6: HTTP Error
```
Original:
requests.exceptions.HTTPError: 404 Client Error: Not Found for url: https://api.example.com/v1/users/12345

Template:
requests.exceptions.HTTPError 404 Client Error Not Found

Reasoning:
- 'requests.exceptions.HTTPError': Exception class (keep)
- '404': Standard HTTP status code (keep)
- 'Client Error: Not Found': Standard HTTP message (keep)
- URL: (remove - variable)
```

#### Example 7: Connection Error
```
Original:
requests.exceptions.ConnectionError: HTTPConnectionPool(host='api.example.com', port=443): Max retries exceeded with url: /v1/users (Caused by NewConnectionError)

Template:
requests.exceptions.ConnectionError HTTPConnectionPool Max retries exceeded

Reasoning:
- Exception class (keep)
- 'HTTPConnectionPool', 'Max retries exceeded': Core message components (keep)
- Host, port, URL: (remove - variable)
- Specific cause details: (remove - variable)
```

### Database Errors

#### Example 8: SQL Error
```
Original:
psycopg2.errors.UniqueViolation: duplicate key value violates unique constraint "users_email_key" DETAIL: Key (email)=(john@example.com) already exists.

Template:
psycopg2.errors.UniqueViolation duplicate key value violates unique constraint

Reasoning:
- Error class (keep)
- Core message structure (keep)
- Constraint name, field value: (remove - variable)
```

### File System Errors

#### Example 9: Permission Error
```
Original:
PermissionError: [Errno 13] Permission denied: '/var/log/app.log'

Template:
PermissionError [Errno 13] Permission denied

Reasoning:
- Error type (keep)
- Error code (keep)
- Core message (keep)
- File path: (remove - variable)
```

### Package Manager Errors

#### Example 10: NPM Error
```
Original:
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree for myproject@1.0.0

Template:
npm ERR! code ERESOLVE unable to resolve dependency tree

Reasoning:
- Error prefix and code (keep)
- Core message (keep)
- Package name and version: (remove - variable)
```

## Common Patterns by Language/Framework

### Python Standard Templates
- `[ErrorType]: [Message]`
- `[ErrorType]: [Message] at line [number] in [file]`
- `[Module].[ErrorType]: [Message]`

### JavaScript/Node Standard Templates
- `[ErrorType]: [Message] at [Location]`
- `Error: [Operation] [ErrorCode]`
- `Unhandled [PromiseRejection/Error]: [Message]`

### HTTP/REST API Templates
- `[StatusCode] [StatusMessage]: [Description]`
- `[Library].[Exception]: [StatusCode] [Message]`

### Database Templates
- `[Driver].[ErrorType]: [Message]`
- `[Database] Error [Code]: [Message]`

## Template Quality Checklist

A good error template should:

✓ Be searchable (yields relevant results on Stack Overflow/GitHub)
✓ Be generic (applies to multiple specific instances of the error)
✓ Retain error classification (type/class name)
✓ Preserve standard error codes
✓ Remove all user-specific or environment-specific details
✓ Be concise (typically 3-8 words)

## Testing Your Template

After extracting a template, validate it:

1. **Search Test**: Search the template on Stack Overflow or Google
   - Good template: Returns relevant discussions about the error type
   - Bad template: Returns no results or overly specific results

2. **Generalization Test**: Would this template match similar errors from other users?
   - Good template: Yes, it matches the general pattern
   - Bad template: No, it's too specific to your case

3. **Specificity Test**: Is the template specific enough to be useful?
   - Good template: Identifies a specific error condition
   - Bad template: Too vague (e.g., just "Error")

## Advanced: Multi-Error Messages

Some errors contain multiple nested errors or stack traces:

### Example: Nested Errors
```
Original:
RuntimeError: Failed to initialize module
  Caused by: ImportError: cannot import name 'foo' from 'bar' (/path/to/bar.py)
    Caused by: AttributeError: module 'bar' has no attribute 'foo'

Template Approach:
- Extract primary error: "RuntimeError Failed to initialize module"
- Extract root cause: "AttributeError module has no attribute"
- Search both templates for comprehensive results
```

**Strategy**: Extract templates for both the outer error and the root cause, as either may lead to relevant solutions.

## Quick Reference: Variable Component Checklist

Remove these from error messages:
- [ ] File paths (absolute or relative)
- [ ] URLs and domains
- [ ] User inputs and arguments
- [ ] Database record IDs
- [ ] Session tokens and API keys
- [ ] Timestamps and dates
- [ ] IP addresses and ports
- [ ] Usernames and emails
- [ ] Line numbers (usually)
- [ ] Stack trace locations
- [ ] Variable names (user-defined)
- [ ] Specific package versions (unless relevant to breaking changes)

Keep these in templates:
- [x] Error type/class names
- [x] Standard error codes
- [x] Core message structure
- [x] Standard library function names
- [x] HTTP status codes
- [x] Generic type names (when part of template)
- [x] Standard operations (e.g., "connect", "read", "write")

## Practice Examples

Try extracting templates from these errors:

### Exercise 1
```
JSONDecodeError: Expecting value: line 1 column 1 (char 0) in /home/user/data.json
```

<details>
<summary>Answer</summary>
Template: `JSONDecodeError Expecting value`

Reasoning: Remove line/column numbers and file path; keep error type and core message.
</details>

### Exercise 2
```
AssertionError: Expected response status 200, got 404 for endpoint /api/users
```

<details>
<summary>Answer</summary>
Template: `AssertionError Expected response status got`

Reasoning: Remove specific status codes and endpoint; keep error type and message structure.
</details>

### Exercise 3
```
sqlalchemy.exc.OperationalError: (psycopg2.OperationalError) could not connect to server: Connection refused on port 5432
```

<details>
<summary>Answer</summary>
Template: `sqlalchemy.exc.OperationalError could not connect to server Connection refused`

Reasoning: Keep full error class path and core message; remove port number.
</details>
