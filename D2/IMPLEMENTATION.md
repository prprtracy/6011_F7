# D2 Technical Implementation

## Architecture

The numerical layer is independent of the Tkinter interface:

- `PowerCalculatorApp` owns the widgets, actions, result display, and status
  feedback.
- `parse_number()` converts GUI text to a finite `float`.
- `calculate_power()` validates the real-valued domain and selects an
  evaluation path.
- `power_by_squaring()` handles integer-valued exponents.
- `natural_log()` and `exponential()` handle positive-base non-integer powers.
- `nearest_integer_without_builtin()` calculates the exponential scale.
- `_checked_multiply()` protects multiplication from overflow and severe
  underflow.

The module-level `if __name__ == "__main__":` guard launches the GUI only when
the file is executed directly. Importing `calculate_power()` does not create a
window.

## Integer exponent path

`calculate_power()` uses `is_integer_value()` to identify integer-valued finite
floats without converting them with `int()`. It passes the arithmetic exponent
directly to `power_by_squaring()`.

For a negative exponent, `power_by_squaring()` first replaces `factor` with
`1.0 / factor` and changes the remaining exponent to `|y|`. The loop then
performs exponentiation by squaring. No final reciprocal is applied.

This order is numerically important. `10^-400` is evaluated from the reciprocal
base and is classified as severe underflow. Computing `10^400` first would
overflow before the implementation could identify the intended tiny result.
Conversely, `10^400` is correctly classified as overflow.

Within the loop, `_checked_multiply()` is used for both:

1. multiplying the accumulated result by an odd factor; and
2. squaring the factor for the next binary digit.

The remaining exponent is halved each iteration, producing `O(log |y|)` loop
iterations.

## Non-integer exponent path

For `x > 0` and non-integer `y`, the calculator uses:

```text
x^y = exp(y * ln(x))
```

`natural_log()` explicitly uses `while` loops to scale the input into
`[0.75, 1.5]` and evaluate an odd atanh series. Each term is derived from the
previous term by multiplication.

`exponential()` uses `nearest_integer_without_builtin()` to reduce its argument
to `k * ln(2) + r`. It explicitly uses a `while` loop to evaluate the Taylor
series for `exp(r)`, then restores the scale with `power_by_squaring(2.0, k)`.

The numerical calculation layer does not use `range()` or `int()`.
`nearest_integer_without_builtin()` rounds a finite value to the nearest
integer by adjusting the value by one half and repeatedly adding or subtracting
one. For the exponential inputs accepted by the calculator, the resulting
scale is bounded by the supported floating-point exponent range.

## Numerical safeguards

- `MAX_FLOAT` defines the largest accepted finite magnitude.
- `MIN_NORMAL` defines the smallest supported normal positive magnitude;
  subnormal results are rejected.
- `SERIES_TOLERANCE` controls series termination.
- `MAX_SERIES_ITERATIONS` bounds the logarithm and exponential series.
- `MAX_RANGE_REDUCTIONS` bounds logarithm range reduction.
- `is_finite_number()` performs custom NaN and infinity detection.
- `is_integer_value()` performs custom integer-valued detection with remainder.
- `_checked_multiply()` checks overflow before multiplication and severe
  underflow afterward.
- Failed range reduction or series convergence raises `ConvergenceError`.

## Exception hierarchy

All expected user-facing failures derive from `PowerCalculatorError`:

- `InvalidInputError` - non-numeric, NaN, or infinite input.
- `UnsupportedDomainError` - a combination outside the supported real domain.
- `NumericRangeError` - overflow or severe underflow.
- `ConvergenceError` - range reduction or a series reaches its limit.

`PowerCalculatorApp.calculate()` catches `PowerCalculatorError`, not a bare
exception. Expected failures are displayed in the status area and the GUI
remains usable. Unexpected programming errors are not caught and silently
discarded.

## GUI behavior

**Calculate** parses both fields, clears any previous result, evaluates the
expression, and updates the result or status. The Enter key invokes the same
action. **Clear** empties both inputs and the result, restores the initial
status, and focuses the base field. **Exit** closes the window normally.

## Known limitations

- Results are real-valued only.
- Negative bases require integer-valued exponents.
- Subnormal results below `MIN_NORMAL` are rejected.
- Binary floating-point conversion limits the precision of extreme inputs.
- Approximation accuracy depends on floating-point arithmetic and can degrade
  near numeric boundaries.
