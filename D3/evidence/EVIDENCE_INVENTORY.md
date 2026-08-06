# D3 Evidence Inventory

| Evidence | Expected File | Status | Verified Content | Manual Action Needed |
|---|---|---|---|---|
| Flake8 | `D3/evidence/flake8/flake8_success.png` | Complete | Shows `flake8 power_calculator.py test_power_calculator.py` and the no-violations success message. | None |
| Pylint | `D3/evidence/pylint/pylint_10.png` | Complete | Shows `pylint --persistent=no power_calculator.py test_power_calculator.py` and `10.00/10`. | None |
| PyUnit regression evidence | `D3/evidence/unittest/unittest_regression_tests.png` | Complete | Shows the verbose test command and the passing large-finite-result regression test. The paired summary image shows the true-overflow regression test. | None |
| PyUnit final summary | `D3/evidence/unittest/unittest_34_passed.png` | Complete | Shows the true-overflow regression test, `Ran 34 tests`, and `OK`. | None |
| Debugger integer check | `D3/evidence/debugger/debugger_integer_check.png` | Complete | Shows `base = 2.0`, `exponent = -3.0`, `exponent_is_integer = True`, and `calculate_power()`. | None |
| Debugger negative exponent | `D3/evidence/debugger/debugger_negative_exponent.png` | Complete | Shows `base = 2.0`, `exponent = -3`, `factor = 2.0`, `remaining = -3`, and entry into the reciprocal branch. | None |
| Debugger final result | `D3/evidence/debugger/debugger_final_result.png` | Complete | Shows `result = 0.125`, `remaining = 0`, and the final return line. | None |
| GUI negative exponent | `D3/evidence/gui/gui_negative_exponent.png` | Complete | Shows version 1.1.0, base `2`, exponent `-3`, result `0.125`, and successful status. | None |
| GUI domain error | `D3/evidence/gui/gui_domain_error.png` | Complete | Shows version 1.1.0, base `-2`, exponent `0.5`, and the integer-exponent domain error. | None |
| GUI zero-to-zero | `D3/evidence/gui/gui_zero_zero_error.png` | Complete | Shows version 1.1.0, base `0`, exponent `0`, and the undefined `0^0` error. | None |
| GUI accessibility | `D3/evidence/gui/gui_accessibility.png` | Complete | Byte-identical copy of the verified domain-error image showing keyboard focus, visible labels, text feedback, and a one-screen layout. | None |
| UIDP SVG | `D3/evidence/uidp/uidp_mind_map.svg` | Complete | Valid SVG markup; center node, three main branches, and `Tab navigation` are present. The matching render shows no clipping or overlap. | None |
| UIDP PNG | `D3/evidence/uidp/uidp_mind_map.png` | Complete | Opens successfully at 1568x720; all branches and labels are visible with no clipping or overlap. | None |

## Inspection Notes

- All required D3 evidence files use the expected filenames.
- PyUnit intentionally uses two screenshots: one for the regression-test list and one for the final 34-test summary.
- `gui_accessibility.png` is an unedited, byte-identical copy of the verified domain-error GUI screenshot.
- No evidence file was deleted.
