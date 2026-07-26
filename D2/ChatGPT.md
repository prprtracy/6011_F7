# SOEN 6011 Delivery 2 — Problems 5, 6, and 7

## F7: Power Function (x^y)

### GAI-Generated Design and Implementation Proposal

This response proposes an implementation plan for Delivery 2 based on the completed Delivery 1 design. It does not claim that the proposed code has been executed, committed, uploaded, or manually verified. All implementation results, screenshots, repository changes, and Git history must be confirmed by the student.

---

# 1. Existing D1 Design Inspected

## 1.1 Supported Domain Established in D1

Delivery 1 defined a real-valued power function with the following supported domain.

| Base (x)        | Exponent (y)                   | Expected behavior                                   |
| --------------- | ------------------------------ | --------------------------------------------------- |
| (x>0)           | Finite integer-valued exponent | Supported                                           |
| (x>0)           | Finite non-integer exponent    | Supported                                           |
| (x=0)           | (y>0)                          | Supported; result is 0                              |
| (x=0)           | (y=0)                          | Rejected because (0^0) is undefined                 |
| (x=0)           | (y<0)                          | Rejected because division by zero would be required |
| (x<0)           | Integer-valued exponent        | Supported                                           |
| (x<0)           | Non-integer exponent           | Rejected because the result may be complex          |
| Any base        | NaN or infinity                | Rejected                                            |
| Any combination | Complex-valued result          | Not supported                                       |

The project returns real-valued results only.

## 1.2 Selected Algorithm

Delivery 1 selected a Hybrid Power Evaluation algorithm.

The algorithm uses:

1. exponentiation by squaring for integer-valued exponents;
2. the identity

[
x^y=\exp(y\ln x)
]

for positive bases with non-integer exponents.

This design should be retained in Delivery 2 rather than replaced with a different algorithm.

## 1.3 Existing Input Validation

The D1 textual interface is assumed to perform the following validation:

* convert user input into numeric values;
* reject non-numeric input;
* reject NaN and infinity;
* detect whether the exponent is integer-valued;
* reject unsupported base-and-exponent combinations;
* provide an explanatory error message;
* allow the user to try again after an error.

## 1.4 Existing Error Handling

D1 already identifies several expected error categories:

* invalid text input;
* undefined (0^0);
* zero raised to a negative exponent;
* negative base with a non-integer exponent;
* floating-point overflow or underflow.

Delivery 2 should expand this design with a clearer exception hierarchy and graphical recovery behavior.

## 1.5 D1 Requirements Affected by D2

The following D1 areas require revision:

| D1 area                 | D2 change                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------ |
| User interface          | Replace the textual interface with Tkinter                                                 |
| Integer calculation     | Preserve exponentiation by squaring but remove built-in power evaluation                   |
| Non-integer calculation | Replace built-in logarithm and exponential functions with custom iterative implementations |
| Finite-value checking   | Use custom comparisons instead of `math.isfinite()`                                        |
| Integer detection       | Use custom integer-valued detection                                                        |
| Error handling          | Add specific custom exceptions                                                             |
| Numerical range         | Add explicit overflow and severe-underflow detection                                       |
| Approximation behavior  | Add tolerance, iteration limits, and convergence failure handling                          |
| Recovery                | Keep the GUI open after expected errors                                                    |
| Documentation           | Add README, implementation documentation, and updated requirements                         |
| Traceability            | Connect each revised requirement to code and verification evidence                         |

---

# 2. D2 Implementation Summary

The proposed D2 implementation extends the D1 hybrid algorithm.

The application should contain two clearly separated layers.

## Calculation Layer

The calculation layer should provide importable functions such as:

```python
calculate_power(base, exponent)
power_by_squaring(base, exponent)
natural_log(value)
exponential(value)
parse_number(text, field_name)
```

This layer should not depend on Tkinter and should be usable independently of an IDE or graphical window.

## Graphical Interface Layer

The GUI should be implemented with Tkinter and should provide:

* base input;
* exponent input;
* Calculate control;
* Clear control;
* Exit control;
* result display;
* status and error display;
* Enter-key calculation.

## Main Numerical Paths

The proposed implementation should use:

```text
Integer-valued exponent
    → power_by_squaring()

Positive base and non-integer exponent
    → natural_log(base)
    → exponent × logarithm
    → exponential(product)
```

The application should not use a built-in mathematical power, logarithm, or exponential operation to evaluate (x^y).

---

# 3. Files Created or Modified

The following repository structure is recommended:

```text
6011_F7/
├── D1/
│   └── existing D1 files
├── D2/
│   ├── power_calculator.py
│   ├── README.md
│   ├── IMPLEMENTATION.md
│   ├── REQUIREMENTS.md
│   └── screenshots/
│       ├── README.md
│       └── verification images
├── .gitignore
└── README.md
```

## Proposed File Responsibilities

| File                       | Responsibility                                                              |
| -------------------------- | --------------------------------------------------------------------------- |
| `D2/power_calculator.py`   | Numerical algorithms, exceptions, validation, and Tkinter GUI               |
| `D2/README.md`             | Project overview, execution instructions, domain, examples, and limitations |
| `D2/IMPLEMENTATION.md`     | Detailed explanation of architecture and numerical algorithms               |
| `D2/REQUIREMENTS.md`       | Revised D1 requirements and D2 traceability                                 |
| `D2/screenshots/README.md` | Screenshot names, inputs, expected outputs, and evidence purpose            |
| `.gitignore`               | Ignore Python cache, IDE, editor, and temporary files                       |
| Root `README.md`           | Explain the repository and link to D1 and D2                                |

