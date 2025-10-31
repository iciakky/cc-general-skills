# Common Error Patterns and Quick Fixes

This reference documents frequently encountered trivial errors and their known solutions. Use this for rapid diagnosis and resolution of common issues.

## How to Use This Reference

1. **Pattern Match**: Compare the error against patterns in this document
2. **Apply Fix**: If there's a high-confidence match, apply the suggested fix
3. **Verify**: Confirm the fix resolved the issue
4. **Escalate**: If fix fails, revert and proceed to rigorous investigation

**Important**: Only apply quick fixes when confident. If the first attempt doesn't work, revert and use systematic troubleshooting.

## Python Common Errors

### 1. ModuleNotFoundError / ImportError

**Pattern:**
```
ModuleNotFoundError: No module named 'package_name'
ImportError: cannot import name 'something' from 'package'
```

**Common Causes & Fixes:**

#### Cause 1: Package Not Installed
```bash
# Fix
pip install package_name

# Or if using requirements.txt
pip install -r requirements.txt
```

#### Cause 2: Wrong Python Environment
```bash
# Check current Python
which python
python --version

# Activate correct virtual environment
source venv/bin/activate  # Unix
.\venv\Scripts\activate  # Windows

# Or use python3 explicitly
pip3 install package_name
```

#### Cause 3: Package Name Mismatch
```bash
# Install name might differ from import name
# Example: pip install Pillow, but import PIL
pip install Pillow  # for 'import PIL'
pip install opencv-python  # for 'import cv2'
pip install scikit-learn  # for 'import sklearn'
```

#### Cause 4: Circular Import
- Check if files are importing each other
- Restructure imports or use lazy imports

### 2. SyntaxError

**Pattern:**
```
SyntaxError: invalid syntax
SyntaxError: unexpected EOF while parsing
```

**Common Causes & Fixes:**

#### Cause 1: Missing Colon
```python
# Wrong
if condition
    do_something()

# Right
if condition:
    do_something()
```

#### Cause 2: Unclosed Brackets/Quotes
```python
# Wrong
result = calculate(x, y
print("Hello world)

# Right
result = calculate(x, y)
print("Hello world")
```

#### Cause 3: Python Version Incompatibility
```python
# f-strings require Python 3.6+
print(f"Value: {x}")  # SyntaxError in Python 3.5

# Walrus operator requires Python 3.8+
if (n := len(items)) > 10:  # SyntaxError in Python 3.7
```

**Fix:** Check Python version and upgrade if needed

### 3. IndentationError

**Pattern:**
```
IndentationError: unexpected indent
IndentationError: expected an indented block
```

**Common Causes & Fixes:**

#### Cause: Mixed Tabs and Spaces
```bash
# Fix: Convert to spaces (recommended)
# In most editors: Settings → Convert indentation to spaces

# Or use autopep8
pip install autopep8
autopep8 --in-place --select=E101,E121 file.py
```

### 4. AttributeError

**Pattern:**
```
AttributeError: 'NoneType' object has no attribute 'something'
AttributeError: module 'X' has no attribute 'Y'
```

**Common Causes & Fixes:**

#### Cause 1: None Value
```python
# Function returned None when you expected object
result = function_that_returns_none()
result.method()  # AttributeError

# Fix: Check for None
if result is not None:
    result.method()
```

#### Cause 2: Wrong Module Version
```bash
# API changed in new version
pip show package_name  # Check version
pip install package_name==1.2.3  # Install specific version
```

#### Cause 3: Module Not Reloaded
```python
# In interactive session/Jupyter
import importlib
importlib.reload(module_name)
```

### 5. FileNotFoundError

**Pattern:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'path/to/file'
```

**Common Causes & Fixes:**

#### Cause 1: Wrong Current Directory
```python
# Check current directory
import os
print(os.getcwd())

