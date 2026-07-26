# Power Function Calculator

## Course and deliverable

**SOEN 6011 — Summer 2026, Delivery 2**

This project implements the assigned function **F7: x raised to y** in Python.
It provides a Tkinter graphical interface and an independently importable
calculation layer.

## Supported real-valued domain

- A positive base supports finite integer-valued and non-integer exponents.
- A zero base supports only positive exponents. Zero to zero and zero to a
  negative exponent are rejected.
- A negative base supports only integer-valued exponents.
- Only finite, real-valued inputs and results are supported.
- NaN, infinity, unsupported domain combinations, overflow, and severe
  underflow are rejected with plain-language messages.

## From-scratch implementation

No built-in mathematical power, logarithm, or exponential operation is used to
evaluate x raised to y. The program uses `float()`, `int()`, `format()`, and
Python iteration facilities only for input conversion, output formatting, and
algorithm control.

The program uses hybrid power evaluation:

1. Integer-valued exponents use iterative exponentiation by squaring.
2. Non-integer exponents require a positive base and use the identity
   `x^y = exp(y × ln(x))`.
3. Both approximation series have a convergence tolerance and iteration limit.
4. Checked arithmetic rejects results outside the supported normal
   floating-point range.

### Exponentiation by squaring

Integer exponents are processed one binary digit at a time. Each loop halves
the remaining exponent, so the iteration count grows logarithmically with the
exponent magnitude. Negative integer exponents use the reciprocal of the
completed positive power.

### Custom natural logarithm approximation

For a positive base and non-integer exponent, the base is range-reduced near
one and evaluated with a convergent odd-term series. A stored `ln(2)` constant
restores the power-of-two scaling.

### Custom exponential approximation

The exponential argument is reduced to a small remainder, evaluated with an
iterative Taylor series, and rescaled using the integer exponentiation path.

## Tkinter GUI

The graphical interface provides base and exponent inputs, **Calculate**,
**Clear**, and **Exit** controls, plus separate result and status fields. The
Enter key also starts a calculation.

## Exception handling

Expected failures derive from `PowerCalculatorError`:

- `InvalidInputError` identifies invalid text, NaN, and infinity.
- `UnsupportedDomainError` identifies unsupported real-number combinations.
- `NumericRangeError` identifies overflow and severe underflow.
- `ConvergenceError` identifies an approximation that reaches its iteration
  limit.

The GUI catches these expected errors, displays corrective guidance, and stays
open so the user can correct the input. Unexpected programming errors are not
silently hidden.

## How to run the program

Use a standard Python 3 installation with Tkinter support. No IDE or external
package is required.

```text
cd D2
python power_calculator.py
```

Press Enter or select **Calculate** to evaluate. **Clear** resets the inputs,
result, and status. **Exit** closes the application.

## Representative manual test cases

| Base | Exponent | Expected behavior |
|---:|---:|---|
| 2 | 3 | 8 |
| 2 | -10 | 0.0009765625 |
| 4 | 0.5 | approximately 2 |
| 16 | 0.25 | approximately 2 |
| -2 | 3 | -8 |
| 0 | 3 | 0 |
| 0.25 | 0.5 | approximately 0.5 |
| 0 | 0 | undefined-domain message |
| -2 | 0.5 | real-valued-domain message |
| `abc` | 2 | numeric-base message |
| `nan` | 2 | finite-number message |
| 10 | 400 | overflow message |
| 10 | -400 | severe-underflow message |

## Known numerical limitations

The calculator targets representative cases within relative error `1e-9`, but
does not claim support for every possible floating-point input. Inputs are
parsed as binary floating-point numbers, so very long decimal values may
already be rounded. Subnormal results below the minimum supported normal
floating-point magnitude are intentionally rejected as insufficiently accurate.
Values near overflow or underflow boundaries can be rejected because an
intermediate step is outside the supported normal range. Approximation error
can grow for especially ill-conditioned or extreme calculations.

Extremely large floating-point inputs are limited by binary floating-point
precision: distinct mathematical integers or decimals can map to the same
stored `float` before evaluation begins.

## Repository structure

```text
D2/
├── power_calculator.py      # Calculation layer and Tkinter application
├── README.md                # Usage, domain, limitations, and test guidance
└── screenshots/             # Manual GUI verification evidence
```