Existing D1 files should not be deleted, renamed, overwritten, or unnecessarily modified.

---

# 4. From-Scratch Numerical Algorithms

## 4.1 Integer-Valued Exponents

Integer-valued exponents should be evaluated with exponentiation by squaring.

### Proposed Algorithm

```python
def power_by_squaring(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1.0

    if base == 0.0:
        if exponent < 0:
            raise UnsupportedDomainError(
                "Zero cannot be raised to a negative exponent."
            )
        return 0.0

    negative_exponent = exponent < 0
    remaining = -exponent if negative_exponent else exponent
    factor = base
    result = 1.0

    while remaining > 0:
        if remaining % 2 == 1:
            result = checked_multiply(result, factor)

        remaining //= 2

        if remaining > 0:
            factor = checked_multiply(factor, factor)

    if negative_exponent:
        return checked_reciprocal(result)

    return result
```

The function uses:

* multiplication;
* division;
* comparison;
* modulo;
* integer division;
* iteration.

It does not require `pow()`, `math.pow()`, or `**`.

### Complexity

Each loop iteration approximately halves the remaining exponent.

Therefore, the number of loop iterations is:

[
O(\log |y|)
]

This is more efficient than multiplying the base (y) times.

### Negative Exponents

For a negative integer exponent:

[
x^{-n}=\frac{1}{x^n}
]

The implementation must check whether the reciprocal becomes zero or enters the rejected subnormal range.

### Important Implementation Consideration

A direct approach that computes (x^n) before taking the reciprocal may produce an intermediate overflow even when the final negative-exponent result should be an underflow.

A stronger design is to invert the base first:

```python
if exponent < 0:
    factor = checked_reciprocal(base)
    remaining = -exponent
```

This approach more accurately identifies extremely small final results as severe underflow rather than intermediate overflow.

---

## 4.2 Custom Natural Logarithm

The proposed `natural_log()` function should accept only positive finite values.

### Range Reduction

The input should be represented as:

[
x=m2^k
]

where the mantissa (m) is reduced to a range close to 1, for example:

[
0.75 \leq m \leq 1.5
]

This can be performed using repeated multiplication or division by 2.

Then:

[
\ln(x)=\ln(m)+k\ln(2)
]

### Iterative Series

Define:

[
z=\frac{m-1}{m+1}
]

Then use:

[
\ln(m)
======

2
\left(
z+\frac{z^3}{3}+\frac{z^5}{5}+\frac{z^7}{7}+\cdots
\right)
]

The next power should be generated through multiplication:

```python
z_squared = z * z
term = z

while ...:
    addition = term / denominator
    total += addition
    term *= z_squared
    denominator += 2
```

This avoids built-in exponentiation.

### Proposed Structure

```python
def natural_log(value: float) -> float:
    if not is_finite_number(value) or value <= 0.0:
        raise UnsupportedDomainError(
            "The natural logarithm requires a positive finite value."
        )

    mantissa = value
    scale = 0
    reductions = 0

    while mantissa > 1.5:
        mantissa /= 2.0
        scale += 1
        reductions += 1
        check_reduction_limit(reductions)

    while mantissa < 0.75:
        mantissa *= 2.0
        scale -= 1
        reductions += 1
        check_reduction_limit(reductions)

    z = (mantissa - 1.0) / (mantissa + 1.0)
    z_squared = z * z
    term = z
    total = 0.0
    denominator = 1

    for _ in range(MAX_SERIES_ITERATIONS):
        addition = term / denominator
        total += addition

        if has_converged(addition, total):
            return 2.0 * total + scale * LN_2

        term *= z_squared
        denominator += 2

    raise ConvergenceError(
        "The calculation did not converge within the supported "
        "number of iterations."
    )
```

---

## 4.3 Custom Exponential

The proposed `exponential()` function should use range reduction.

Represent the input as:

[
v=k\ln(2)+r
]

Then:

[
e^v=2^k e^r
]

The value of (k) should be chosen so that (r) remains small.

### Taylor Series

Use:

[
e^r
===

1+r+\frac{r^2}{2!}+\frac{r^3}{3!}+\cdots
]

Each new term can be calculated from the previous term:

```python
term = term * remainder / index
```

### Proposed Structure

```python
def exponential(value: float) -> float:
    if not is_finite_number(value):
        raise NumericRangeError(
            "The result is outside the supported finite numeric range."
        )

    quotient = value / LN_2

    if quotient >= 0.0:
        scale = int(quotient + 0.5)
    else:
        scale = int(quotient - 0.5)

    remainder = value - scale * LN_2

    term = 1.0
    total = 1.0

    for index in range(1, MAX_SERIES_ITERATIONS + 1):
        term = term * remainder / index
        total += term

        if has_converged(term, total):
            check_scale_range(scale)
            scale_factor = power_by_squaring(2.0, scale)
            return checked_multiply(total, scale_factor)

    raise ConvergenceError(
        "The calculation did not converge within the supported "
        "number of iterations."
    )
```

---

## 4.4 Numerical Constants

The implementation may define explicit floating-point constants:

```python
LN_2 = 0.6931471805599453
MAX_FLOAT = 1.7976931348623157e308
MIN_NORMAL = 2.2250738585072014e-308
SERIES_TOLERANCE = 1e-16
MAX_SERIES_ITERATIONS = 1000
MAX_RANGE_REDUCTIONS = 2048
```

