# SOEN 6011 — Delivery 2 (Problems 5, 6, 7)

## F7: Power Function — x raised to y

This document was produced with GAI assistance. The calculation layer described
here was **actually written and executed**; every verification number below
comes from a real run (Python 3.12, headless Tkinter). Items that still require
the student — screenshots, Git commits, and running the GUI on your own
machine — are marked explicitly and must not be claimed as done until done.

Repository: `https://github.com/prprtracy/6011_F7.git`

---

## 1. Existing D1 design inspected

| Aspect | D1 state |
|---|---|
| Domain | x>0 → integer & non-integer; x=0 → only y>0; x<0 → only integer; reject NaN/∞/overflow/underflow; real results only |
| Algorithm | Hybrid Power Evaluation — exponentiation by squaring for integer exponents; `x^y = exp(y·ln x)` for positive base, non-integer exponent |
| Input validation | Numeric conversion, reject non-numeric/NaN/∞, integer-valued detection, reject unsupported combinations, retry after error |
| Error handling | Invalid text, 0^0, zero to negative exponent, negative base with non-integer exponent, overflow/underflow |
| Requirement IDs | ISO/IEC/IEEE 29148 "The system shall…"; FR/IR/OR/ER/UR/AR/CR |

**D1 requirements affected by D2:** CR-001 (prohibition widens to log + exp),
UR-002/003 (textual UI → Tkinter), ER-003 (split out underflow), IR-004
(re-prompt loop → GUI recovery). D1 files are **not** modified.

---

## 2. D2 implementation summary

Single file `D2/power_calculator.py`, two separated layers:

- **Calculation layer** (importable, no window needed): `calculate_power`,
  `power_by_squaring`, `natural_log`, `exponential`, `parse_number`,
  `format_result`, plus helpers `is_finite_number`, `is_integer_value`,
  `_checked_multiply`.
- **GUI layer**: `PowerCalculatorApp` over Tkinter.

Numerical paths:

```text
integer-valued exponent              → power_by_squaring()
positive base, non-integer exponent  → exponential(exponent * natural_log(base))
```

---

## 3. From-scratch numerical algorithms

### 3.1 Integer exponents — exponentiation by squaring

```python
def power_by_squaring(base: float, exponent: int) -> float:
    if exponent == 0:
        return 1.0
    if base == 0.0:
        if exponent < 0:
            raise UnsupportedDomainError("Zero cannot be raised to a negative exponent.")
        return 0.0

    remaining = exponent
    factor = float(base)
    if remaining < 0:
        factor = 1.0 / factor          # invert the base FIRST
        if factor == 0.0 or absolute_value(factor) < MIN_NORMAL:
            raise NumericRangeError("The result is too small to be represented accurately by this calculator.")
        remaining = -remaining

    result = 1.0
    while remaining > 0:
        if remaining % 2 == 1:
            result = _checked_multiply(result, factor)
        remaining //= 2
        if remaining > 0:
            factor = _checked_multiply(factor, factor)
    return result
```

Uses multiplication, division, comparison, modulo, integer division, loops.
No `pow()`, `math.pow()`, `**`. Loop count is **O(log |y|)** — measured at 26
checked multiplications for `y = 1_000_000`.

**Design choice that matters:** inverting the base *before* the loop means a
genuinely tiny result (e.g. `10^-400`) is reported as *underflow*, not masked
by an intermediate overflow of `10^400`. The naïve "compute the positive power,
then take the reciprocal" order gets this error direction wrong.

### 3.2 Custom natural logarithm

Range-reduce `x = m·2^k` with `0.75 ≤ m ≤ 1.5`, then
`ln(x) = ln(m) + k·ln(2)`. With `z = (m−1)/(m+1)`:

$$\ln(m) = 2\left(z + \frac{z^3}{3} + \frac{z^5}{5} + \cdots\right)$$

Higher powers of `z` are formed by multiplication (`term *= z_squared`), with a
tolerance, a `MAX_SERIES_ITERATIONS` cap, and a `MAX_RANGE_REDUCTIONS` cap on
the reduction loops; both raise `ConvergenceError` if exceeded.

### 3.3 Custom exponential

Range-reduce `v = k·ln(2) + r` so `e^v = 2^k · e^r`, then

$$e^r = 1 + r + \frac{r^2}{2!} + \frac{r^3}{3!} + \cdots$$

Each term is derived from the previous one (`term = term * r / index`). The
power of two is restored with `power_by_squaring(2.0, k)`; scales outside
`[-1022, 1023]` raise `NumericRangeError`.

### 3.4 Constants (values only — no power/log/exp evaluation)

