"""Core power-calculation logic for SOEN 6011 Delivery 1.

Requirement coverage:
- FR-001, CR-001: computes x^y only within the supported real-valued domain.
- IR-002: accepts only finite numeric values.
- IR-003: identifies whether the exponent is integer-valued.
- ER-001, ER-002, ER-003: rejects unsupported domains and range failures.
"""

from __future__ import annotations

import math


class PowerCalculationError(ValueError):
    """Base exception for controlled calculator errors."""


class DomainError(PowerCalculationError):
    """Raised when x and y are outside the supported D1 domain."""


class NumericRangeError(PowerCalculationError):
    """Raised when a calculation leaves the supported finite numeric range."""


def validate_finite_number(value: float, name: str) -> None:
    """Validate a numeric input for IR-002."""
    if not math.isfinite(value):
        raise DomainError(f"{name} must be a finite numeric value.")


def is_integer_valued(value: float) -> bool:
    """Return True when a finite float represents an integer value.

    The program parses input as float values, so this uses float.is_integer()
    after the finite-number check. It does not round non-integer values.
    """
    return math.isfinite(value) and value.is_integer()


def _checked_multiply(left: float, right: float) -> float:
    """Multiply two floats and reject non-finite or underflow results."""
    result = left * right
    if not math.isfinite(result):
        raise NumericRangeError(
            "the result is outside the supported numeric range."
        )
    if result == 0.0 and left != 0.0 and right != 0.0:
        raise NumericRangeError(
            "The result is too small to represent (underflow)."
        )
    return result


def power_by_squaring(base: float, exponent: int) -> float:
    """Compute base raised to an integer exponent in O(log |y|).

    This iterative exponentiation-by-squaring path is used for integer-valued
    exponents and intentionally avoids Python's built-in power operators.
    """
    if exponent == 0:
        return 1.0

    is_negative_exponent = exponent < 0
    remaining = -exponent if is_negative_exponent else exponent

    positive_power = 1.0
    factor = float(base)

    while remaining > 0:
        if remaining % 2 == 1:
            positive_power = _checked_multiply(positive_power, factor)
        remaining //= 2
        if remaining > 0:
            factor = _checked_multiply(factor, factor)

    if not is_negative_exponent:
        return positive_power

    if positive_power == 0.0:
        raise NumericRangeError(
            "the result is outside the supported numeric range."
        )
    result = 1.0 / positive_power
    if not math.isfinite(result):
        raise NumericRangeError(
            "the result is outside the supported numeric range."
        )
    if result == 0.0:
        raise NumericRangeError(
            "The result is too small to represent (underflow)."
        )
    return result


def hybrid_power(base: float, exponent: float) -> float:
    """Compute x^y using the selected Hybrid Power Evaluation algorithm.

    Integer-valued exponents use exponentiation by squaring. Non-integer
    exponents are supported only for positive bases and use exp(y * log(x)).
    """
    validate_finite_number(base, "base")
    validate_finite_number(exponent, "exponent")

    exponent_is_integer = is_integer_valued(exponent)

    if base == 0.0:
        if exponent == 0.0:
            raise DomainError("0^0 is undefined in this calculator.")
        if exponent < 0.0:
            raise DomainError("zero cannot be raised to a negative exponent.")
        return 0.0

    if base < 0.0 and not exponent_is_integer:
        raise DomainError(
            "a negative base requires an integer-valued exponent."
        )

    if exponent_is_integer:
        try:
            result = power_by_squaring(base, int(exponent))
        except OverflowError as error:
            raise NumericRangeError(
                "the result is outside the supported numeric range."
            ) from error
    else:
        try:
            result = math.exp(exponent * math.log(base))
        except (OverflowError, ValueError) as error:
            raise NumericRangeError(
                "the result is outside the supported numeric range."
            ) from error

    if not math.isfinite(result):
        raise NumericRangeError(
            "the result is outside the supported numeric range."
        )
    if result == 0.0:
        raise NumericRangeError(
            "The result is too small to represent (underflow)."
        )

    return result
