# Bug Investigation Log Template

Use this template to document debugging sessions systematically. Copy and adapt as needed.

---

## Investigation Metadata

**Issue ID/Reference:** [e.g., #123, TICKET-456]
**Date Started:** [YYYY-MM-DD HH:MM]
**Investigator:** [Name or AI assistant]
**Priority:** [Critical / High / Medium / Low]
**Status:** [🔴 Investigating / 🟡 In Progress / 🟢 Resolved]

---

## Step 1: Initial Observations

**User Report:**
```
[Paste user's bug report or description here]
```

**Reproduction Steps:**
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Expected Behavior:**
[What should happen]

**Actual Behavior:**
[What actually happens]

**Environment:**
- OS: [e.g., Ubuntu 22.04, Windows 11, macOS 14]
- Application Version: [e.g., v2.3.1]
- Runtime: [e.g., Node.js 18.16, Python 3.11]
- Browser: [if applicable]

**Evidence Collected:**

*Error Messages:*
```
[Paste error messages, stack traces]
```

*Logs:*
```
[Relevant log entries]
```

*Configuration:*
```
[Relevant config values, environment variables]
```

*Recent Changes:*
- [Commit hash / PR / change description]
- [git diff summary if relevant]

---

## Step 2: Fact Classification

**Confirmed Symptoms (Observable Facts):**
1. [Symptom 1]
2. [Symptom 2]
3. [Symptom 3]

**Scope Analysis:**

| Test | Result | Notes |
|------|--------|-------|
| Different environments (dev/staging/prod) | ✓/✗ | |
| Different platforms (Win/Mac/Linux) | ✓/✗ | |
| Different browsers | ✓/✗ | |
| Different input data | ✓/✗ | |
| Previous version | ✓/✗ | |

**Isolated Components:**
- ✅ Working correctly: [Component A, Component B]
- ❌ Suspected issues: [Component C, Component D]
- ❓ Uncertain: [Component E]

**What Changed Recently:**
- [Change 1 - date, description]
- [Change 2 - date, description]

---

## Step 3: Differential Diagnosis List

**Hypotheses (Ranked by Likelihood):**

### Hypothesis 1: [Name of hypothesis]
**Likelihood:** High / Medium / Low
**Category:** [Infrastructure / Application / Configuration / Code]
**Reasoning:** [Why this is suspected]

### Hypothesis 2: [Name of hypothesis]
**Likelihood:** High / Medium / Low
**Category:** [Infrastructure / Application / Configuration / Code]
**Reasoning:** [Why this is suspected]

### Hypothesis 3: [Name of hypothesis]
**Likelihood:** High / Medium / Low
**Category:** [Infrastructure / Application / Configuration / Code]
**Reasoning:** [Why this is suspected]

[Add more as needed]

---

## Step 4: Elimination and Deductive Reasoning

### Test 1: [Hypothesis being tested]
**Test Design:** [How to test this hypothesis]
**Expected Result if Hypothesis True:** [What you expect to see]
**Actual Result:** [What you observed]
**Conclusion:** ✅ Confirmed / ❌ Eliminated / ⚠️ Inconclusive
**Reasoning:**
```
If [condition], then [expected behavior]
We observed [actual behavior]
Therefore [conclusion]
```

### Test 2: [Hypothesis being tested]
**Test Design:** [How to test this hypothesis]
**Expected Result if Hypothesis True:** [What you expect to see]
**Actual Result:** [What you observed]
**Conclusion:** ✅ Confirmed / ❌ Eliminated / ⚠️ Inconclusive
**Reasoning:**
```
[Chain of reasoning]
```

[Continue for each test]

**Hypotheses Remaining:** [List hypotheses not yet eliminated]

---

## Step 5: Experimental Verification

**Checkpoint Created:** [git branch name, commit hash, or backup location]

### Experiment 1: [Description]
**Goal:** [What this experiment aims to prove/disprove]
**Method:**
```bash
# Commands or code used
```
**Results:**
```
[Output or findings]
```
**Conclusion:** [What this proves]

### Experiment 2: [Description]
**Goal:** [What this experiment aims to prove/disprove]
**Method:**
```bash
# Commands or code used
```
**Results:**
```
[Output or findings]
```
**Conclusion:** [What this proves]

**Research Conducted:**
- [ ] GitHub issues searched: [keywords used]
- [ ] Stack Overflow checked: [relevant Q&As]
- [ ] Documentation reviewed: [sections consulted]
- [ ] Release notes: [findings]

**Findings:**
[Summary of research findings]

**Root Cause Identified:** ✅ Yes / ❌ No

---

## Step 6: Root Cause and Fix

**Root Cause:**
[Precise description of what's causing the issue]

**Location:**
- File: [path/to/file.ext]
- Line(s): [line number(s)]
- Function/Method: [name]

**Why This Causes the Issue:**
[Explanation of the causal mechanism]

**Fix Approaches Considered:**

| Approach | Pros | Cons | Selected |
|----------|------|------|----------|
| [Approach 1] | [pros] | [cons] | ✅/❌ |
| [Approach 2] | [pros] | [cons] | ✅/❌ |
| [Approach 3] | [pros] | [cons] | ✅/❌ |

**Selected Fix:**
```diff
[Show code diff or configuration change]
```

**Rationale:** [Why this fix was chosen]

**Implementation Notes:**
[Any important details about the fix]

**Verification:**
- [ ] Original issue resolved
- [ ] No new issues introduced
- [ ] Test suite passes
- [ ] Edge cases tested

---

## Step 7: Prevention and Documentation

**Regression Test Added:**
```
[Test code or test case description]
```

**Documentation Updated:**
- [ ] CLAUDE.md updated
- [ ] Code comments added
- [ ] API documentation updated
- [ ] README updated (if needed)

**Prevention Measures Implemented:**
1. [Measure 1 - e.g., added validation]
2. [Measure 2 - e.g., improved error handling]
3. [Measure 3 - e.g., added monitoring]

**Lessons Learned:**
1. [Lesson 1]
2. [Lesson 2]
3. [Lesson 3]

**Knowledge Base Update:**
- Pattern: [If this represents a new pattern to document]
- Category: [What category of bug this was]
- Key Insight: [Main takeaway for future debugging]

---

## Timeline Summary

| Time | Activity | Result |
|------|----------|--------|
| [HH:MM] | Investigation started | |
| [HH:MM] | Initial observations completed | |
| [HH:MM] | Hypothesis list created | |
| [HH:MM] | Testing began | |
| [HH:MM] | Root cause identified | |
| [HH:MM] | Fix implemented | |
| [HH:MM] | Verification completed | |
| [HH:MM] | Issue resolved | |

**Total Time:** [Duration]

---

## Status Update for Stakeholders

**Summary for Non-Technical Audience:**
[1-2 sentence explanation of what went wrong and how it was fixed]

**Impact:**
- Users affected: [number or description]
- Duration: [how long the issue existed]
- Severity: [impact level]

**Resolution:**
[Brief description of the fix]

**Follow-up Actions:**
- [ ] [Action 1]
- [ ] [Action 2]

---

**Investigation Completed:** [YYYY-MM-DD HH:MM]
**Final Status:** 🟢 Resolved / 🔴 Unresolved / ⚠️ Workaround Applied