# Fix: Use absolute path or change directory
os.chdir('/correct/path')
# Or use absolute path
file_path = os.path.join(os.path.dirname(__file__), 'data', 'file.txt')
```

#### Cause 2: Typo in Path
- Check file name spelling (case-sensitive on Unix)
- Check file extension

#### Cause 3: File Doesn't Exist Yet
```python
# Create file if it doesn't exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)
with open(file_path, 'w') as f:
    f.write('')
```

## JavaScript/Node.js Common Errors

### 1. Cannot find module

**Pattern:**
```
Error: Cannot find module 'module-name'
```

**Common Causes & Fixes:**

#### Cause 1: Module Not Installed
```bash
# Fix
npm install module-name

# Or restore all dependencies
npm install
```

#### Cause 2: Wrong Node Version
```bash
# Check required version in package.json
cat package.json | grep "engines"

# Use nvm to switch version
nvm install 16
nvm use 16
```

#### Cause 3: Module Path Error
```javascript
// Wrong (relative path without ./)
const myModule = require('utils/helper')

// Right
const myModule = require('./utils/helper')
```

### 2. Reference Error

**Pattern:**
```
ReferenceError: X is not defined
```

**Common Causes & Fixes:**

#### Cause 1: Variable Not Declared
```javascript
// Wrong
console.log(myVar)  // ReferenceError

// Right
const myVar = 'value'
console.log(myVar)
```

#### Cause 2: Scope Issue
```javascript
// Wrong
if (true) {
  var x = 1
}
console.log(x)  // Works with var, but not with let/const