These constants support numerical control but do not perform power, logarithm, or exponential evaluation.

---

# 5. Tkinter GUI Design

The proposed GUI should use a class such as:

```python
class PowerCalculatorApp:
```

## 5.1 Interface Components

The window should contain:

* application title;
* short explanation;
* label and input field for base (x);
* label and input field for exponent (y);
* Calculate button;
* Clear button;
* Exit button;
* labelled result field;
* separate status field.

Example interface text:

```text
Power Function Calculator

Compute x raised to the power y

Base x:      [               ]
Exponent y:  [               ]

[Calculate] [Clear] [Exit]

Result:
Status:
```

## 5.2 Calculate Behavior

The Calculate action should:

1. clear the previous result;
2. parse the base;
3. parse the exponent;
4. validate the domain;
5. calculate the result;
6. display the formatted result;
7. display a success message.

Expected calculator exceptions should update the status area without closing the window.

```python
def calculate(self, _event=None):
    self.result_text.set("")

    try:
        base = parse_number(self.base_entry.get(), "base x")
        exponent = parse_number(
            self.exponent_entry.get(),
            "exponent y"
        )
        result = calculate_power(base, exponent)

    except PowerCalculatorError as error:
        self.status_text.set(f"Error: {error}")
        return

    self.result_text.set(format_result(result))
    self.status_text.set("Calculation completed successfully.")
```

## 5.3 Clear Behavior

The Clear action should:

* clear both inputs;
* clear the result;
* restore the default status;
* return focus to the base field.

## 5.4 Exit Behavior

The Exit action should close the application normally by calling:

```python
root.destroy
```

## 5.5 Enter-Key Calculation

The Enter key should invoke the same method as the Calculate button:

```python
root.bind("<Return>", self.calculate)
```

## 5.6 Independent Import

The calculation functions must remain importable without opening a GUI.

```python
def main():
    root = tk.Tk()
    PowerCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
```

---

# 6. Exception Hierarchy

The following hierarchy is recommended:

```python
class PowerCalculatorError(Exception):
    """Base class for expected calculator errors."""


class InvalidInputError(PowerCalculatorError):
    """Raised for missing, non-numeric, NaN, or infinite input."""


class UnsupportedDomainError(PowerCalculatorError):
    """Raised for unsupported real-valued combinations."""


class NumericRangeError(PowerCalculatorError):
    """Raised for overflow or severe underflow."""


class ConvergenceError(PowerCalculatorError):
    """Raised when an iterative approximation does not converge."""
```

## Exception Responsibilities

| Exception                | Responsibility                                    |
| ------------------------ | ------------------------------------------------- |
| `PowerCalculatorError`   | Parent class for expected user-facing errors      |
| `InvalidInputError`      | Non-numeric text, NaN, or infinity                |
| `UnsupportedDomainError` | Unsupported real-number domain                    |
| `NumericRangeError`      | Overflow or severe underflow                      |
| `ConvergenceError`       | Failure to converge within the allowed iterations |

The GUI should catch only `PowerCalculatorError`.

It should not use a bare `except:` clause.

Unexpected programming errors should not be silently hidden.

---

# 7. Supported-Domain Behavior

The central `calculate_power()` function should enforce the domain before selecting an algorithm.

```python
def calculate_power(base: float, exponent: float) -> float:
    if not is_finite_number(base):
        raise InvalidInputError(
            "NaN and infinity are not supported. "
            "Please enter a finite number for the base x."
        )

    if not is_finite_number(exponent):
        raise InvalidInputError(
            "NaN and infinity are not supported. "
            "Please enter a finite number for the exponent y."
        )

    exponent_is_integer = is_integer_value(exponent)

    if base == 0.0:
        if exponent == 0.0:
            raise UnsupportedDomainError(
                "The expression 0^0 is undefined. Please enter "
                "a positive exponent when the base is zero."
            )

        if exponent < 0.0:
            raise UnsupportedDomainError(
                "Zero cannot be raised to a negative exponent."
            )

        return 0.0

    if base < 0.0 and not exponent_is_integer:
        raise UnsupportedDomainError(
            "A negative base requires an integer exponent because "
            "this calculator returns real-valued results only."
        )

    if exponent == 0.0 or base == 1.0:
        return 1.0

    if exponent_is_integer:
        return power_by_squaring(base, int(exponent))

    logarithm = natural_log(base)
    product = checked_multiply(exponent, logarithm)
    return exponential(product)
```

## Behavior Table

| Condition                           | Required behavior                |
| ----------------------------------- | -------------------------------- |
| Positive base, integer exponent     | Exponentiation by squaring       |
| Positive base, non-integer exponent | Custom logarithm and exponential |
| Zero base, positive exponent        | Return 0                         |
| (0^0)                               | Reject                           |
| Zero base, negative exponent        | Reject                           |
| Negative base, integer exponent     | Exponentiation by squaring       |
| Negative base, non-integer exponent | Reject                           |
| Non-numeric text                    | Reject                           |
| NaN or infinity                     | Reject                           |
| Overflow                            | Reject                           |
| Severe underflow                    | Reject                           |
| Convergence failure                 | Reject                           |

---

# 8. Verification Results

No verification result should be reported as completed until the implementation has been executed.

The following cases are the required verification plan.

## 8.1 Valid Test Cases

