# D2 Technical Implementation

## Architecture

The program separates numerical evaluation from its Tkinter interface:

- `PowerCalculatorApp` owns the input widgets, actions, result display, and
  status feedback.
- `parse_number()` converts one text field to a finite `float` and reports
  field-specific invalid input.
- `calculate_power()` validates the real-valued domain and selects the integer
  or non-integer evaluation path.
- `power_by_squaring()` evaluates integer exponents using checked
  multiplication.
- `natural_log()` approximates `ln(x)` for a positive finite value.
- `exponential()` approximates `exp(x)` and restores its power-of-two scale.
- `_checked_multiply()` rejects multiplication that would overflow or produce
  a magnitude below the supported normal range.

## Integer exponent path

`calculate_power()` recognizes an integer-valued exponent from its stored
finite float and passes it to `power_by_squaring()` as an integer. An exponent
of zero returns `1.0`; a positive exponent is evaluated directly; and a
negative exponent is evaluated at its positive magnitude before taking the
reciprocal.

Exponentiation by squaring examines the exponent in binary. It multiplies the
result when the current value is odd, squares the factor, and halves the
remaining exponent. The number of loop iterations is therefore logarithmic in
the exponent magnitude.

## Non-integer exponent path

Non-integer exponents use the identity:

```text
x^y = exp(y * ln(x))
```

This path accepts positive bases only because the calculator returns real
values. `natural_log()` scales the base into `[0.75, 1.5]`, evaluates an odd
atanh series, and restores the scale with the stored `LN_2` constant.
`exponential()` reduces its argument by a multiple of `LN_2`, evaluates the
small remainder with a Taylor series, and applies the corresponding power of
two through `power_by_squaring()`.

## Numerical safeguards

- `MAX_FLOAT` defines the largest accepted finite float magnitude.
- `MIN_NORMAL` defines the smallest supported normal positive magnitude;
  subnormal results are intentionally rejected.
- `SERIES_TOLERANCE` determines when successive approximation terms are small
  enough to stop.
- `MAX_SERIES_ITERATIONS` bounds both series and prevents an endless loop.
- `MAX_RANGE_REDUCTIONS` independently bounds logarithm range reduction.
- `_checked_multiply()` checks for overflow before multiplication and for
  severe underflow afterward.
- `exponential()` rejects power-of-two scales outside the supported normal
  exponent range.
- Failed range reduction or series convergence raises `ConvergenceError`.

These checks favor an explicit error over returning a result that the
implementation considers insufficiently accurate.

## Exception hierarchy

All expected user-facing failures derive from `PowerCalculatorError`:

- `InvalidInputError` — missing, non-numeric, NaN, or infinite input.
- `UnsupportedDomainError` — a combination outside the supported real domain,
  such as `0^0` or a negative base with a non-integer exponent.
- `NumericRangeError` — overflow or severe underflow.
- `ConvergenceError` — range reduction or a series exceeds its iteration
  limit.

## GUI behavior

**Calculate** parses both fields, evaluates the result, and updates the result
and status fields. The Enter key invokes the same action. **Clear** empties both
inputs and the result, restores the initial status, and returns focus to the
base field. **Exit** closes the window.

Expected calculator exceptions are caught at the GUI boundary and shown in the
status field. The window remains usable after invalid input so the user can
correct either value and calculate again.

## Known limitations

- Only real-valued results are supported.
- Negative bases require integer-valued exponents.
- Results below `MIN_NORMAL`, including subnormal outputs, are rejected.
- Approximation accuracy depends on binary floating-point arithmetic and can
  degrade for extreme or ill-conditioned inputs.
