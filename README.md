# Claude Code General Skills

A collection of general-purpose skills for [Claude Code](https://claude.com/claude-code).

## Skills

### debug

Apply systematic debugging methodology using medical differential diagnosis principles.

**Key Features:**
- **7-Step Medical Diagnosis Approach**: Systematic workflow from observation to prevention
- **Evidence-Based Investigation**: Prioritize facts over assumptions
- **Differential Diagnosis Lists**: Enumerate all possible failure points before elimination
- **Chain-of-Thought Reasoning**: Transparent deductive process with experimental verification
- **Comprehensive Documentation**: Templates for investigation logs and post-mortem reports

**Triggers on:**
- AI modifies working code and anomalies occur
- Users report unexpected test results or execution failures

**Workflow:**
1. Observe Without Preconception
2. Classify and Isolate Facts
3. Build Differential Diagnosis List
4. Apply Elimination and Deductive Reasoning
5. Experimental Verification and Investigation
6. Locate and Implement Fix
7. Prevention Mechanism

[View skill documentation](./skills/debug/SKILL.md)

### error-troubleshooter

Automatically troubleshoot unexpected results and command/script errors without user request.

**Key Features:**
- **Proactive Investigation**: Automatically activates on unexpected behavior or errors
- **Dual-Mode Troubleshooting**: Handles both explicit failures (stderr, exceptions) and silent anomalies (missing expected effects)
- **Systematic Approach**: Uses error template extraction, hypothesis testing, and web research
- **Scientific Methodology**: Employs "bold hypotheses, careful verification" principles
- **Token Efficient**: Leverages subagents and file-based debugging for complex investigations

**Triggers on:**
- Command succeeded but expected effect didn't happen
- Missing expected errors (e.g., test designed to fail but passed)
- Wrong or unexpected output
- Silent failures
- Explicit errors (SDK/API errors, exceptions, build failures)

[View skill documentation](./skills/error-troubleshooter/SKILL.md)

## Installation

### Option 1: Plugin Installation (Recommended)

Install directly using Claude Code's plugin system:

```bash
# Add this repository as a marketplace
/plugin marketplace add iciakky/cc-general-skills

# Install the plugin
/plugin install cc-general-skills@cc-general-skills

# Restart Claude Code
```

### Option 2: Manual Installation

**Install all skills (Unix/Linux/macOS):**
```bash
git clone https://github.com/iciakky/cc-general-skills.git
cp -r cc-general-skills/skills/debug ~/.claude/skills/
cp -r cc-general-skills/skills/error-troubleshooter ~/.claude/skills/
```

**Install all skills (Windows PowerShell):**
```powershell
git clone https://github.com/iciakky/cc-general-skills.git
Copy-Item -Recurse cc-general-skills\skills\debug $env:USERPROFILE\.claude\skills\
Copy-Item -Recurse cc-general-skills\skills\error-troubleshooter $env:USERPROFILE\.claude\skills\
```

**Install specific skills only:**
Replace `debug` or `error-troubleshooter` with the skill you want to install.

Then restart Claude Code.

### Option 3: Download Release

1. Download the latest skill zip files from [Releases](https://github.com/iciakky/cc-general-skills/releases):
   - `debug.zip` - Systematic debugging with medical diagnosis methodology
   - `error-troubleshooter.zip` - Automatic error troubleshooting
2. Extract to `~/.claude/skills/` (or `%USERPROFILE%\.claude\skills\` on Windows)
3. Restart Claude Code

## Development

### Repository Structure

```
cc-general-skills/
├── .claude-plugin/          # Plugin configuration
│   ├── plugin.json          # Plugin metadata
│   └── marketplace.json     # Marketplace catalog
├── skills/                  # Skills directory
│   ├── debug/
│   │   ├── SKILL.md         # Main skill definition
│   │   ├── references/      # Investigation templates and bug patterns
│   │   ├── assets/          # Report templates
│   │   └── repackage.py     # Build script
│   └── error-troubleshooter/
│       ├── SKILL.md         # Main skill definition
│       ├── references/      # Reference documentation
│       ├── assets/          # Templates and resources
│       └── repackage.py     # Build script
├── .gitignore
├── LICENSE
└── README.md
```

### Repackaging a Skill

Each skill includes a `repackage.py` script for creating distributable zip files:

```bash
# Repackage debug skill
cd skills/debug
python repackage.py

# Repackage error-troubleshooter skill
cd ../error-troubleshooter
python repackage.py
```

This creates `debug.zip` and `error-troubleshooter.zip` in the `skills/` directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Credits

Created with Claude Code's skill-creator tool.