| ID    | Base | Exponent |   Expected result | Status             |
| ----- | ---: | -------: | ----------------: | ------------------ |
| VT-01 |    2 |        3 |                 8 | Requires execution |
| VT-02 |    2 |      -10 |      0.0009765625 | Requires execution |
| VT-03 |    4 |      0.5 |   Approximately 2 | Requires execution |
| VT-04 |   16 |     0.25 |   Approximately 2 | Requires execution |
| VT-05 |   -2 |        3 |                -8 | Requires execution |
| VT-06 |   -2 |        4 |                16 | Requires execution |
| VT-07 |   -2 |       -3 |            -0.125 | Requires execution |
| VT-08 |    0 |        3 |                 0 | Requires execution |
| VT-09 |    5 |        0 |                 1 | Requires execution |
| VT-10 | 0.25 |      0.5 | Approximately 0.5 | Requires execution |

For approximate cases, the result should be compared using a defined tolerance such as:

[
\frac{|actual-expected|}
{\max(1,|expected|)}
\leq 10^{-9}
]

## 8.2 Invalid Test Cases

| ID    | Input                      | Expected behavior              | Status             |
| ----- | -------------------------- | ------------------------------ | ------------------ |
| IT-01 | (0^0)                      | Undefined-expression message   | Requires execution |
| IT-02 | (0^{-1})                   | Zero-negative-exponent message | Requires execution |
| IT-03 | ((-2)^{0.5})               | Negative-base domain message   | Requires execution |
| IT-04 | `abc` as base              | Numeric-base message           | Requires execution |
| IT-05 | `abc` as exponent          | Numeric-exponent message       | Requires execution |
| IT-06 | NaN                        | Finite-number message          | Requires execution |
| IT-07 | Positive infinity          | Finite-number message          | Requires execution |
| IT-08 | Negative infinity          | Finite-number message          | Requires execution |
| IT-09 | Overflow-producing input   | Result-too-large message       | Requires execution |
| IT-10 | Severe-underflow input     | Result-too-small message       | Requires execution |
| IT-11 | Forced convergence failure | Convergence message            | Requires execution |

## 8.3 GUI Recovery Verification

After each invalid case, manually confirm that:

* the GUI remains open;
* the result field is empty;
* the status area contains a helpful message;
* the input fields remain editable;
* a corrected input can be calculated successfully;
* no unexplained traceback appears in the GUI.

## 8.4 Screenshot Evidence

Recommended screenshot names include:

```text
valid_integer_positive.png
valid_integer_negative.png
valid_non_integer.png
valid_negative_base.png
valid_zero_base.png
invalid_zero_to_zero.png
invalid_zero_negative_exponent.png
invalid_negative_base_decimal.png
invalid_base_text.png
invalid_exponent_text.png
invalid_nan.png
invalid_infinity.png
invalid_overflow.png
invalid_underflow.png
recovery_after_error.png
```

These screenshots must not be claimed as completed until they are actually captured.

---

# 9. Prohibited-Operation Check

The final production calculation code must be checked for the following prohibited operations:

```text
pow(
math.pow
**
math.log
math.exp
math.isfinite
numpy
scipy
decimal
fractions
sympy
cmath
eval(
```

A source-code search should be performed before submission.

## Required Statement

The documentation should use the following precise statement:

> No built-in mathematical power, logarithm, or exponential operation is used to evaluate x raised to y.

The documentation should not claim that the application uses no Python built-in functions at all.

The application may legitimately use:

* `float()`;
* `int()`;
* `format()`;
* `range()`;
* comparisons;
* arithmetic;
* loops;
* exceptions;
* Tkinter.

## Verification Status

| Check                                                  | Status                     |
| ------------------------------------------------------ | -------------------------- |
| Production code contains no `pow()`                    | Requires source inspection |
| Production code contains no `**`                       | Requires source inspection |
| Production code contains no built-in log               | Requires source inspection |
| Production code contains no built-in exponential       | Requires source inspection |
| Production code contains no external numerical library | Requires source inspection |
| Production code contains no `eval()`                   | Requires source inspection |

---

# 10. GitHub Repository Organization

The public repository is:

```text
https://github.com/prprtracy/6011_F7.git
```

The repository should preserve D1 and create a separate D2 directory.

Recommended structure:

```text
6011_F7/
├── D1/
│   ├── D1 source files
│   ├── D1 presentation files
│   └── D1 documentation
├── D2/
│   ├── power_calculator.py
│   ├── README.md
│   ├── IMPLEMENTATION.md
│   ├── REQUIREMENTS.md
│   └── screenshots/
│       ├── README.md
│       └── *.png
├── .gitignore
└── README.md
```

## Repository Rules

The following actions should be avoided:

* deleting D1;
* overwriting D1 with D2;
* rewriting Git history;
* amending old commits;
* squashing existing commits;
* rebasing published history;
* force-pushing;
* committing generated cache files;
* creating fake commits only to increase the commit count.

---

# 11. Commit Messages Created or Recommended

Because the repository has not been modified as part of this GAI response, the following messages are recommendations rather than completed commits.

## Recommended Commit Sequence

```text
Add D2 power calculation architecture

Implement integer exponentiation by squaring

Implement custom natural logarithm approximation

Implement custom exponential approximation

Add numeric range and convergence exceptions

Add Tkinter power calculator interface

Document D2 execution and supported domain

Document D2 architecture and numerical limitations

Add updated D2 software requirements

Document GUI verification evidence

Add Python and editor files to gitignore
```

Each commit should correspond to a real, inspectable change.

Avoid messages such as:

```text
update
fix
changes
final
D2
D2 update
```

A high-quality commit message should:

