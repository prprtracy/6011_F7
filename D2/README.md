# Power Function Calculator

## SOEN 6011 — Summer 2026, Delivery 2

This project implements the assigned function **F7: x raised to y** in Python.
It provides a Tkinter graphical interface and an independently importable
calculation layer. The mathematical result is calculated without Python power,
logarithm, or exponential operations.

## Supported domain

- A positive base supports finite integer-valued and non-integer exponents.
- A zero base supports only positive exponents. Zero to zero and zero to a
  negative exponent are rejected.
- A negative base supports only integer-valued exponents.
- Only finite, real-valued inputs and results are supported.
- NaN, infinity, unsupported domain combinations, overflow, and severe
  underflow are rejected with plain-language messages.

## From-scratch algorithms

The program uses Hybrid Power Evaluation:

1. Integer-valued exponents use iterative exponentiation by squaring. Negative
   exponents are handled with a reciprocal. Its running time is logarithmic in
   the exponent magnitude.
2. Non-integer exponents require a positive base. The program combines a custom
   natural logarithm with a custom exponential approximation.
3. The logarithm repeatedly scales its input by two, then evaluates an odd-term
   atanh series. Terms are updated by multiplication.
4. The exponential reduces its argument using a predefined natural-log-of-two
   constant, evaluates a Taylor series iteratively, and scales by an integer
   power of two using exponentiation by squaring.

Both series use a convergence tolerance and an iteration limit. Arithmetic
checks detect results outside the supported normal floating-point range.

The production source intentionally does not use Python's power operator,
`pow`, the `math` module, logarithm or exponential library functions, `eval`,
NumPy, SciPy, Decimal, Fractions, SymPy, or other mathematical libraries.
Tkinter is the only imported GUI library.

## Exception handling

Expected failures derive from `PowerCalculatorError`:

- `InvalidInputError` identifies invalid text, NaN, and infinity.
- `UnsupportedDomainError` identifies unsupported real-number combinations.
- `NumericRangeError` identifies overflow and severe underflow.
- `ConvergenceError` identifies an approximation that reaches its iteration
  limit.

The GUI catches these expected errors, displays corrective guidance, and stays
open for another attempt. Unexpected programming errors are not silently hidden.

## Requirements and running

Use a standard Python 3 installation that includes Tkinter. No IDE or external
package is required.

```text
cd D2
python power_calculator.py
```

Press Enter or select **Calculate** to evaluate. **Clear** resets the inputs,
result, and status. **Exit** closes the application.

## Manual test examples

| Base | Exponent | Expected behavior |
|---:|---:|---|
| 2 | 3 | 8 |
| 2 | -3 | 0.125 |
| 4 | 0.5 | approximately 2 |
| 16 | 0.25 | approximately 2 |
| -2 | -3 | -0.125 |
| 0 | 3 | 0 |
| 0.25 | 0.5 | approximately 0.5 |
| 0 | 0 | undefined-domain message |
| -2 | 0.5 | real-valued-domain message |
| `abc` | 2 | numeric-base message |

## Numerical limitations

The calculator targets representative cases within relative error `1e-9`, but
does not claim support for every possible floating-point input. Inputs are first
parsed as binary floating-point numbers, so very long decimal values may already
be rounded. Values with magnitudes below the smallest normal floating-point
number are treated as severe underflow instead of returning subnormal results.
Values near overflow or underflow boundaries can be rejected because an
intermediate step is outside the supported normal range. Approximation error can
grow for especially ill-conditioned or extreme calculations.
