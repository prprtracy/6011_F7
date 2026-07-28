# Power Function Calculator

## Course and deliverable

**SOEN 6011 - Software Engineering Processes, Delivery 2**

This project implements the assigned function **F7: x raised to y** in Python.
It provides a Tkinter graphical interface and an independently importable
calculation layer.

## Supported real-valued domain

- For `x > 0`, finite integer-valued and non-integer exponents are supported.
- For `x = 0`, only `y > 0` is supported. `0^0` and zero raised to a negative
  exponent are rejected.
- For `x < 0`, only integer-valued exponents are supported.
- Results are real-valued and must remain within the supported normal
  floating-point range.
- Non-numeric input, NaN, infinity, unsupported domain combinations,
  overflow, severe underflow, and convergence failure are rejected with
  specific messages.

## From-scratch numerical implementation

The numerical calculation layer uses custom arithmetic algorithms and does
not rely on prohibited built-in or library functions for power evaluation,
logarithm, exponential evaluation, finite-value checking, integer detection,
or numerical iteration.

This restriction applies to the numerical core. Input conversion, string
handling, output formatting, exception handling, and Tkinter GUI operations
remain permitted because they support interaction rather than replace the
required numerical algorithms.

### Integer exponent path

Integer-valued exponents use exponentiation by squaring. The algorithm examines
the exponent in binary, multiplies the result when the remaining exponent is
odd, squares the factor, and halves the remaining exponent. Its iteration count
is `O(log |y|)`.

For a negative integer exponent, the algorithm inverts the base before the
loop and then processes `|y|`. It does not compute a positive power and apply a
final reciprocal. Inverting first prevents an intermediate overflow such as
`10^400` from masking the correct severe-underflow classification for
`10^-400`.

### Non-integer exponent path

For a positive base and non-integer exponent, the calculator uses:

```text
x^y = exp(y * ln(x))
```

`natural_log()` reduces the input by powers of two into a range near one and
evaluates an odd atanh series. `exponential()` reduces its argument by a
multiple of `ln(2)`, evaluates a Taylor series, and restores the power-of-two
scale through the custom integer-power path.

Both functions use explicit `while` loops, a convergence tolerance, and a
maximum iteration count.

### Custom numerical checks

- `is_finite_number()` detects NaN and infinity by comparison with
  `MAX_FLOAT`; it does not call `math.isfinite()`.
- `is_integer_value()` uses arithmetic remainder to detect integer-valued
  finite floats; it does not call `int()`.
- `nearest_integer_without_builtin()` determines the exponential scale through
  arithmetic and explicit iteration.
- `_checked_multiply()` checks both result multiplication and factor squaring
  for overflow and severe underflow.

## Exception handling

Expected failures derive from `PowerCalculatorError`:

- `InvalidInputError` - invalid text, NaN, or infinity.
- `UnsupportedDomainError` - an unsupported real-valued combination.
- `NumericRangeError` - overflow or severe underflow.
- `ConvergenceError` - an approximation exceeds its iteration limit.

The GUI catches these specific expected exceptions, clears the result, displays
plain-language guidance, and remains open. Unexpected programming errors are
not silently hidden.

## Tkinter GUI

The interface contains labelled base and exponent fields, **Calculate**,
**Clear**, and **Exit** buttons, and separate result and status areas. The Enter
key performs the same action as **Calculate**. **Clear** resets all fields and
returns focus to the base input.

## Run the application

Use Python 3 with Tkinter support. The program requires no third-party package,
specific IDE, or IDE configuration.

```text
cd D2
python power_calculator.py
```

The `if __name__ == "__main__":` guard allows the calculation layer to be
imported without launching the GUI.

## Run independent verification

From the `D2` directory:

```text
python verify_power_calculator.py
```

The script reports each case as `PASS` or `FAIL` and exits with a nonzero status
if any check fails.

## Representative verification cases

| Base `x` | Exponent `y` | Expected behavior |
|---:|---:|---|
| 2 | -10 | `0.0009765625` |
| -2 | -3 | `-0.125` |
| 2 | 0.3 | approximately `1.23114441334492` |
| 4 | 0.5 | approximately `2` |
| 0 | 3 | `0` |
| 0 | 0 | undefined-domain message |
| -2 | 0.5 | integer-exponent-required message |
| `abc` | 2 | numeric-base message |
| `nan` | 2 | finite-number message |
| 10 | -400 | severe underflow / result-too-small message |
| 10 | 400 | overflow / result-too-large message |

## Known numerical limitations

Inputs are stored as binary floating-point values, so decimal conversion and
rounding apply before evaluation. Extremely large values have limited integer
and decimal precision. Subnormal results below `MIN_NORMAL` are intentionally
rejected as insufficiently accurate. Approximation error can grow near numeric
boundaries or for ill-conditioned inputs, and the calculator does not support
complex-valued results.

## D2 structure

```text
D2/
|-- power_calculator.py          # Numerical layer and Tkinter application
|-- verify_power_calculator.py   # Independent non-GUI verification
|-- README.md                    # Usage, behavior, and limitations
|-- IMPLEMENTATION.md            # Technical design documentation
|-- screenshots/                 # GUI and repository evidence
|-- ChatGPT.md                   # GAI evidence
|-- Claude.md                    # GAI evidence
|-- D2_CASTROFF_Prompt.md        # CASTROFF-based prompt evidence
`-- SOEN6011_F7_Power_Function.pdf
                                 # Delivery 2 presentation
```