* use the imperative form;
* describe the actual change;
* remain concise;
* avoid vague wording;
* not claim work that the commit does not contain.

---

# 12. README Summary

The proposed `D2/README.md` should contain the following sections.

## Project Title

```text
Power Function Calculator
```

## Course and Deliverable

```text
SOEN 6011 — Software Engineering Processes
Delivery 2
Assigned function: F7, x raised to y
```

## Required Topics

The README should document:

* supported real-valued domain;
* from-scratch calculation requirement;
* exponentiation by squaring;
* custom natural logarithm;
* custom exponential;
* Tkinter GUI behavior;
* exception hierarchy;
* execution instructions;
* representative valid and invalid cases;
* numerical limitations;
* repository structure.

## Execution Instructions

```text
cd D2
python power_calculator.py
```

The README should state:

```text
Python 3 with Tkinter support is required.
No external numerical package is required.
```

## Required Numerical Limitations

The README should state honestly that:

* only real-valued results are supported;
* negative bases require integer-valued exponents;
* subnormal results below the minimum supported normal magnitude are rejected;
* extremely large floating-point values are limited by binary floating-point precision;
* some extreme inputs may be rejected because an intermediate value exceeds the supported range;
* approximation accuracy depends on convergence and binary floating-point behavior;
* the implementation does not claim support for every possible floating-point input.

---

# 13. Complete Updated Requirements

The following requirements revise the D1 requirements for Delivery 2.

## 13.1 Functional Requirements

| ID     | Requirement statement                                                                                                           | Source or rationale                            | Verification method                                 | D1 status |
| ------ | ------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------- | --------- |
| FR-001 | The system shall calculate (x^y) for every supported finite real-valued input combination.                                      | Assigned function F7                           | Execute representative valid cases                  | Modified  |
| FR-002 | The system shall evaluate integer-valued exponents using exponentiation by squaring.                                            | Selected D1 algorithm                          | Code inspection and integer test cases              | Retained  |
| FR-003 | The system shall support positive, zero, and negative integer-valued exponents.                                                 | Supported D1 domain                            | Execute positive, zero, and negative exponent cases | Modified  |
| FR-004 | The system shall evaluate a positive base with a non-integer exponent using a custom natural-logarithm and exponential process. | Selected D1 hybrid algorithm and D2 constraint | Code inspection and non-integer cases               | Modified  |
| FR-005 | The system shall calculate the natural logarithm using range reduction and an iterative series.                                 | D2 from-scratch constraint                     | Code inspection                                     | New       |
| FR-006 | The system shall calculate the exponential using range reduction and an iterative Taylor series.                                | D2 from-scratch constraint                     | Code inspection                                     | New       |
| FR-007 | The system shall accept a negative base only when the exponent is integer-valued.                                               | Real-valued domain                             | Negative-base valid and invalid cases               | Retained  |
| FR-008 | The system shall return zero when the base is zero and the exponent is positive.                                                | Mathematical domain                            | Execute (0^3)                                       | Retained  |
| FR-009 | The system shall return one when a nonzero base is raised to the exponent zero.                                                 | Mathematical definition                        | Execute (5^0) and ((-2)^0)                          | Retained  |
| FR-010 | The system shall identify whether a finite exponent is integer-valued before selecting the numerical algorithm.                 | Hybrid algorithm selection                     | Code inspection and decimal/integer cases           | Modified  |

## 13.2 Input Requirements

| ID     | Requirement statement                                                                                  | Source or rationale                | Verification method       | D1 status |
| ------ | ------------------------------------------------------------------------------------------------------ | ---------------------------------- | ------------------------- | --------- |
| IR-001 | The system shall provide a labelled input field for base (x).                                          | Persona clarity and GUI constraint | GUI inspection            | Modified  |
| IR-002 | The system shall provide a labelled input field for exponent (y).                                      | Persona clarity and GUI constraint | GUI inspection            | Modified  |
| IR-003 | The system shall accept numeric text that can be converted into a finite floating-point value.         | Input requirement                  | Valid numeric input tests | Modified  |
| IR-004 | The system shall reject non-numeric base input with a field-specific message.                          | Helpful error requirement          | Enter `abc` as base       | Modified  |
| IR-005 | The system shall reject non-numeric exponent input with a field-specific message.                      | Helpful error requirement          | Enter `abc` as exponent   | Modified  |
| IR-006 | The system shall reject NaN and positive or negative infinity.                                         | Supported finite domain            | Enter NaN and infinity    | Modified  |
| IR-007 | The system shall preserve both input fields after an expected error so that the user can correct them. | Persona recovery need              | GUI recovery inspection   | New       |

## 13.3 Domain Requirements

| ID     | Requirement statement                                                                               | Source or rationale         | Verification method         | D1 status |
| ------ | --------------------------------------------------------------------------------------------------- | --------------------------- | --------------------------- | --------- |
| DR-001 | The system shall support finite integer-valued and non-integer exponents when the base is positive. | Supported domain            | Positive-base tests         | Retained  |
| DR-002 | The system shall support a zero base only when the exponent is positive.                            | Supported domain            | Zero-base tests             | Retained  |
| DR-003 | The system shall reject (0^0) as undefined.                                                         | Mathematical domain         | Execute (0^0)               | Retained  |
| DR-004 | The system shall reject zero raised to a negative exponent.                                         | Division-by-zero prevention | Execute (0^{-1})            | Retained  |
| DR-005 | The system shall support a negative base when the exponent is integer-valued.                       | Supported real domain       | Negative-base integer cases | Retained  |
| DR-006 | The system shall reject a negative base with a non-integer exponent.                                | Real-valued-only constraint | Execute ((-2)^{0.5})        | Retained  |
| DR-007 | The system shall return real-valued results only.                                                   | D1 scope                    | Domain inspection           | Retained  |

