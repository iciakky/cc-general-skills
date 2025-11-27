---
name: debug
description: Deep investigation tool for complex bugs using medical diagnosis methodology. Use when simple troubleshooting fails, for intermittent issues, race conditions, or when user says "I've tried everything". Applies 7-step process: observe facts, classify symptoms, differential diagnosis, deductive elimination, experimental verification, precise fix, prevention. For difficult bugs needing rigorous analysis.
---

# Debug

## Overview

This skill applies a systematic debugging methodology inspired by medical differential diagnosis. It provides a rigorous 7-step process for investigating and resolving bugs through observation, classification, hypothesis testing, and verification. This approach prioritizes evidence-based reasoning over assumptions, ensuring root causes are identified rather than symptoms treated.

## When to Use This Skill

Activate this skill in two primary scenarios:

**Scenario A: Post-Modification Anomalies**
When modifying a previously tested and working version, and any unexpected behavior emerges after the changes.

**Scenario B: User-Reported Issues**
When users report that test results don't meet expectations or the system fails to execute as intended.

## Debugging Workflow

Follow this 7-step systematic approach to diagnose and resolve issues.

For a detailed checklist of each step, refer to `{baseDir}/references/debugging_checklist.md`. For common bug patterns and their signatures, see `{baseDir}/references/common_patterns.md`.

### Step 1: Observe Without Preconception (Observe)

**Objective:** Collect all available evidence without jumping to conclusions.

**Process:**
- Gather all accessible clues: user reports, system logs, dashboards, error stack traces, version changes (git diff), configuration parameters (configs/args/env)
- Focus exclusively on facts and observable phenomena
- Avoid premature hypotheses or assumptions about causes
- Document all observations systematically

**Key Principle:** Observe, don't just see. At this stage, the goal is comprehensive data collection, not interpretation.

### Step 2: Classify and Isolate Facts (Classify & Isolate Facts)

**Objective:** Distinguish symptoms from root causes and narrow the problem scope.

**Process:**

**For Incremental Development (Scenario A - Post-Modification Anomalies):**
- Confirm the previous step still works (ensure issue is from new changes)
- List ALL changes since last working state (git diff, code modifications, config changes)
- Identify implicit assumptions in these changes, such as:
  - API calling conventions ("I assume this API works this way")
  - Parameter types/order ("I assume this parameter accepts X")
  - Configuration values ("I assume this env var is set")
  - Data formats ("I assume the response is JSON")
  - [And other fundamental assumptions embedded in the changes]
- **Apply Occam's Razor**: The simplest explanation is usually correct—prioritize basic assumption errors (typos, wrong parameters, incorrect API usage) over complex failure modes
- Verify fundamental assumptions with this priority:
  1. Check how it was implemented in the last working version (proven to work)
  2. Consult official documentation for correct usage (may be outdated)
  3. Only then consider external issues (community-reported bugs, known issues)

**General Isolation:**
- Separate "what is broken" (symptoms) from "why it's broken" (causes)
- Systematically narrow down the problem domain by testing:
  - Does it occur only in specific browsers?
  - Does it happen on specific operating systems?
  - Is it time-dependent?
  - Is it triggered by specific parameter values or input data?
- Eliminate all modules/components that function correctly
- Isolate the suspicious area

**Key Principle:** Reduce the search space by eliminating what works correctly.

### Step 3: Build Differential Diagnosis List (Differential Diagnosis List)

**Objective:** Enumerate all possible technical failure points.

**Process:**
- Create a comprehensive list of potential failure modes:
  - Cache errors
  - Database connection failures
  - Third-party API outages
  - Memory leaks
  - Configuration anomalies
  - Version compatibility issues
  - Race conditions
  - Resource exhaustion
- Include even rare or unlikely scenarios
- Draw on knowledge base and past experiences
- Consider both common and edge cases
- Consult `{baseDir}/references/common_patterns.md` for known bug patterns

**Key Principle:** Cast a wide net initially—don't prematurely exclude possibilities.

### Step 4: Apply Elimination and Deductive Reasoning (Deduce & Exclude)

**Objective:** Systematically eliminate impossible factors to find the truth.

**Process:**
- Follow Sherlock Holmes' principle: "When you eliminate the impossible, whatever remains, however improbable, must be the truth"
- Design precise tests to validate or invalidate each hypothesis
- Use Chain-of-Thought reasoning to document the deductive process
- Make reasoning transparent and verifiable
- Progressively eliminate factors until a single root cause remains

**Key Principle:** Evidence-based elimination leads to certainty.

### Step 5: Experimental Verification and Investigation (Experimental Verification)

**Objective:** Validate hypotheses through controlled experiments.

**Process:**
- Create restorable checkpoints before making changes
- Design and execute targeted experiments to test remaining hypotheses
- Research latest versions, known issues, and community discussions (GitHub issues, Stack Overflow)
- Conduct focused verification tests
- Use experimental evidence to prove each logical step
- Iterate until the exact cause is confirmed

**Key Principle:** Prove hypotheses with experiments, not assumptions.

### Step 6: Locate and Implement Fix (Locate & Implement Fix)

**Objective:** Apply the most elegant and least invasive solution.

**Process:**
- Pinpoint the exact code location or configuration causing the issue
- Design the fix with minimal side effects
- Prioritize elegant solutions over quick patches
- Consider long-term maintainability
- Implement the fix with precision

**Key Principle:** Seek elegant solutions, not temporary workarounds.

### Step 7: Prevention Mechanism (Prevent)

**Objective:** Ensure the same error doesn't recur and verify stability.

**Process:**
- Verify all related modules remain stable after the fix
- Run comprehensive regression tests
- Review the entire debugging process
- Generalize lessons learned
- Document findings in CLAUDE.md or project documentation
- Implement safeguards to prevent similar issues

**Key Principle:** Fix once, prevent forever.

## Best Practices

**Maintain Scientific Rigor:**
- Bold hypotheses, careful verification
- Evidence before assertions
- Transparency in reasoning

**Documentation:**
- Track all observations, hypotheses, and test results
- Make the investigation reproducible
- Document not just the fix, but the reasoning process
- Use `{baseDir}/references/investigation_template.md` to structure investigation logs
- Use `{baseDir}/assets/debug_report_template.md` for creating post-mortem reports

**Communication:**
- Explain findings clearly to users
- Provide context for why the issue occurred
- Describe preventive measures implemented

## Resources

This skill includes bundled resources to support the debugging workflow:

### references/
Load these into context as needed during investigation:
- `{baseDir}/references/debugging_checklist.md` - Comprehensive checklist for each debugging step
- `{baseDir}/references/common_patterns.md` - Common bug patterns and their signatures
- `{baseDir}/references/investigation_template.md` - Template for documenting investigations

### assets/
Use these templates for documentation and reporting:
- `{baseDir}/assets/debug_report_template.md` - Template for summarizing debugging sessions and creating post-mortem reports
