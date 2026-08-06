# Power Function Calculator — Deliverable 3

## Version

1.1.0

## Deliverable 3 Scope

Deliverable 3 extends the tested D2 implementation with PEP 8 conformance,
Flake8 verification, debugger usage, Pylint static analysis, Semantic
Versioning, a UIDP-based GUI review, keyboard accessibility improvements, and
a comprehensive PyUnit test suite. The custom numerical algorithms and
supported mathematical domain remain intact.

## Supported Domain

- Positive bases support integer and decimal exponents.
- Negative bases support integer exponents only.
- Negative exponents return reciprocals.
- Zero with a positive exponent returns zero.
- `0^0` is rejected.
- Zero with a negative exponent is rejected.
- Complex results are unsupported.
- Direct expressions such as `sqrt(2)` are not parsed.
- Subnormal results below `MIN_NORMAL` are intentionally rejected by the
  documented underflow policy.

## D2 Feedback Addressed

- Numeric conversion was moved outside the numerical core into
  `parse_numeric_input()`.
- `power_by_squaring()` no longer calls `float()`.
- Valid near-maximum finite results are no longer misclassified as overflow.
- Genuine overflow is still detected.
- Regression tests cover valid large results and genuine overflow.
- Repository and poster evidence will use enlarged, readable crops.

## Running the Application

From the `D3` directory:

```text
python power_calculator.py
```

Python must include a working Tkinter/Tcl installation.

## Running Unit Tests

```text
python -m unittest test_power_calculator.py -v
```

## Code Quality Commands

```text
flake8 power_calculator.py test_power_calculator.py
pylint --persistent=no power_calculator.py test_power_calculator.py
```

## Verified Results

- 34 PyUnit tests passed.
- Flake8 reported no PEP 8 violations.
- Pylint rated the code 10.00/10.

## Evidence Folder

The `evidence` directory contains destinations for manually captured, genuine
evidence:

- `evidence/flake8` — terminal evidence of the clean Flake8 run.
- `evidence/pylint` — terminal evidence of the Pylint score.
- `evidence/unittest` — verbose PyUnit output and final test count.
- `evidence/debugger` — VS Code variable and call-stack views.
- `evidence/gui` — real application behavior and accessibility views.
- `evidence/uidp` — the completed UIDP mind map.

No screenshot is included or claimed until it is captured manually. Detailed
capture instructions are in `evidence/EVIDENCE_GUIDE.md`.
