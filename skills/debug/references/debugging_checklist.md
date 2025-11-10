# Debugging Checklist

This checklist provides detailed action items for each step of the debugging workflow.

## Step 1: Observe Without Preconception ✓

**Evidence Collection:**
- [ ] Review user's bug report or issue description
- [ ] Examine error messages and stack traces
- [ ] Check application logs (stderr, stdout, application-specific logs)
- [ ] Review monitoring dashboards (if available)
- [ ] Inspect recent code changes (`git diff`, `git log`)
- [ ] Document current environment (OS, versions, dependencies)
- [ ] Capture configuration files (config files, environment variables, CLI arguments)
- [ ] Screenshot or record the error if visual
- [ ] Note exact steps to reproduce

**Documentation:**
- [ ] Create investigation log file
- [ ] Record timestamp and initial observations
- [ ] List all data sources consulted

## Step 2: Classify and Isolate Facts ✓

**Symptom Analysis:**
- [ ] List all observable symptoms
- [ ] Distinguish symptoms from potential causes
- [ ] Identify what changed recently (code, config, dependencies, infrastructure)

**Scope Narrowing:**
- [ ] Test across different environments (dev, staging, production)
- [ ] Test across different platforms (Windows, Linux, macOS)
- [ ] Test across different browsers (if web application)
- [ ] Test with different input data
- [ ] Test with different configurations
- [ ] Identify minimal reproduction case
- [ ] Test with previous working version (regression testing)

**Component Isolation:**
- [ ] List all involved components/modules
- [ ] Mark components known to work correctly
- [ ] Highlight suspicious components
- [ ] Draw dependency diagram if complex

## Step 3: Build Differential Diagnosis List ✓

**Infrastructure Issues:**
- [ ] Network connectivity problems
- [ ] DNS resolution failures
- [ ] Load balancer misconfiguration
- [ ] Firewall/security group blocking
- [ ] Resource exhaustion (CPU, memory, disk)

**Application Issues:**
- [ ] Cache staleness or corruption
- [ ] Database connection pool exhaustion
- [ ] Database deadlocks or slow queries
- [ ] Third-party API failures or timeouts
- [ ] Memory leaks
- [ ] Race conditions or threading issues
- [ ] Incorrect error handling
- [ ] Invalid input validation

**Configuration Issues:**
- [ ] Environment variable mismatch
- [ ] Configuration file errors
- [ ] Version incompatibility
- [ ] Missing dependencies
- [ ] Permission problems

**Code Issues:**
- [ ] Logic errors in recent changes
- [ ] Null pointer/undefined errors
- [ ] Type mismatches
- [ ] Off-by-one errors
- [ ] Incorrect assumptions

## Step 4: Apply Elimination and Deductive Reasoning ✓

**Hypothesis Testing:**
- [ ] Rank hypotheses by likelihood
- [ ] Design test for most likely hypothesis
- [ ] Execute test and document result
- [ ] If hypothesis invalidated, mark as eliminated
- [ ] If hypothesis confirmed, design further verification
- [ ] Move to next hypothesis if needed

**Reasoning Documentation:**
- [ ] Document "If X, then Y" statements
- [ ] Record why each hypothesis was eliminated
- [ ] Note which tests ruled out which possibilities
- [ ] Maintain chain of reasoning for review

**Narrowing Down:**
- [ ] Eliminate external factors first (network, APIs)
- [ ] Then infrastructure (resources, configuration)
- [ ] Then application-level issues (cache, database)
- [ ] Finally code-level issues (logic, types)

## Step 5: Experimental Verification ✓

**Preparation:**
- [ ] Create git branch for experiments
- [ ] Backup current state (checkpoint)
- [ ] Document experiment plan

**Experimentation:**
- [ ] Add logging/instrumentation to suspected area
- [ ] Add debug breakpoints if using debugger
- [ ] Create controlled test case
- [ ] Run experiment and capture output
- [ ] Compare actual vs expected behavior

**Research:**
- [ ] Search GitHub issues for similar problems
- [ ] Check Stack Overflow for related questions
- [ ] Review official documentation for edge cases
- [ ] Check release notes for known issues
- [ ] Consult language/framework changelog

**Validation:**
- [ ] Can the issue be reproduced consistently?
- [ ] Does the evidence match the hypothesis?
- [ ] Are there alternative explanations?

## Step 6: Locate and Implement Fix ✓

**Root Cause Confirmation:**
- [ ] Identify exact file and line number
- [ ] Understand why the code fails
- [ ] Confirm this is root cause, not symptom

**Solution Design:**
- [ ] Consider multiple fix approaches
- [ ] Evaluate side effects of each approach
- [ ] Choose most elegant and maintainable solution
- [ ] Ensure fix doesn't introduce new issues

**Implementation:**
- [ ] Implement the fix
- [ ] Add comments explaining the fix
- [ ] Update related documentation
- [ ] Add test case to prevent regression

**Verification:**
- [ ] Test the fix resolves original issue
- [ ] Run existing test suite
- [ ] Test edge cases
- [ ] Verify no new issues introduced

## Step 7: Prevention Mechanism ✓

**Stability Verification:**
- [ ] Run full test suite
- [ ] Perform integration testing
- [ ] Test in staging environment
- [ ] Monitor for unexpected behavior

**Documentation:**
- [ ] Update CLAUDE.md or project docs
- [ ] Document root cause
- [ ] Document fix and reasoning
- [ ] Add to knowledge base

**Prevention Measures:**
- [ ] Add automated test for this scenario
- [ ] Add validation/assertions to prevent recurrence
- [ ] Update error messages for clarity
- [ ] Add monitoring/alerting if applicable
- [ ] Share learnings with team

**Post-Mortem:**
- [ ] Review what went well
- [ ] Identify what could improve
- [ ] Update debugging procedures if needed
- [ ] Celebrate the fix! 🎉
