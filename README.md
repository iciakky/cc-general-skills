# Claude Code General Skills

A collection of general-purpose skills for [Claude Code](https://claude.com/claude-code).

## Skills

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

[View skill documentation](./error-troubleshooter/SKILL.md)

## Installation

### Option 1: Download Release

1. Download `error-troubleshooter.zip` from the releases
2. Extract to `~/.claude/skills/`
3. Restart Claude Code

### Option 2: Manual Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/cc-general-skills.git

# Copy skill to Claude Code skills directory
cp -r cc-general-skills/error-troubleshooter ~/.claude/skills/

# Restart Claude Code
```

## Development

### Repackaging a Skill

Each skill includes a `repackage.py` script for convenience:

```bash
cd error-troubleshooter
python repackage.py
```

This creates a distributable zip file in the parent directory.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Credits

Created with Claude Code's skill-creator tool.
