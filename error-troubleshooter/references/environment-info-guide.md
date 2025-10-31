# Environment Information Collection Guide

This guide provides systematic approaches for gathering environment information during error troubleshooting while maintaining strict privacy and security standards.

## Core Privacy Principles

### Never Collect Without Authorization

**Absolutely Forbidden** (never collect these):
- Passwords or password hashes
- API keys, tokens, or credentials
- Private keys or certificates
- Personal identifiable information (PII): names, emails, addresses, phone numbers
- Financial information
- Session cookies
- Authentication headers
- Database connection strings with credentials

**Requires Explicit User Permission**:
- Project-specific file paths
- Custom configuration files
- Custom environment variables
- Application logs (may contain sensitive data)
- Network configurations
- User-specific system settings

**Generally Safe** (collect without permission):
- Public software versions
- Operating system type and version
- Public package versions
- Standard error messages
- Command outputs that don't reveal sensitive paths or data

### Privacy-First Collection Strategy

1. **Assess Necessity**: Only collect information directly relevant to the error
2. **Request Permission**: When in doubt, ask the user first
3. **Sanitize Output**: Remove sensitive data before recording
4. **Minimize Scope**: Collect the smallest amount needed
5. **Explain Purpose**: Tell the user why specific information is needed

## Environment Information Categories

### 1. System Environment

**What to Collect:**
- Operating system and version
- System architecture (x86, ARM, etc.)
- Shell/terminal type
- Locale and encoding settings

**Collection Commands:**

```bash
# Cross-platform OS detection
# Linux/Mac
uname -a
uname -s  # Just OS name
uname -r  # Just kernel version

# Windows
ver
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"

# Architecture
uname -m  # Linux/Mac
echo %PROCESSOR_ARCHITECTURE%  # Windows

# Locale
locale  # Linux/Mac
echo %LANG%  # Unix-like
chcp  # Windows (code page)
```

**Privacy Notes:**
- These commands generally don't expose sensitive information
- Hostname may be included in `uname -a` output (consider sanitizing)

### 2. Language Runtime Environment

**What to Collect:**
- Programming language version
- Runtime environment details
- Virtual environment status

**Collection Commands by Language:**

#### Python
```bash
# Version
python --version
python3 --version

# Detailed info
python -c "import sys; print(sys.version)"

# Virtual environment detection
echo $VIRTUAL_ENV  # Unix-like
echo %VIRTUAL_ENV%  # Windows

# Python path
python -c "import sys; print(sys.executable)"
```

#### Node.js/JavaScript
```bash
# Versions
node --version
npm --version
yarn --version

# Node environment
echo $NODE_ENV

# Global package location
npm config get prefix
```

#### Java
```bash
# Version
java -version
javac -version

# Runtime details
java -XshowSettings:properties -version 2>&1 | grep 'java.version'
```

#### Ruby
```bash
# Version
ruby --version

# Gem environment
gem env
```

#### Go
```bash
# Version
go version

# Environment
go env
```

**Privacy Notes:**
- Installation paths may reveal usernames (sanitize if needed)
- Custom environment variables may contain sensitive data

### 3. Package Dependencies

**What to Collect:**
- Installed package versions (relevant to error)
- Package manager version
- Dependency conflicts
- Lock file status

**Collection Commands:**

#### Python (pip)
```bash
# Specific package version
pip show <package-name>
pip list | grep <package-name>

# All packages (use sparingly, large output)
pip list

# Dependency conflicts
pip check

# Requirements file
cat requirements.txt  # Request permission first
```

#### Python (conda)
```bash
# Environment info
conda info

# Installed packages
conda list <package-name>

# Environment exports
conda env export  # Use with caution, may be large
```

#### Node.js (npm)
```bash
# Specific package version
npm list <package-name>
npm view <package-name> version

# Global packages
npm list -g --depth=0

# Dependency audit
npm doctor
npm audit

# Lock file status
ls -l package-lock.json
```

#### Ruby (gem)
```bash
# Specific gem version
gem list <gem-name>

# All gems
gem list

# Gem environment
gem env
```

**Privacy Notes:**
- Package lists can be large; collect only relevant packages when possible
- Lock files may contain private registry URLs (review before sharing)
- Package names might reveal business logic (request permission for private packages)

### 4. Configuration Files

**What to Collect:**
Configuration files often contain sensitive data. Always exercise caution.

