# D2 GUI Verification Evidence

The screenshot filenames are retained because presentation material may
reference them. Newer evidence uses lowercase, descriptive names. Each image
records its input, expected behavior, and evidence purpose below.

| Screenshot | Input `(x, y)` | Expected behavior | Evidence purpose |
|---|---|---|---|
| `negative_exponent_2_neg10.png` | `(2, -10)` | Displays `0.0009765625`. | Verifies the corrected base-inversion path for a negative exponent. |
| `negative_base_negative_exponent.png` | `(-2, -3)` | Displays `-0.125`. | Verifies a negative base with a negative integer exponent. |
| `non_integer_exponent_2_0_3.png` | `(2, 0.3)` | Displays approximately `1.23114441334492`. | Verifies the custom logarithm and exponential path. |
| `underflow_10_neg400.png` | `(10, -400)` | Reports that the result is too small. | Verifies severe-underflow classification after base inversion. |
| `overflow_10_400.png` | `(10, 400)` | Reports that the result is too large. | Verifies positive-exponent overflow classification. |
| `valid_non_integer_exponent.png` | `(4, 0.5)` | Displays `2` and a successful status. | Verifies a representative non-integer exponent. |
| `valid_negative_integer_exponent.png` | `(2, -10)` | Displays `0.0009765625` and a successful status. | Preserves the original negative-exponent evidence. |
| `valid_negative_base_integer_exponent.png` | `(-2, 3)` | Displays `-8` and a successful status. | Verifies a negative base with an integer exponent. |
| `valid_zero_base_positive_exponent.png` | `(0, 3)` | Displays `0` and a successful status. | Verifies the supported zero-base case. |
| `invalid_zero_to_zero.png` | `(0, 0)` | Leaves the result empty and explains that `0^0` is undefined. | Verifies domain validation and recovery guidance. |
| `invalid_negative_base_non_integer_exponent.png` | `(-2, 0.5)` | Requires an integer exponent for a negative base. | Verifies enforcement of the real-valued domain. |
| `invalid_non_numeric_base.png` | `(abc, 2)` | Requests a numeric base. | Verifies field-specific input validation. |
| `invalid_nan_input.png` | `(nan, 2)` | Requests a finite number. | Verifies rejection of NaN input. |
| `invalid_overflow_result.png` | `(1e308, 2)` | Reports that the result is too large. | Preserves the original overflow evidence. |
| `invalid_underflow_result.png` | `(1e-308, 2)` | Reports that the result is too small. | Preserves the original severe-underflow evidence. |
| `github_repository_overview.png` | Not applicable | Shows the public repository and D1/D2 organization. | Verifies repository visibility and deliverable separation. |

No existing screenshot was renamed because the presentation embeds or may
reference the current filenames.