// Right
let x
if (true) {
  x = 1
}
console.log(x)
```

#### Cause 3: Typo in Variable Name
- Check spelling and case (JavaScript is case-sensitive)

### 3. SyntaxError: Unexpected token

**Pattern:**
```
SyntaxError: Unexpected token 'x'
SyntaxError: Unexpected token {
```

**Common Causes & Fixes:**

#### Cause 1: JSON Parsing Error
```javascript
// Wrong: Invalid JSON
const data = JSON.parse("{'key': 'value'}")  // Single quotes not valid JSON

// Right: Valid JSON
const data = JSON.parse('{"key": "value"}')
```

#### Cause 2: Missing Semicolons/Commas
```javascript
// Wrong
const obj = {
  key1: 'value1'
  key2: 'value2'
}

// Right
const obj = {
  key1: 'value1',
  key2: 'value2'
}
```

#### Cause 3: ES6 Syntax in Old Node
```javascript
// Arrow functions require Node 4+
const func = () => {}

// async/await requires Node 7.6+
async function test() { await promise }
```

**Fix:** Upgrade Node or use transpiler (Babel)

### 4. ECONNREFUSED

**Pattern:**
```
Error: connect ECONNREFUSED 127.0.0.1:3000
```

**Common Causes & Fixes:**

#### Cause 1: Server Not Running
```bash
# Fix: Start the server
npm start
node server.js
```

#### Cause 2: Wrong Port
```javascript
// Check server port in code
const PORT = process.env.PORT || 3000

// Ensure client uses same port
```

#### Cause 3: Firewall Blocking
```bash
# Check if port is listening
netstat -an | grep 3000  # Unix
netstat -an | findstr 3000  # Windows
```

### 5. EADDRINUSE

**Pattern:**
```
Error: listen EADDRINUSE: address already in use :::3000
```

**Common Causes & Fixes:**

#### Fix 1: Kill Process Using Port
```bash
# Unix/Linux/Mac
lsof -ti:3000 | xargs kill
# Or
kill $(lsof -t -i:3000)

# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

#### Fix 2: Use Different Port
```javascript
const PORT = process.env.PORT || 3001  // Change port
```

## Git Common Errors

### 1. Permission Denied (publickey)

**Pattern:**
```
Permission denied (publickey).
fatal: Could not read from remote repository.
```

**Common Causes & Fixes:**

#### Cause: SSH Key Not Set Up
```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to SSH agent
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519

# Copy public key and add to GitHub/GitLab
cat ~/.ssh/id_ed25519.pub
```

### 2. Merge Conflict

**Pattern:**
```
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**Common Causes & Fixes:**

#### Standard Resolution
```bash
# 1. Open conflicted files and resolve markers
# <<<<<<< HEAD
# =======
# >>>>>>> branch-name

# 2. Stage resolved files
git add file.txt

# 3. Complete merge
git commit
```

### 3. Detached HEAD

**Pattern:**
```
You are in 'detached HEAD' state.
```

**Common Causes & Fixes:**

#### Fix: Create Branch or Return to Branch
```bash
# Option 1: Create branch at current commit
git checkout -b new-branch-name

# Option 2: Return to main branch
git checkout main
```

## Docker Common Errors

### 1. Cannot connect to Docker daemon

**Pattern:**
```
Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
```

**Common Causes & Fixes:**

#### Cause 1: Docker Not Running
```bash
# Start Docker
sudo systemctl start docker  # Linux
# Or start Docker Desktop (Mac/Windows)
```

#### Cause 2: Permission Issue
```bash
# Add user to docker group
sudo usermod -aG docker $USER
# Then logout and login again
```

### 2. Port Already Allocated

**Pattern:**
```
Error starting userland proxy: listen tcp 0.0.0.0:8080: bind: address already in use
```

**Common Causes & Fixes:**

#### Fix 1: Stop Conflicting Container
```bash
# Find container using port
docker ps | grep 8080

# Stop it
docker stop <container_id>
```

#### Fix 2: Use Different Port
```bash
# Change port mapping
docker run -p 8081:8080 image_name
```

### 3. No Space Left on Device

**Pattern:**
```
Error: No space left on device
```

**Common Causes & Fixes:**

#### Fix: Clean Up Docker Resources
```bash
# Remove unused containers, images, volumes
docker system prune -a --volumes

# Or selectively
docker container prune
docker image prune -a
docker volume prune
```

## Database Common Errors

### 1. Connection Refused

**Pattern:**
```
Error: connect ECONNREFUSED 127.0.0.1:5432
psycopg2.OperationalError: could not connect to server: Connection refused
```

**Common Causes & Fixes:**

#### Cause 1: Database Not Running
```bash
# PostgreSQL
sudo systemctl start postgresql  # Linux
brew services start postgresql  # Mac

# MySQL
sudo systemctl start mysql  # Linux
brew services start mysql  # Mac

# MongoDB
sudo systemctl start mongod  # Linux
brew services start mongodb-community  # Mac
```

#### Cause 2: Wrong Port
- PostgreSQL default: 5432
- MySQL default: 3306
- MongoDB default: 27017

#### Cause 3: Wrong Host
```python
# Wrong
host='localhost'

# Try
host='127.0.0.1'
# Or check actual host in database config
```

### 2. Authentication Failed

**Pattern:**
```
Authentication failed for user 'username'
Access denied for user 'username'@'localhost'
```

**Common Causes & Fixes:**

#### Fix: Check Credentials
```bash
# PostgreSQL: Check user exists
psql -U postgres
\du  # List users

# MySQL: Check user exists
mysql -u root -p
SELECT User, Host FROM mysql.user;

# Reset password if needed
ALTER USER 'username' IDENTIFIED BY 'new_password';
```

### 3. Database Does Not Exist

**Pattern:**
```
FATAL: database "dbname" does not exist
ERROR 1049 (42000): Unknown database 'dbname'
```

**Common Causes & Fixes:**

#### Fix: Create Database
```sql
-- PostgreSQL
CREATE DATABASE dbname;

-- MySQL
CREATE DATABASE dbname;

-- Or use command line
createdb dbname  # PostgreSQL
mysql -e "CREATE DATABASE dbname"  # MySQL
```

## Package Manager Common Errors

### 1. npm: EACCES Permission Denied

**Pattern:**
```
npm ERR! code EACCES
npm ERR! EACCES: permission denied
```

**Common Causes & Fixes:**

#### Fix: Don't Use Sudo (Instead Fix Permissions)
```bash
# Fix npm global directory permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile
source ~/.profile
```

### 2. pip: Could Not Find a Version

**Pattern:**
```
ERROR: Could not find a version that satisfies the requirement package_name
```

**Common Causes & Fixes:**

#### Cause 1: Typo in Package Name
```bash
# Fix: Check correct name on PyPI
pip search package_name  # (Note: search disabled on PyPI)
# Or search on https://pypi.org
```

#### Cause 2: Python Version Incompatibility
```bash
# Check Python version
python --version

# Some packages require specific Python versions
# Upgrade Python or find compatible package version
pip install package_name==1.2.3
```

#### Cause 3: No Internet / Proxy Issue
```bash
# Check connectivity
ping pypi.org

# If behind proxy
pip install --proxy http://proxy:port package_name
```

### 3. Requirements File Error

**Pattern:**
```
ERROR: Invalid requirement: 'package_name==1.0.0\r' (from line X of requirements.txt)
```

**Common Causes & Fixes:**

#### Cause: Windows Line Endings
```bash
# Fix: Convert to Unix line endings
dos2unix requirements.txt

# Or with Python
python -c "import sys; data = open('requirements.txt', 'r').read(); open('requirements.txt', 'w').write(data.replace('\r\n', '\n'))"
```

## Build Tool Common Errors

### 1. Make: Command Not Found

**Pattern:**
```
make: command not found
```

**Common Causes & Fixes:**

#### Fix: Install Build Tools
```bash
# Debian/Ubuntu
sudo apt-get install build-essential

# macOS
xcode-select --install

# CentOS/RHEL
sudo yum groupinstall "Development Tools"
```

### 2. Compiler Error: Missing Header

**Pattern:**
```
fatal error: Python.h: No such file or directory
fatal error: openssl/ssl.h: No such file or directory
```

**Common Causes & Fixes:**

#### Fix: Install Development Headers
```bash
# Python headers
sudo apt-get install python3-dev  # Debian/Ubuntu
sudo yum install python3-devel  # CentOS/RHEL

# OpenSSL headers
sudo apt-get install libssl-dev  # Debian/Ubuntu
sudo yum install openssl-devel  # CentOS/RHEL
```

## Cross-Platform Path Issues

### Windows Backslash vs Unix Forward Slash

**Pattern:**
```
FileNotFoundError: [Errno 2] No such file or directory: 'path\\to\\file'
```

**Common Causes & Fixes:**

#### Fix: Use os.path or pathlib
```python
# Wrong (platform-specific)
path = 'C:\\Users\\name\\file.txt'  # Windows only
path = '/home/user/file.txt'  # Unix only

# Right (cross-platform)
import os
path = os.path.join('Users', 'name', 'file.txt')

# Or use pathlib (Python 3.4+)
from pathlib import Path
path = Path('Users') / 'name' / 'file.txt'
```

## Quick Diagnosis Checklist

When encountering an error, quickly check:

- [ ] Is the tool/service running?
- [ ] Are dependencies installed?
- [ ] Is it a typo (file name, variable, import)?
- [ ] Am I in the right directory?
- [ ] Am I using the right version (Python, Node, package)?
- [ ] Am I in the right environment (virtual env, conda env)?
- [ ] Is there a port conflict?
- [ ] Do I have proper permissions?
- [ ] Are there network/firewall issues?
- [ ] Did I check the error message carefully?

## Adding New Patterns

As new common errors are discovered during troubleshooting:

1. **Document the pattern**: Error message template
2. **Document the cause**: Why it happens
3. **Document the fix**: Step-by-step solution
4. **Test the fix**: Verify it works reliably
5. **Add to this file**: So it's available for future use

**Format:**
```markdown
### N. Brief Error Description

**Pattern:**
```
Error message pattern
```

**Common Causes & Fixes:**

#### Cause 1: Specific Cause
```bash
# Fix
command or code to fix
```

**Notes:** Additional context or warnings
```