**Approach:**
1. **Identify relevant config**: Only collect configs directly related to the error
2. **Request permission**: Always ask before reading project-specific configs
3. **Sanitize**: Remove credentials, API keys, and sensitive values before recording
4. **Provide context**: Explain why the config is needed

**Common Configuration Files:**

```bash
# Python
# - setup.py, setup.cfg, pyproject.toml, tox.ini

# Node.js
# - package.json (usually safe), .npmrc (check for tokens)

# General
# - .env files (NEVER share without sanitization)
# - config.json, config.yaml (sanitize before sharing)
```

**Sanitization Example:**

```yaml
# Before sanitization
database:
  host: db.example.com
  username: admin
  password: super_secret_123
  port: 5432

# After sanitization
database:
  host: [REDACTED]
  username: [REDACTED]
  password: [REDACTED]
  port: 5432
```

### 5. Environment Variables

**What to Collect:**
Environment variables often contain sensitive data. Collect with extreme caution.

**Approach:**
1. **Be Specific**: Only check specific, relevant variables
2. **Avoid Wildcards**: Never do `env` or `printenv` without filtering
3. **Sanitize**: Redact values that might be sensitive
4. **Public Variables Only**: Prefer checking well-known, non-sensitive variables

**Safe Environment Variables:**

```bash
# Locale and encoding
echo $LANG
echo $LC_ALL

# Shell
echo $SHELL

# Path (usually safe, but may reveal usernames)
echo $PATH

# Node environment
echo $NODE_ENV

# Python path
echo $PYTHONPATH
```

**Potentially Sensitive Variables:**

```bash
# Requires permission or sanitization
# - API keys: $API_KEY, $SECRET_KEY, $TOKEN
# - Database URLs: $DATABASE_URL
# - Credentials: $USERNAME, $PASSWORD
# - Custom app settings: $APP_* variables
```

**Collection Command (filtered):**

```bash
# Safe: Check specific variable
echo $LANG

# Risky: List all variables (AVOID unless necessary)
env
printenv

# Better: Filter for specific patterns
env | grep -i "^PYTHON"
env | grep -i "^NODE"
```

### 6. Network and Connectivity

**What to Collect:**
- Network connectivity status
- DNS resolution (for external services)
- Proxy settings
- Firewall status (general)

**Collection Commands:**

```bash
# Test connectivity
ping -c 4 google.com  # Linux/Mac
ping -n 4 google.com  # Windows

# DNS resolution
nslookup example.com
dig example.com  # Linux/Mac

# Proxy settings (may contain credentials - sanitize)
echo $HTTP_PROXY
echo $HTTPS_PROXY

# Network interfaces (general info)
ifconfig  # Linux/Mac
ipconfig  # Windows

# Firewall status (general)
sudo ufw status  # Linux (Ubuntu)
netsh advfirewall show allprofiles  # Windows (requires admin)
```

**Privacy Notes:**
- Internal IP addresses are generally low-risk
- Proxy settings may contain authentication credentials (sanitize)
- Network topology might be sensitive in enterprise environments

### 7. File System and Permissions

**What to Collect:**
- File existence and permissions (for files mentioned in error)
- Directory structure (limited)
- Disk space (if relevant)

**Collection Commands:**

```bash
# File info (request permission if non-system file)
ls -la /path/to/file  # Linux/Mac
dir /path/to/file  # Windows

# Permissions
stat /path/to/file  # Linux/Mac

# Disk space
df -h  # Linux/Mac
wmic logicaldisk get size,freespace,caption  # Windows

# Check if file exists
test -f /path/to/file && echo "exists" || echo "not found"
```

**Privacy Notes:**
- File paths may reveal usernames or project structure (request permission)
- Avoid listing directory contents unless necessary

## Collection Workflow

### Step 1: Assess Relevance

Before collecting any information, ask:
- Is this directly related to the error?
- Will this information help diagnose or resolve the issue?
- Is there a less invasive way to get the same information?

### Step 2: Categorize Sensitivity

Classify the information:
- **Public**: Widely available, non-sensitive (e.g., OS version)
- **Private**: User-specific but non-confidential (e.g., package versions)
- **Confidential**: May contain sensitive data (e.g., config files)
- **Secret**: Credentials, keys, PII (NEVER collect without explicit permission)

### Step 3: Request Permission When Needed

For private or confidential information:

