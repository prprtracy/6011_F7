# Deliverable 3 Poster Content Notes

These notes define content and evidence placement for a later three-column
poster. They are not the final poster.

## Left Column

### Project Objective

Deliverable 3 improves the D2 Power Function Calculator through coding-style
compliance, automated analysis, debugging, semantic versioning, GUI design
principles, accessibility, and unit testing.

### D2 Feedback Addressed

| D2 Feedback | D3 Action |
|---|---|
| Numeric conversion occurred inside the numerical core | Conversion moved to `parse_numeric_input()` |
| Valid large result classified as overflow | Actual finite result is now verified |
| Repository evidence was too small | Enlarged cropped evidence will be used |
| Requirements content was too dense | Use concise requirement-to-evidence mapping |

### Architecture

```text
GUI
  ↓
Parsing
  ↓
Validation
  ↓
Numerical Core
  ↓
Result / Error Feedback
```

### Semantic Versioning

```text
D2: 1.0.0
D3: 1.1.0
```

The minor version increases because the interface remains compatible while D3
adds corrected range handling, tests, accessibility, and verified code-quality
work.

## Center Column

### Final GUI

Use these verified files:

- `gui_negative_exponent.png`
- `gui_domain_error.png`
- `gui_zero_zero_error.png`

Reserve a large, readable area for the main GUI screenshot. Annotate:

- visible Base, Exponent, Result, and Status labels;
- Calculate, Clear, and Exit controls;
- immediate result display;
- specific status feedback; and
- version number.

### UIDP Mind Map

Use `uidp_mind_map.svg`.

Reserve a readable area for the completed mind map connecting Consistency,
Visibility, Feedback, Error Prevention, Affordance, and Simplicity to actual
GUI features.

### Accessibility

Use `gui_accessibility.png`.

- Keyboard navigation
- Enter to calculate
- Escape to clear
- Readable labels
- Specific error messages
- No color-only error communication
- Simple one-screen workflow

## Right Column

### PEP 8 and Flake8

Verified result: **No PEP 8 violations**.

Use `flake8_success.png`.

### Static Analysis

Verified result: **Pylint 10.00/10**.

Use `pylint_10.png`.

### Debugger

Use the negative exponent path:

```text
2^-3 = 0.125
```

Reserve space for readable debugger evidence showing integer detection,
reciprocal handling, variables, and the final result.

Use:

- `debugger_integer_check.png`
- `debugger_negative_exponent.png`
- `debugger_final_result.png`

### Unit Testing

Verified result: **34 tests passed**.

Use both `unittest_regression_tests.png` and `unittest_34_passed.png`.

Summarize:

- valid integer and decimal cases;
- parsing and domain errors;
- non-finite values;
- overflow and underflow behavior; and
- D2 regression tests.

Highlight:

```text
test_large_finite_result_is_not_classified_as_overflow
test_true_overflow_raises_result_overflow_error
```

### Conclusion

The D3 implementation preserves the mathematical behavior of D2 while
improving maintainability, reliability, accessibility, and evidence-based
verification.
