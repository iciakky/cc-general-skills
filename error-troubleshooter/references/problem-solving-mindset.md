# Claude Assistant Guidelines

## Problem-Solving Mindset: Bold Hypotheses, Careful Verification

### Core Principles

When encountering technical problems or errors, follow this disciplined approach:

1. **大膽提出假說 (Bold Hypotheses)**
   - Generate multiple competing hypotheses to explain the problem
   - Don't be afraid to speculate about root causes
   - Cast a wide net - consider obvious and non-obvious possibilities

2. **小心求證 (Careful Verification)**
   - Rigorously verify each hypothesis with concrete evidence
   - Actively search for counter-evidence that disproves your hypotheses
   - Distinguish between official documentation, user reports, and speculation
   - Check for exact matches (e.g., model names, version numbers) - similar ≠ identical

3. **挑戰自己的推論 (Challenge Your Own Reasoning)**
   - Ask: "What would disprove this hypothesis?"
   - Look for successful counter-examples
   - Identify weak points in your evidence chain
   - Question assumptions and implicit leaps in logic

4. **承認不確定性 (Acknowledge Uncertainty)**
   - It's better to say "I don't know" than to pretend certainty
   - Present confidence levels for each hypothesis
   - Avoid premature conclusions when evidence is incomplete
   - Be explicit about what is proven vs. what is speculation

5. **設計實驗 (Design Experiments)**
   - Propose controlled experiments to distinguish between hypotheses
   - Order experiments by information gain and cost
   - Change one variable at a time
   - Collect diagnostic information before making changes

---

### Case Study: Gemini Live API Function Calling Investigation

**Context**: POC test script immediately closed connection with no error messages or responses.

#### ❌ Initial Mistakes

**Mistake 1: Over-interpreting vague language**
- Saw: "Native audio models have limited tool use support"
- Jumped to: "This is why our connection closed!"
- Problem: "Limited" ≠ "doesn't work" or "causes connection closure"

**Mistake 2: Conflating user reports with official statements**
- Found: GitHub Issues reporting function calling problems
- Concluded: "Native audio doesn't support function calling"
- Problem: User reports are bug reports, not design documentation. Issues were still OPEN/unresolved.

**Mistake 3: Assuming name similarity = identity**
- Issue mentioned: `gemini-2.5-flash-preview-native-audio-dialog`
- We used: `gemini-2.5-flash-native-audio-preview-09-2025`
- Assumed: Same model, same limitations
- Reality: Different releases (May vs September), latter has "improved function calling"

**Mistake 4: Not seeking counter-evidence**
- Never searched for: "Working examples of gemini-2.5-flash-native-audio-preview-09-2025 with function calling"
- Never checked: Official model capability table
- Result: Missed official documentation stating model DOES support function calling

**Mistake 5: Skipping other possible causes**
- Jumped to "function calling incompatibility"
- Ignored: API key issues, SDK version mismatches, config format errors, network issues, quota limits, etc.

#### ✅ Corrected Approach

**Step 1: Verify exact capabilities**
- Searched official docs specifically for our model name
- Found: Official table explicitly states function calling IS supported
- Conclusion: Hypothesis 3 was DISPROVEN by official source

**Step 2: Search for counter-examples**
- Looked for successful usage examples
- Result: Found claims of support but NO complete working examples
- Insight: Documentation says it works, but no proof in the wild

**Step 3: Acknowledge limitations of evidence**
- Admitted: Can't prove function calling is the issue
- Admitted: Can't prove model switch will fix it
- Admitted: Don't know root cause without more diagnostics

**Step 4: Propose experiments**
- Collect error messages (close code/reason)
- Test same model without tools (isolate variable)
- Test different model with tools (isolate variable)
- Replicate official examples exactly

---

### Checklist for Technical Investigations

Before presenting conclusions, verify:

- [ ] Have I checked official documentation for ALL components/versions involved?
- [ ] Are my evidence sources exact matches (names, versions, dates)?
- [ ] Have I actively searched for counter-evidence?
- [ ] Can I distinguish between "official statement" vs "user report" vs "my inference"?
- [ ] Have I listed what I DON'T know or can't prove?
- [ ] Have I proposed experiments to test competing hypotheses?
- [ ] Am I stating confidence levels appropriately?

---

## Application to Error Troubleshooting

Apply these principles when using the error-troubleshooter skill:

1. **Generate Multiple Theories**: Don't fixate on the first explanation
2. **Verify with Official Sources**: Distinguish documentation from user reports
3. **Check Exact Matches**: Version numbers, model names, and configurations must match exactly
4. **Search for Counter-Evidence**: Look for cases where the theory should fail but doesn't
5. **Design Targeted Experiments**: Isolate variables to test specific hypotheses

This disciplined approach prevents premature conclusions and leads to more reliable solutions.