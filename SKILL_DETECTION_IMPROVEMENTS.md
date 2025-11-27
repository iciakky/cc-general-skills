# Skill Detection Improvements

## Problem Analysis

The original skill descriptions were not being easily detected by Claude because:

1. **Too verbose**: Included too many implementation details
2. **Unclear differentiation**: Both skills dealt with debugging, unclear when to use which
3. **Lack of trigger keywords**: Missing common user phrases that would trigger the skills
4. **Passive language**: Descriptions focused on methodology rather than clear use cases

## Improvements Made

### 1. error-troubleshooter: First Responder

**Old Description:**
> Automatically troubleshoot unexpected results OR command/script errors without user request. Triggers when: (1) unexpected behavior - command succeeded but expected effect didn't happen, missing expected errors, wrong output, silent failures; (2) explicit failures - stderr, exceptions, non-zero exit, SDK/API errors. Applies systematic diagnosis using error templates, hypothesis testing, and web research for any Stack Overflow-worthy issue.

**New Description:**
> First responder for ANY error or unexpected behavior. Auto-trigger on stderr, exceptions, test failures, wrong output, or when things don't work as expected. Quick-fix simple issues; systematically investigate complex ones using error patterns, web research, and hypothesis testing. Use when you see errors, bugs, failures, or "something's wrong".

**Key Improvements:**
- ✅ Clear role: "First responder"
- ✅ Trigger keywords: errors, bugs, failures, "something's wrong"
- ✅ Action-oriented: "Auto-trigger on..."
- ✅ Concise and scannable

### 2. debug: Deep Investigation

**Old Description:**
> Apply systematic debugging methodology using medical differential diagnosis principles. Trigger when AI modifies working code and anomalies occur, or when users report unexpected test results or execution failures. Use observation without preconception, fact isolation, differential diagnosis lists, deductive exclusion, experimental verification, precise fixes, and prevention mechanisms.

**New Description:**
> Deep investigation tool for complex bugs using medical diagnosis methodology. Use when simple troubleshooting fails, for intermittent issues, race conditions, or when user says "I've tried everything". Applies 7-step process: observe facts, classify symptoms, differential diagnosis, deductive elimination, experimental verification, precise fix, prevention. For difficult bugs needing rigorous analysis.

**Key Improvements:**
- ✅ Clear positioning: "Deep investigation tool"
- ✅ Clear trigger: "when simple troubleshooting fails", "I've tried everything"
- ✅ Specific use cases: intermittent issues, race conditions
- ✅ Concise process summary

## Role Differentiation

The two skills now have clear, distinct roles:

| Skill | Role | When to Use | Approach |
|-------|------|-------------|----------|
| **error-troubleshooter** | First responder | ANY error or unexpected behavior | Quick-fix → Systematic investigation |
| **debug** | Deep investigator | Complex/persistent bugs | Medical diagnosis methodology |

## Expected Impact

With these improvements, Claude should:

1. **Automatically trigger error-troubleshooter** when encountering any error or unexpected behavior
2. **Escalate to debug** when error-troubleshooter's attempts fail or for inherently complex issues
3. **Respond to user keywords** like "bug", "error", "not working", "I've tried everything"
4. **Better understand** which tool to use based on problem complexity

## Testing Recommendations

Test these scenarios to validate improvements:

1. Simple error: `SyntaxError: unexpected token` → Should trigger error-troubleshooter
2. Persistent issue: "I've tried 3 different fixes, still broken" → Should trigger debug
3. Intermittent bug: "Sometimes works, sometimes doesn't" → Should trigger debug
4. General complaint: "This isn't working" → Should trigger error-troubleshooter