```python
LN_2 = 0.6931471805599453
MAX_FLOAT = 1.7976931348623157e308
MIN_NORMAL = 2.2250738585072014e-308
SERIES_TOLERANCE = 1e-16
MAX_SERIES_ITERATIONS = 1000
MAX_RANGE_REDUCTIONS = 4096
```

---

## 4. Exception hierarchy

```text
PowerCalculatorError
├── InvalidInputError       # missing / non-numeric / NaN / infinity
├── UnsupportedDomainError  # unsupported real-valued combination
├── NumericRangeError       # overflow or severe underflow
└── ConvergenceError        # series or reduction hit its iteration limit
```

The GUI catches only `PowerCalculatorError`. No bare `except`. Unexpected
programming errors are not hidden.

---

## 5. Supported-domain behaviour

`calculate_power()` validates before dispatch:

| Condition | Behaviour |
|---|---|
| positive base, integer exponent | exponentiation by squaring |
| positive base, non-integer exponent | custom ln + exp |
| zero base, positive exponent | return 0 |
| 0^0 | reject (undefined) |
| zero base, negative exponent | reject |
| negative base, integer exponent | exponentiation by squaring |
| negative base, non-integer exponent | reject (real-valued only) |
| non-numeric / NaN / infinity | reject |
| overflow / severe underflow / convergence failure | reject |

---

## 6. Tkinter GUI design

Title, short explanation, labelled **Base x** and **Exponent y** fields,
**Calculate** / **Clear** / **Exit** buttons, a labelled result field, and a
separate status area. `<Return>` triggers Calculate. **Clear** empties both
inputs, the result, and the status, and returns focus to the base field.
Calculation functions are importable without launching the window
(`if __name__ == "__main__":`).

---

## 7. Helpful error messages (plain language, field-specific)

```text
Please enter a numeric value for the base x.
Please enter a numeric value for the exponent y.
NaN and infinity are not supported. Please enter a finite number.
The expression 0^0 is undefined. Please enter a positive exponent when the base is zero.
Zero cannot be raised to a negative exponent.
A negative base requires an integer exponent because this calculator returns real-valued results only.
The result is too large to be represented by this calculator.
The result is too small to be represented accurately by this calculator.
The calculation did not converge within the supported number of iterations.
```

No bare "Math Error" and no raw traceback in the GUI.

---

## 8. Verification results (executed — not a plan)

### 8.1 Valid cases — all PASS (relative error 0)

| ID | Case | Result | rel. err |
|---|---|---|---|
| VT-01 | 2^3 | 8 | 0 |
| VT-02 | 2^-10 | 0.0009765625 | 0 |
| VT-03 | 4^0.5 | 2 | 0 |
| VT-04 | 16^0.25 | 2 | 0 |
| VT-05 | (-2)^3 | -8 | 0 |
| VT-06 | (-2)^4 | 16 | 0 |
| VT-07 | (-2)^-3 | -0.125 | 0 |
| VT-08 | 0^3 | 0 | 0 |
| VT-09 | 5^0 | 1 | 0 |
| VT-10 | 0.25^0.5 | 0.5 | 0 |

### 8.2 Invalid cases — all PASS (correct exception + message)

| ID | Input | Exception raised |
|---|---|---|
| IT-01 | 0^0 | `UnsupportedDomainError` (undefined) |
| IT-02 | 0^-1 | `UnsupportedDomainError` (negative exponent) |
| IT-03 | (-2)^0.5 | `UnsupportedDomainError` (integer exponent required) |
| IT-04 | `abc` base | `InvalidInputError` (numeric base) |
| IT-05 | `abc` exponent | `InvalidInputError` (numeric exponent) |
| IT-06 | NaN | `InvalidInputError` (finite number) |
| IT-07/08 | +inf / -inf | `InvalidInputError` (finite number) |
| IT-09 | 10^400, 1e308^2, 0.5^-5000 | `NumericRangeError` (too large) |
| IT-10 | 10^-400, 1e-308^2, 2^-5000 | `NumericRangeError` (too small) |

The negative-exponent range cases (`10^-400` → too small, `0.5^-5000` → too
large) confirm the invert-first design reports the correct direction.

### 8.3 Accuracy vs an independent reference (verification only)

| Case | Relative error |
|---|---|
| 2^0.5 | 1.6e-16 |
| 10^0.3 | 1.1e-16 |
| 0.5^2.5 | 0 |
| 123.456^1.789 | 1.7e-16 |
| 9^-0.5 | 1.7e-16 |
| 1.0001^1000.5 | 4.0e-16 |

All within the D1 accuracy target (relative error ≤ 1e-9).

### 8.4 GUI behaviour (headless Tkinter run)

Valid calc displays and status = success; invalid `(-2)^0.5` leaves result
empty and shows the domain message with the window still open; **Clear** resets
everything; a valid calc succeeds immediately afterward; `<Return>` computes.
All confirmed.

