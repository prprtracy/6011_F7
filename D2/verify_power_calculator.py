"""Simple non-GUI verification for the calculation layer."""

from __future__ import annotations

import sys

from power_calculator import (
    ConvergenceError,
    InvalidInputError,
    NumericRangeError,
    PowerCalculatorError,
    UnsupportedDomainError,
    calculate_power,
    parse_number,
)


def check_close(name: str, actual: float, expected: float, tolerance: float) -> bool:
    """Check absolute or relative error against an expected value."""
    if expected == 0.0:
        error = abs(actual - expected)
    else:
        error = abs(actual - expected) / abs(expected)
    passed = error <= tolerance
    status = "PASS" if passed else "FAIL"
    print(f"{status}: {name} -> {actual} | error={error}")
    return passed


def check_exception(
    name: str,
    action,
    expected_exception,
    expected_message: str | None = None,
) -> bool:
    """Check that the expected exception is raised."""
    try:
        action()
    except expected_exception as error:
        message = str(error)
        if expected_message is None or expected_message in message:
            print(f"PASS: {name} -> raised {expected_exception.__name__}: {message}")
            return True
        print(f"FAIL: {name} -> message mismatch: {message}")
        return False
    except PowerCalculatorError as error:
        print(f"FAIL: {name} -> unexpected {type(error).__name__}: {error}")
        return False

    print(f"FAIL: {name} -> no exception raised")
    return False


all_passed = True

all_passed &= check_close("2^3", calculate_power(2.0, 3.0), 8.0, 1e-12)
all_passed &= check_close("2^-10", calculate_power(2.0, -10.0), 0.0009765625, 1e-12)
all_passed &= check_close("(-2)^3", calculate_power(-2.0, 3.0), -8.0, 1e-12)
all_passed &= check_close("(-2)^-3", calculate_power(-2.0, -3.0), -0.125, 1e-12)
all_passed &= check_close("(-2)^-4", calculate_power(-2.0, -4.0), 0.0625, 1e-12)
all_passed &= check_close("4^0.5", calculate_power(4.0, 0.5), 2.0, 1e-9)
all_passed &= check_close("2^0.3", calculate_power(2.0, 0.3), 1.2311444133449163, 1e-9)
all_passed &= check_close("0^3", calculate_power(0.0, 3.0), 0.0, 1e-12)
all_passed &= check_close("5^0", calculate_power(5.0, 0.0), 1.0, 1e-12)

all_passed &= check_exception(
    "0^0", lambda: calculate_power(0.0, 0.0), UnsupportedDomainError
)
all_passed &= check_exception(
    "0^-1", lambda: calculate_power(0.0, -1.0), UnsupportedDomainError
)
all_passed &= check_exception(
    "(-2)^0.5", lambda: calculate_power(-2.0, 0.5), UnsupportedDomainError
)
all_passed &= check_exception(
    "non-numeric base",
    lambda: parse_number("abc", "base x"),
    InvalidInputError,
)
all_passed &= check_exception(
    "NaN", lambda: parse_number("nan", "base x"), InvalidInputError
)
all_passed &= check_exception(
    "infinity", lambda: parse_number("inf", "base x"), InvalidInputError
)
all_passed &= check_exception(
    "10^400",
    lambda: calculate_power(10.0, 400.0),
    NumericRangeError,
    "exceeds the supported numeric range",
)
all_passed &= check_exception(
    "10^-400",
    lambda: calculate_power(10.0, -400.0),
    NumericRangeError,
    "too small",
)

if not all_passed:
    sys.exit(1)

print("All verification cases passed.")