```
"To diagnose this error, I need to check [specific information].
This will involve [specific action].
Is it okay to proceed?"
```

Example:
```
"To diagnose this database connection error, I need to check your database
configuration settings. This will involve reading the config/database.yml file.
Any sensitive values will be redacted. Is it okay to proceed?"
```

### Step 4: Collect and Sanitize

Execute the collection command and immediately sanitize:

1. **Capture output**
2. **Review for sensitive data**
3. **Redact or replace sensitive values**
4. **Document what was redacted**

### Step 5: Document Collection

Record what was collected and why:
- What information was gathered
- Why it was needed
- What commands were used
- What was sanitized

## Sanitization Techniques

### Pattern-Based Redaction

Common patterns to redact:

```bash
# API keys (various formats)
AIza[0-9A-Za-z-_]{35}  # Google API keys
sk_live_[0-9a-zA-Z]{24}  # Stripe keys
[0-9a-f]{32}  # Generic 32-char hex keys

# Email addresses
[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}

# URLs with credentials
https?://[^:]+:[^@]+@[^/]+

# IP addresses (if needed)
\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b

# File paths with usernames
/home/[^/]+/  -> /home/[USERNAME]/
C:\\Users\\[^\\]+\\  -> C:\Users\[USERNAME]\
```

### Replacement Strategies

```bash
# Replace with generic placeholder
password: super_secret_123  →  password: [REDACTED]

# Replace with type indicator
api_key: sk_live_abc123xyz  →  api_key: [API_KEY]

# Partial redaction
email: john.doe@example.com  →  email: [***]@example.com

# Anonymize paths
/home/john/project  →  /home/[USER]/project
```

## Quick Reference: Collection Decision Tree

```
Need environment information?
    ↓
Is it sensitive or user-specific?
    ├─ NO → Collect directly
    │        (e.g., OS version, Python version)
    │
    └─ YES → Does it contain credentials or PII?
               ├─ YES → Request explicit permission
               │         ↓
               │      Permission granted?
               │         ├─ YES → Collect and sanitize
               │         └─ NO → Find alternative approach
               │
               └─ NO → Is it project-specific?
                        ├─ YES → Request permission
                        └─ NO → Collect and sanitize proactively
```

## Common Scenarios

### Scenario 1: Module Not Found Error

**Information Needed:**
- Python version
- pip version
- Virtual environment status
- Package installation status

**Collection:**
```bash
python --version
pip --version
echo $VIRTUAL_ENV
pip show <package-name>
```

**Privacy Impact:** Low (all public information)

### Scenario 2: Database Connection Error

**Information Needed:**
- Database client version
- Connection configuration (sanitized)
- Network connectivity

**Collection:**
```bash
# Client version (safe)
psql --version  # PostgreSQL
mysql --version  # MySQL

# Configuration (REQUIRES PERMISSION)
# Request permission, then read config with sanitization

# Connectivity (safe)
ping -c 4 database.host.com
nslookup database.host.com
```

**Privacy Impact:** Medium-High (config contains credentials)

### Scenario 3: Build Failure

**Information Needed:**
- Compiler/build tool version
- System libraries
- Build configuration

**Collection:**
```bash
# Build tools (safe)
gcc --version
make --version
cmake --version

# Package manager (safe)
apt list --installed | grep <lib-name>  # Debian/Ubuntu
brew info <lib-name>  # macOS

# Build config (request permission for project-specific)
cat CMakeLists.txt
cat Makefile
```

**Privacy Impact:** Low-Medium (build config might reveal project details)

## Best Practices Summary

1. **Collect Minimally**: Only gather what's directly relevant
2. **Request Permission**: When information is user-specific or potentially sensitive
3. **Sanitize Proactively**: Remove credentials and PII before recording
4. **Document Purpose**: Explain why information is needed
5. **Validate Necessity**: Double-check if collection is truly required
6. **Use Specific Commands**: Avoid broad commands like `env` or `find /`
7. **Respect User Privacy**: When uncertain, err on the side of asking permission
8. **Provide Context**: Help users understand what information will be accessed

## Red Flags: Never Collect

- Raw credential files (.env, credentials.json)
- Browser cookies or session storage
- SSH keys or SSL certificates
- Database dumps
- Full process listings (might expose arguments with credentials)
- Complete environment variable dumps
- User home directory listings
- Git repository contents (without permission)
- Application logs (without permission and sanitization)