## 13.4 User Interface Requirements

| ID     | Requirement statement                                                                           | Source or rationale           | Verification method               | D1 status |
| ------ | ----------------------------------------------------------------------------------------------- | ----------------------------- | --------------------------------- | --------- |
| UI-001 | The system shall provide a Tkinter graphical user interface.                                    | D2 Problem 5                  | Launch application                | New       |
| UI-002 | The system shall display an application title and short explanation.                            | Persona clarity               | GUI inspection                    | New       |
| UI-003 | The system shall provide a Calculate control.                                                   | D2 GUI requirement            | GUI inspection and use            | New       |
| UI-004 | The system shall provide a Clear control.                                                       | D2 GUI requirement            | GUI inspection and use            | New       |
| UI-005 | The system shall provide an Exit control.                                                       | D2 GUI requirement            | GUI inspection and use            | New       |
| UI-006 | The system shall provide a clearly labelled result field.                                       | Persona output clarity        | GUI inspection                    | Modified  |
| UI-007 | The system shall provide a separate status or error-message area.                               | Helpful error requirement     | GUI inspection                    | New       |
| UI-008 | The system shall perform the calculation when the user presses Enter.                           | D2 keyboard requirement       | Press Enter after entering values | New       |
| UI-009 | The system shall clear both inputs, the result, and the previous status when Clear is selected. | D2 Clear behavior             | GUI interaction                   | New       |
| UI-010 | The system shall return keyboard focus to the base field after Clear is selected.               | Efficient correction workflow | GUI interaction                   | New       |
| UI-011 | The system shall close normally when Exit is selected.                                          | D2 Exit behavior              | GUI interaction                   | New       |

## 13.5 Error-Handling Requirements

| ID     | Requirement statement                                                                                                          | Source or rationale          | Verification method                   | D1 status |
| ------ | ------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- | ------------------------------------- | --------- |
| EH-001 | The system shall use specific custom exceptions for invalid input, unsupported domain, numeric range, and convergence failure. | D2 exception requirement     | Code inspection                       | Modified  |
| EH-002 | The system shall display a plain-language message for each expected input or domain error.                                     | Persona and D2 requirement   | Invalid-case execution                | Modified  |
| EH-003 | The system shall clear the displayed result after an unsuccessful calculation.                                                 | Avoid stale output           | GUI invalid-case inspection           | New       |
| EH-004 | The system shall remain open after an expected input or domain error.                                                          | Error recovery requirement   | GUI invalid-case inspection           | Modified  |
| EH-005 | The system shall allow a valid calculation immediately after an expected error.                                                | Recovery requirement         | Invalid input followed by valid input | New       |
| EH-006 | The system shall not use a bare `except` clause.                                                                               | Software-engineering quality | Code inspection                       | New       |
| EH-007 | The system shall not silently hide unexpected programming errors.                                                              | Debuggability                | Code inspection                       | New       |

## 13.6 Numerical Requirements

| ID     | Requirement statement                                                                                            | Source or rationale         | Verification method                         | D1 status |
| ------ | ---------------------------------------------------------------------------------------------------------------- | --------------------------- | ------------------------------------------- | --------- |
| NR-001 | The system shall detect a result that exceeds the supported floating-point range.                                | D2 overflow requirement     | Overflow test                               | Modified  |
| NR-002 | The system shall report overflow using a helpful result-too-large message.                                       | Persona clarity             | Overflow test                               | New       |
| NR-003 | The system shall reject results below the minimum supported normal magnitude.                                    | Severe-underflow constraint | Underflow test                              | Modified  |
| NR-004 | The system shall report severe underflow using a helpful result-too-small message.                               | Persona clarity             | Underflow test                              | New       |
| NR-005 | The system shall stop logarithm and exponential approximations when their convergence criterion is satisfied.    | Numerical algorithm design  | Code inspection                             | New       |
| NR-006 | The system shall apply a maximum iteration limit to each approximation series.                                   | Prevent endless iteration   | Code inspection                             | New       |
| NR-007 | The system shall raise a convergence exception when an iterative calculation exceeds its supported limit.        | D2 convergence requirement  | Reduced-limit test or controlled simulation | New       |
| NR-008 | The system shall update approximation powers and terms using multiplication rather than built-in exponentiation. | From-scratch constraint     | Code inspection                             | New       |
| NR-009 | The system shall reject non-finite intermediate results.                                                         | Numerical safety            | Extreme input tests                         | New       |

## 13.7 Implementation Constraints