### 8.5 Still requires the student

- Capture real screenshots of each case in the GUI on your machine.
- Run `python power_calculator.py` yourself for a visual check.

---

## 9. Prohibited-operation check

Source scan of the executable code (comments and docstrings stripped by
tokeniser): **no matches** for `pow(`, `math.`, `**`, `math.log`, `math.exp`,
`math.isfinite`, `numpy`, `scipy`, `decimal`, `fractions`, `sympy`, `cmath`,
`eval(`. Only import is `tkinter`.

> No built-in mathematical power, logarithm, or exponential operation is used
> to evaluate x raised to y.

Legitimately used: `float()`, `int()`, `format()`, `range()`, comparisons,
arithmetic, loops, exceptions, Tkinter.

---

## 10. GitHub repository organization

```text
6011_F7/
├── D1/                     # preserved, unchanged
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

Do **not** delete/overwrite D1, rewrite history, amend, squash, rebase, or
force-push. Every commit should be a real, inspectable change.

---

## 11. Recommended commit messages (imperative, not yet committed)

```text
Add D2 from-scratch power calculation layer
Implement integer exponentiation by squaring with checked arithmetic
Implement custom natural logarithm approximation
Implement custom exponential approximation
Add numeric-range and convergence exception hierarchy
Add Tkinter power calculator interface
Document D2 execution, domain, and numerical limitations
Add updated D2 ISO/IEC/IEEE 29148 requirements
Document D2 GUI verification evidence
Add Python and editor files to gitignore
```

Avoid: `update`, `fix`, `changes`, `final`, `D2`, `D2 update`.

---

## 12. README summary

`D2/README.md` should carry: title; course and deliverable; F7; supported
real-valued domain; from-scratch statement; exponentiation by squaring; custom
logarithm; custom exponential; Tkinter GUI behaviour; exception handling;
execution instructions (`cd D2` / `python power_calculator.py`, Tkinter
required); representative valid and invalid cases; known numerical limitations;
repository structure.

---

## 13. Updated requirements (ISO/IEC/IEEE 29148)

Legend — **R**etained / **M**odified / **N**ew.

### Functional

| ID | The system shall … | Source / rationale | Verification | Status |
|---|---|---|---|---|
| FR-001 | compute x^y for every supported finite real input combination | assigned function F7 | valid cases | M |
| FR-002 | evaluate integer-valued exponents by exponentiation by squaring in O(log \|y\|), without a built-in power op | D1 algorithm + D2 constraint | inspection; 26 mults for y=1e6 | M |
| FR-003 | evaluate a positive base with non-integer exponent via `exp(y·ln x)`, both from scratch | D1 hybrid + D2 constraint | VT-03/04/10 | M |
| FR-004 | compute ln via power-of-two reduction and an iterative series, powers updated by multiplication | D2 Task 3 | inspection | N |
| FR-005 | compute exp via ln(2) reduction and an iterative Taylor series, terms derived from the previous term | D2 Task 3 | inspection | N |
| FR-006 | identify whether the exponent is integer-valued before selecting the path | hybrid selection | inspection; VT-05 vs VT-03 | R |

### Input

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| IR-001 | provide labelled input fields for base x and exponent y | persona + GUI | GUI inspection | M |
| IR-002 | accept only finite numeric input; reject non-numeric text, NaN, ±infinity | D1 IR-002 + Task 4 | IT-04..08 | M |
| IR-003 | preserve both fields after an expected error so the user can correct them | persona recovery | GUI recovery test | N |

### Domain

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| DR-001 | support finite integer and non-integer exponents for a positive base | D1 domain | positive-base tests | R |
| DR-002 | support a zero base only when y > 0 | D1 domain | VT-08 | R |
| DR-003 | reject 0^0 as undefined | domain | IT-01 | R |
| DR-004 | reject zero raised to a negative exponent | domain | IT-02 | R |
| DR-005 | support a negative base only when y is integer-valued | real domain | VT-05/06/07 | R |
| DR-006 | reject a negative base with a non-integer exponent | real-only | IT-03 | R |
| DR-007 | return real-valued results only | D1 scope | inspection | R |

### User interface

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| UI-001 | provide a Tkinter GUI with title and short explanation | D2 Problem 5 | launch | N |
| UI-002 | provide Calculate, Clear, and Exit controls | D2 GUI | GUI use | N |
| UI-003 | display the result in a clearly labelled field | persona output | GUI inspection | M |
| UI-004 | display status/error in an area separate from the result | helpful errors | invalid-case GUI | N |
| UI-005 | perform the calculation when Enter is pressed | D2 keyboard | Enter test | N |
| UI-006 | on Clear, empty both inputs, result, and status, and refocus the base field | D2 Clear | GUI interaction | N |
| UI-007 | close normally on Exit | D2 Exit | GUI interaction | N |

### Error handling

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| EH-001 | use specific custom exceptions for invalid input, unsupported domain, numeric range, and convergence | D2 Task 5 | inspection | M |
| EH-002 | show a plain-language message for each expected error, never only "Math Error" or a traceback | persona + Task 7 | IT-01..10 | M |
| EH-003 | clear the result after an unsuccessful calculation | avoid stale output | invalid-case GUI | N |
| EH-004 | remain open after an expected error and allow an immediate valid calculation | recovery | recovery test | M |
| EH-005 | not use a bare `except`, and not silently hide unexpected errors | SE quality | inspection | N |

### Numerical

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| NR-001 | detect overflow and report a result-too-large message | D2 overflow | IT-09 | M |
| NR-002 | reject results below the minimum supported normal magnitude and report result-too-small | severe underflow | IT-10 | M |
| NR-003 | stop each approximation at a convergence tolerance under a maximum iteration limit | algorithm design | inspection | N |
| NR-004 | raise a convergence exception when an iterative calculation exceeds its limit | D2 convergence | inspection | N |

### Constraints

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| CR-001 | not use pow(), math.pow(), or ** to evaluate x^y | D2 restriction | source scan | M |
| CR-002 | not use math.log() or math.exp() to evaluate x^y | D2 restriction | source scan | N |
| CR-003 | not use numpy, scipy, decimal, fractions, sympy, cmath, or eval() | D2 restriction | import scan | N |
| CR-004 | keep the calculation functions importable without launching the GUI, IDE-independent, guarded by `if __name__ == "__main__":` | independent layer | import test | N |

### Accuracy

| ID | The system shall … | Source | Verification | Status |
|---|---|---|---|---|
| AR-001 | for the ten representative cases, have absolute error ≤ 1e-9 when expected is 0, else relative error ≤ 1e-9 | D1 AR-001 | VT-01..10 | R |

---

## 14. Requirements-to-code traceability

| Persona need / D2 constraint | Requirement | Code element | Verification evidence |
|---|---|---|---|
| Compute x^y accurately | FR-001, AR-001, DR-* | `calculate_power()` | VT-01..10 all PASS |
| From-scratch computation | FR-002/003/004/005, CR-001/002/003 | `power_by_squaring`, `natural_log`, `exponential` | source scan clean |
| Efficient integer path | FR-002 | binary loop | 26 mults for y=1e6 |
| Series construction rules | FR-004/005, NR-003/004 | reduction loops, tolerance & iteration caps | inspection |
| Clear inputs (Alex) | IR-001/002, FR-006 | `parse_number`, labelled entries | IT-04..08 |
| Continue after errors (Alex) | IR-003, EH-004 | `calculate()` catching `PowerCalculatorError` | recovery test |
| Understandable failures (Alex) | EH-001/002 | domain messages | IT-01/02/03 |
| Reliable ranges | NR-001/002 | `_checked_multiply`, invert-first reciprocal, scale checks | IT-09/10 |
| Robust failure model | EH-005 | specific `except` only | inspection |
| Labelled output | UI-003/004 | result & status labels | screenshots (student) |
| Graphical usability | UI-001/002/005/006/007 | `PowerCalculatorApp`, `clear()`, `<Return>` | GUI test |
| IDE-independent verification | CR-004 | module functions + main guard | import test |

---

## 15. Known numerical limitations

- Real-valued results only; negative base with non-integer exponent rejected.
- Inputs are binary floats, so long decimals may already be rounded.
- Subnormal results below the minimum supported normal magnitude are rejected.
- Values near the overflow/underflow boundary may be rejected when an
  intermediate step leaves the supported normal range.
- Approximation error can grow for ill-conditioned or extreme inputs.
- Not every possible floating-point input is claimed to be supported.

---

## 16. Remaining manual actions

1. Create `D2/power_calculator.py` from the code above; add `README.md`,
   `IMPLEMENTATION.md`, `REQUIREMENTS.md`, `screenshots/`.
2. Run the GUI yourself and **capture real screenshots** of each valid and
   invalid case; do not claim screenshots until captured.
3. Commit with the messages in §11; do not rewrite D1 or existing history.
4. Confirm any D1 requirement wording (FR-001, IR-*, CR-001) against the D1
   report text before finalising the "Retained/Modified" labels.

**Compliance:** Problem 5 ✅ (code written and executed), Problem 6 ▶ (structure
and commit plan ready; commits/screenshots are yours to make), Problem 7 ✅
(requirements + traceability match the executed code). No verification result,
screenshot, or commit is claimed as done unless it actually is.
