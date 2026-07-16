"""Tests for the core Hybrid Power Evaluation functions."""

from __future__ import annotations

import unittest

from src.power_calculator import (
    DomainError,
    NumericRangeError,
    hybrid_power,
    is_integer_valued,
    power_by_squaring,
    validate_finite_number,
)


class PowerCalculatorTestCase(unittest.TestCase):
    """Core mathematical tests for AR-001."""

    def assert_close_ar001(self, actual: float, expected: float) -> None:
        """Apply AR-001 absolute/relative error tolerance."""
        tolerance = 1e-9
        if expected == 0:
            self.assertLessEqual(abs(actual - expected), tolerance)
        else:
            relative_error = abs((actual - expected) / expected)
            self.assertLessEqual(relative_error, tolerance)

    def test_integer_valued_detection(self) -> None:
        self.assertTrue(is_integer_valued(3.0))
        self.assertTrue(is_integer_valued(-2.0))
        self.assertFalse(is_integer_valued(0.5))
        self.assertFalse(is_integer_valued(2.0001))

    def test_power_by_squaring_integer_exponents(self) -> None:
        self.assertEqual(power_by_squaring(2.0, 3), 8.0)
        self.assertEqual(power_by_squaring(2.0, 0), 1.0)
        self.assertEqual(power_by_squaring(2.0, -3), 0.125)

    def test_valid_integer_exponent_cases(self) -> None:
        cases = [
            (2.0, 3.0, 8.0),
            (2.0, 0.0, 1.0),
            (2.0, -3.0, 0.125),
            (-2.0, 3.0, -8.0),
            (-2.0, 4.0, 16.0),
            (0.0, 3.0, 0.0),
            (1.0, 100000.0, 1.0),
        ]

        for base, exponent, expected in cases:
            with self.subTest(base=base, exponent=exponent):
                self.assert_close_ar001(hybrid_power(base, exponent), expected)

    def test_valid_non_integer_positive_base_cases(self) -> None:
        cases = [
            (4.0, 0.5, 2.0),
            (16.0, 0.25, 2.0),
            (9.0, 0.5, 3.0),
            (27.0, 1.0 / 3.0, 3.0),
        ]

        for base, exponent, expected in cases:
            with self.subTest(base=base, exponent=exponent):
                self.assert_close_ar001(hybrid_power(base, exponent), expected)

    def test_invalid_domain_cases(self) -> None:
        invalid_cases = [
            (0.0, 0.0),
            (0.0, -1.0),
            (-2.0, 0.5),
            (-8.0, 1.0 / 3.0),
        ]

        for base, exponent in invalid_cases:
            with self.subTest(base=base, exponent=exponent):
                with self.assertRaises(DomainError):
                    hybrid_power(base, exponent)

    def test_invalid_input_cases(self) -> None:
        invalid_values = [float("nan"), float("inf"), float("-inf")]

        for value in invalid_values:
            with self.subTest(value=value):
                with self.assertRaises(DomainError):
                    validate_finite_number(value, "value")
                with self.assertRaises(DomainError):
                    hybrid_power(value, 2.0)
                with self.assertRaises(DomainError):
                    hybrid_power(2.0, value)

    def test_range_error_is_controlled(self) -> None:
        with self.assertRaises(NumericRangeError):
            hybrid_power(10.0, 1000.0)
        with self.assertRaises(NumericRangeError):
            hybrid_power(1e308, 2.0)

    def test_underflow_is_controlled(self) -> None:
        with self.assertRaises(NumericRangeError) as context:
            hybrid_power(1e-300, 2.0)
        self.assertIn("too small to represent", str(context.exception))


if __name__ == "__main__":
    unittest.main()