| ID     | Requirement statement                                                                              | Source or rationale             | Verification method | D1 status |
| ------ | -------------------------------------------------------------------------------------------------- | ------------------------------- | ------------------- | --------- |
| IC-001 | The system shall implement the power calculation from scratch in Python.                           | D2 Problem 5                    | Code inspection     | Modified  |
| IC-002 | The system shall not use `pow()`, `math.pow()`, or `**` to evaluate (x^y).                         | D2 restriction                  | Source search       | New       |
| IC-003 | The system shall not use `math.log()` or another built-in logarithm operation to evaluate (x^y).   | D2 restriction                  | Source search       | New       |
| IC-004 | The system shall not use `math.exp()` or another built-in exponential operation to evaluate (x^y). | D2 restriction                  | Source search       | New       |
| IC-005 | The system shall not use `math.isfinite()` for finite-value validation.                            | Prompt restriction              | Source search       | New       |
| IC-006 | The system shall not use NumPy, SciPy, Decimal, Fractions, SymPy, or cmath.                        | External-library restriction    | Imports inspection  | New       |
| IC-007 | The system shall not use `eval()` to parse or calculate input.                                     | Security and prompt restriction | Source search       | New       |
| IC-008 | The calculation functions shall be importable without automatically starting the GUI.              | Independent calculation layer   | Import inspection   | New       |
| IC-009 | The application shall use `if __name__ == "__main__":` to control startup.                         | Python independence requirement | Code inspection     | New       |
| IC-010 | The application shall run using a standard Python command without dependence on a particular IDE.  | D2 execution requirement        | Run from terminal   | New       |

## 13.8 Accuracy Requirements

| ID     | Requirement statement                                                             | Source or rationale                 | Verification method | D1 status |
| ------ | --------------------------------------------------------------------------------- | ----------------------------------- | ------------------- | --------- |
| AR-001 | The system shall return exactly 8 for (2^3).                                      | Representative verification         | Execute VT-01       | Retained  |
| AR-002 | The system shall return exactly 0.0009765625 for (2^{-10}).                       | Representative verification         | Execute VT-02       | New       |
| AR-003 | The system shall approximate (4^{0.5}) as 2 within relative error (10^{-9}).      | Non-integer path verification       | Execute VT-03       | Modified  |
| AR-004 | The system shall approximate (16^{0.25}) as 2 within relative error (10^{-9}).    | Non-integer path verification       | Execute VT-04       | New       |
| AR-005 | The system shall return exactly -8 for ((-2)^3).                                  | Negative-base verification          | Execute VT-05       | Retained  |
| AR-006 | The system shall return exactly 16 for ((-2)^4).                                  | Even-exponent verification          | Execute VT-06       | New       |
| AR-007 | The system shall return exactly -0.125 for ((-2)^{-3}).                           | Negative base and negative exponent | Execute VT-07       | New       |
| AR-008 | The system shall return exactly 0 for (0^3).                                      | Zero-base verification              | Execute VT-08       | Retained  |
| AR-009 | The system shall return exactly 1 for (5^0).                                      | Zero-exponent verification          | Execute VT-09       | Retained  |
| AR-010 | The system shall approximate (0.25^{0.5}) as 0.5 within relative error (10^{-9}). | Fractional-base verification        | Execute VT-10       | New       |

---

# 14. Requirements-to-Code Traceability

The final implementation should provide traceability from project motivation to verification evidence.

| Source                                 | Requirement              | Proposed implementation element      | Verification evidence             |
| -------------------------------------- | ------------------------ | ------------------------------------ | --------------------------------- |
| Alex requires clear input              | IR-001, IR-002           | Labelled Tkinter entries             | GUI screenshot                    |
| Alex requires understandable output    | UI-006                   | Labelled result field                | Successful calculation screenshot |
| Alex requires helpful errors           | EH-002                   | Status area and exception messages   | Invalid-input screenshots         |
| D2 requires Tkinter                    | UI-001                   | `PowerCalculatorApp`                 | GUI launch evidence               |
| D2 requires Calculate control          | UI-003                   | `calculate()`                        | Valid-case screenshot             |
| D2 requires Clear control              | UI-004, UI-009, UI-010   | `clear()`                            | Before-and-after screenshot       |
| D2 requires Exit control               | UI-005, UI-011           | `root.destroy`                       | Manual observation                |
| D2 requires Enter-key calculation      | UI-008                   | `root.bind("<Return>", ...)`         | Manual key test                   |
| D1 selected exponentiation by squaring | FR-002                   | `power_by_squaring()`                | Integer test results              |
| D1 selected hybrid evaluation          | FR-004                   | `calculate_power()`                  | Integer and non-integer tests     |
| D2 requires custom logarithm           | FR-005, IC-003           | `natural_log()`                      | Code inspection and VT-03         |
| D2 requires custom exponential         | FR-006, IC-004           | `exponential()`                      | Code inspection and VT-03         |
| D2 prohibits built-in power            | IC-002                   | Multiplication-based loops           | Source search                     |
| D2 requires finite input               | IR-006                   | `is_finite_number()`                 | NaN and infinity screenshots      |
| Real-valued domain                     | DR-005, DR-006, DR-007   | Domain checks in `calculate_power()` | Negative-base cases               |
| Overflow handling                      | NR-001, NR-002           | `checked_multiply()`                 | Overflow screenshot               |
| Severe-underflow handling              | NR-003, NR-004           | minimum-normal comparison            | Underflow screenshot              |
| Convergence protection                 | NR-005, NR-006, NR-007   | tolerance and iteration constants    | Code inspection                   |
| Independent execution                  | IC-008, IC-009, IC-010   | `main()` guard                       | Terminal launch                   |
| Problem 6 repository requirement       | Repository documentation | D1/D2 directories and README         | GitHub inspection                 |
| Problem 7 requirement revision         | All D2 requirements      | `REQUIREMENTS.md`                    | Document inspection               |

---

# 15. Known Numerical Limitations

The final documentation should clearly state the following limitations.

## 15.1 Real-Valued Results Only

The calculator does not return complex values.

Therefore, a negative base with a non-integer exponent is rejected.

## 15.2 Binary Floating-Point Input

Inputs are converted to Python floating-point values.

As a result:

* long decimal inputs may be rounded before calculation;
* mathematically different large integers may map to the same stored value;
* exact decimal representation is not guaranteed.

## 15.3 Subnormal Results

Results below:

[
2.2250738585072014\times10^{-308}
]

are intentionally rejected.

The program treats these values as too small to represent accurately within the supported normal range.

## 15.4 Overflow Boundaries

Results above the maximum finite floating-point magnitude are rejected.

Some mathematically valid results near this boundary may also be rejected if an intermediate multiplication exceeds the supported range.

## 15.5 Approximation Error

The custom logarithm and exponential functions use finite iterative series.

Approximation error may increase for:

* extreme values;
* poorly conditioned calculations;
* inputs close to overflow or underflow;
* values affected by significant floating-point rounding.

## 15.6 Stored (\ln(2)) Constant

Range reduction uses a stored floating-point approximation of (\ln(2)).

The constant itself has finite precision and contributes to the final approximation error.

## 15.7 Integer-Valued Detection

Integer-valued detection operates on the stored floating-point number.

Very large decimal exponents may lose their fractional part during input conversion and may therefore appear integer-valued.

## 15.8 No Universal Support Claim

The implementation should not claim that every possible floating-point input is supported.

It should claim only that representative supported cases meet the stated verification criteria after testing.

---

# 16. Remaining Manual Actions

The following work must be completed or confirmed by the student.

## Implementation

* Create `D2/power_calculator.py`.
* Implement the custom exception hierarchy.
* Implement custom finite-number detection.
* Implement custom integer-valued detection.
* Implement checked multiplication and reciprocal handling.
* Implement `power_by_squaring()`.
* Implement `natural_log()`.
* Implement `exponential()`.
* Implement `calculate_power()`.
* Implement the Tkinter interface.
* Add the `__main__` startup guard.

## Verification

* Execute all valid representative cases.
* Execute all invalid representative cases.
* Confirm the GUI remains open after every expected error.
* Confirm the result field is cleared after every error.
* Confirm a corrected calculation succeeds.
* Verify overflow behavior.
* Verify severe-underflow behavior.
* Verify convergence-failure behavior.
* Compare approximate results against the selected tolerance.
* Inspect the source for every prohibited operation.

## Documentation

* Create `D2/README.md`.
* Create `D2/IMPLEMENTATION.md`.
* Create `D2/REQUIREMENTS.md`.
* Create `D2/screenshots/README.md`.
* Update the root README.
* Document numerical limitations honestly.
* Add actual test results only after execution.

## GitHub

* Preserve the D1 directory.
* Create a separate D2 directory.
* Add `.gitignore`.
* Commit only real changes.
* Use meaningful imperative commit messages.
* Push commits normally.
* Do not amend, squash, rebase, or force-push existing history.
* Confirm the repository remains public.

## Evidence

* Capture the required GUI screenshots.
* Use stable and descriptive screenshot filenames.
* Ensure every screenshot clearly shows:

  * the entered values;
  * the result or error;
  * the status area;
  * the open application window.

---

# Final Compliance Checklist

## Problem 5 — Proposed Coverage

| Requirement                          | Proposed status                                     |
| ------------------------------------ | --------------------------------------------------- |
| Extend D1 rather than redesign       | Covered by hybrid-algorithm continuation            |
| Implement (x^y) from scratch         | Covered by proposed algorithms                      |
| Integer exponentiation by squaring   | Covered                                             |
| Custom logarithm                     | Covered                                             |
| Custom exponential                   | Covered                                             |
| Preserve real-valued domain          | Covered                                             |
| Tkinter GUI                          | Covered                                             |
| Exception handling                   | Covered                                             |
| Helpful error messages               | Covered                                             |
| Independent calculation layer        | Covered                                             |
| Overflow handling                    | Covered                                             |
| Severe-underflow handling            | Covered                                             |
| Convergence handling                 | Covered                                             |
| No prohibited mathematical operation | Designed for compliance; source inspection required |
| Actual execution                     | Not yet confirmed                                   |
| Actual screenshots                   | Not yet confirmed                                   |

## Problem 6 — Proposed Coverage

| Requirement                    | Proposed status         |
| ------------------------------ | ----------------------- |
| Public GitHub repository       | Repository identified   |
| Preserve D1                    | Required                |
| Separate D1 and D2 directories | Proposed                |
| Complete D2 README             | Proposed                |
| Implementation documentation   | Proposed                |
| Meaningful commits             | Recommended             |
| Actual commits created         | Not claimed             |
| Repository contents verified   | Student action required |

## Problem 7 — Proposed Coverage

| Requirement                       | Proposed status                      |
| --------------------------------- | ------------------------------------ |
| Revised D1 requirements           | Covered                              |
| Unique requirement identifiers    | Covered                              |
| ISO/IEC/IEEE 29148-style wording  | Covered using “The system shall”     |
| Source or rationale               | Included                             |
| Verification method               | Included                             |
| D1 status                         | Included                             |
| Requirements-to-code traceability | Included                             |
| Match with final code             | Must be checked after implementation |

## Final Assessment

The proposed design covers the requested scope of Delivery 2 Problems 5, 6, and 7.

However, the following claims cannot yet be made:

* that the implementation has been executed;
* that all representative cases passed;
* that the GUI recovery behavior has been observed;
* that screenshots have been captured;
* that commits have been created;
* that the repository has been updated;
* that the final code contains no prohibited operation.

These items require student implementation, execution, inspection, and confirmation before submission.
