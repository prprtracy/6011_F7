# D2 GUI Verification Evidence

These screenshots record representative successful calculations and handled
errors in the Tkinter interface. Each image shows the entered values, the
result or status message, and that the application remains available after the
action.

| Screenshot | Input `(x, y)` | Expected behavior | Evidence purpose |
|---|---|---|---|
| `valid_non_integer_exponent.png` | `(4, 0.5)` | Displays `2` and a successful status. | Verifies the custom logarithm/exponential path for a positive base. |
| `valid_negative_integer_exponent.png` | `(2, -10)` | Displays `0.0009765625` and a successful status. | Verifies reciprocal handling for a negative integer exponent. |
| `valid_negative_base_integer_exponent.png` | `(-2, 3)` | Displays `-8` and a successful status. | Verifies that negative bases are accepted for integer exponents. |
| `valid_zero_base_positive_exponent.png` | `(0, 3)` | Displays `0` and a successful status. | Verifies the supported zero-base case. |
| `invalid_zero_to_zero.png` | `(0, 0)` | Leaves the result empty and explains that `0^0` is undefined. | Verifies domain validation and corrective status feedback. |
| `invalid_negative_base_non_integer_exponent.png` | `(-2, 0.5)` | Leaves the result empty and requires an integer exponent for a negative base. | Verifies enforcement of the real-valued domain. |
| `invalid_non_numeric_base.png` | `(abc, 2)` | Leaves the result empty and requests a numeric base. | Verifies field-specific text validation and recovery. |
| `invalid_nan_input.png` | `(nan, 2)` | Leaves the result empty and requests a finite number. | Verifies rejection of NaN input. |
| `invalid_overflow_result.png` | `(1e308, 2)` | Leaves the result empty and reports that the result is too large. | Verifies overflow detection and user-facing handling. |
| `invalid_underflow_result.png` | `(1e-308, 2)` | Leaves the result empty and reports insufficient accuracy for the tiny result. | Verifies rejection of severe underflow/subnormal output. |

The filenames are kept stable so they can be referenced from other delivery
materials, including presentation slides.
