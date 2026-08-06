# Poster Readiness

## Ready Evidence

- `flake8_success.png`
- `pylint_10.png`
- `unittest_regression_tests.png`
- `unittest_34_passed.png`
- `debugger_integer_check.png`
- `debugger_negative_exponent.png`
- `debugger_final_result.png`
- `gui_negative_exponent.png`
- `gui_domain_error.png`
- `gui_zero_zero_error.png`
- `gui_accessibility.png`
- `uidp_mind_map.svg`
- `uidp_mind_map.png`

## Tool Evidence

- Flake8: no PEP 8 violations.
- Pylint: 10.00/10.
- PyUnit: 34 tests passed.

## D2 Regression Evidence

The two PyUnit screenshots verify that:

- a valid large finite result is accepted; and
- true overflow is rejected.

## Debugger Evidence

The negative-exponent path is shown in three steps:

1. The integer exponent is recognized.
2. The negative exponent enters the reciprocal branch.
3. The final result is `0.125`.

## GUI Evidence

- Valid negative exponent: `2^-3 = 0.125`.
- Invalid negative-base decimal exponent: base `-2` with exponent `0.5` produces a domain error.
- Boundary error: `0^0` is reported as undefined.
- Accessibility: keyboard focus, visible labels, text feedback, and the one-screen layout are visible.

## UIDP Evidence

Use `uidp_mind_map.svg` as the preferred poster asset. Use
`uidp_mind_map.png` only as a fallback.

## Readability Notes

- Enlarge debugger screenshots enough to read both Variables and source code.
- Use both PyUnit screenshots: one shows the regression tests and the other shows the final 34-test summary.
- The UIDP mind map is wide and should receive a large, preferably full-width, poster section.
- The Pylint screenshot is short and wide; size it so the wrapped command and final score remain readable.
- GUI screenshots are clean application-window captures and do not need cropping.

## Still Missing

- Final poster source.
- Final poster PDF.
- Final in-person review.
