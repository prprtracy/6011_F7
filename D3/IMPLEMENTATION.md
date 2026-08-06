# D3 Implementation Notes

## Architecture

```text
GUI
  ↓
Input Parsing
  ↓
Domain Validation
  ↓
Numerical Core
  ↓
Result Formatting / Error Feedback
```

`PowerCalculatorApp` reads widget text and displays results or specific error
messages. Text-to-float conversion occurs only in `parse_numeric_input()`.
`calculate_power()` therefore receives numeric arguments, validates the
supported real-valued domain, and selects the integer or decimal calculation
path. The numerical core contains no GUI widget operations or text parsing.

## Integer Exponent Algorithm

`power_by_squaring()` implements exponentiation by squaring. It examines the
integer exponent in binary, multiplies the accumulated result for odd bits,
squares the factor, and halves the remaining exponent. This requires a
logarithmic number of multiplication steps relative to the exponent magnitude.

Positive integer exponents are evaluated directly. For negative integer
exponents, the function first uses the reciprocal factor and then evaluates the
positive magnitude. This preserves correct results such as `2^-3 = 0.125`
without using `pow()` or the `**` operator.

## Decimal Exponent Algorithm

For a positive base and non-integer exponent, the calculator uses:

```text
x^y = exp(y × ln(x))
```

`natural_log()` and `exponential()` are custom approximation functions using
range reduction and convergent series. Only positive bases enter this path.
Negative bases with non-integer exponents are rejected before logarithm
evaluation because complex results are outside the supported domain.

## Overflow Correction

The D2 implementation could reject a valid large finite result because its
range decision was made using a conservative estimate before multiplication.
The corrected implementation checks the actual computed multiplication result.
`math.isfinite()`, `math.isinf()`, and `math.isnan()` distinguish finite
results, genuine overflow, and undefined outcomes. The exponential restoration
also permits scale 1024 when its actual final product remains finite.

## Underflow Policy

Results below `MIN_NORMAL` are intentionally rejected because the calculator
does not claim accurate support for subnormal floating-point values. This is a
documented numerical accuracy policy and known limitation, not an accidental
calculation failure. The tests cover both a deterministic rejected underflow
and a nearby accepted normal result.

## Semantic Versioning

The D3 version is `1.1.0`:

- MAJOR remains 1 because the supported interface remains compatible.
- MINOR becomes 1 because D3 adds testing, accessibility, code-quality
  verification, and corrected range handling.
- PATCH remains 0 because this is the first release of the 1.1 feature set.

## Unit Testing

The 34-test PyUnit suite covers:

- parsing and field-specific errors;
- positive, negative, and zero integer powers;
- decimal powers through the custom approximation path;
- unsupported domain combinations;
- non-finite inputs;
- valid-large-result and genuine-overflow regressions;
- the documented underflow policy and nearby normal result; and
- direct integer-algorithm behavior.

## Tool Results

- Flake8: no PEP 8 violations.
- Pylint: 10.00/10.
- PyUnit: 34 tests passed.
