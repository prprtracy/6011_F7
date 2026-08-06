"""PyUnit tests for the calculator parsing and numeric layers."""

# Descriptive test names already document each scenario; repeating every name
# in a method docstring would add noise without useful information.
# pylint: disable=missing-function-docstring
# unittest requires public discovery methods, and this complete suite has more
# than the general-purpose class limit of 20.
# pylint: disable=too-many-public-methods

import math
import unittest

from power_calculator import (
    InvalidInputError,
    NumericRangeError,
    ResultOverflowError,
    UnsupportedDomainError,
    calculate_power,
    parse_numeric_input,
    power_by_squaring,
)


class TestPowerCalculator(unittest.TestCase):
    """Verify parsing, calculations, and documented error policies."""

    def test_parse_valid_numeric_text(self) -> None:
        cases = (("2", 2.0), ("4.5", 4.5), ("-3.25", -3.25))
        for text, expected in cases:
            with self.subTest(text=text):
                self.assertEqual(parse_numeric_input(text, "Base"), expected)

    def test_parse_strips_surrounding_whitespace(self) -> None:
        self.assertEqual(parse_numeric_input("  2.5  ", "Base"), 2.5)

    def test_parse_empty_base_raises_invalid_input_error(self) -> None:
        with self.assertRaisesRegex(InvalidInputError, "Base is required"):
            parse_numeric_input("", "Base")

    def test_whitespace_exponent_raises_invalid_input_error(self) -> None:
        with self.assertRaisesRegex(InvalidInputError, "Exponent is required"):
            parse_numeric_input("   ", "Exponent")

    def test_parse_invalid_base_text_raises_invalid_input_error(self) -> None:
        with self.assertRaisesRegex(
            InvalidInputError, "Base must be a valid numeric value"
        ):
            parse_numeric_input("abc", "Base")

    def test_invalid_exponent_text_raises_invalid_input_error(self) -> None:
        with self.assertRaisesRegex(
            InvalidInputError, "Exponent must be a valid numeric value"
        ):
            parse_numeric_input("2x", "Exponent")

    def test_parse_nan_raises_invalid_input_error(self) -> None:
        with self.assertRaises(InvalidInputError):
            parse_numeric_input("nan", "Base")

    def test_parse_positive_infinity_raises_invalid_input_error(self) -> None:
        with self.assertRaises(InvalidInputError):
            parse_numeric_input("inf", "Base")

    def test_parse_negative_infinity_raises_invalid_input_error(self) -> None:
        with self.assertRaises(InvalidInputError):
            parse_numeric_input("-inf", "Base")

    def test_positive_integer_exponent(self) -> None:
        self.assertEqual(calculate_power(2.0, 3.0), 8.0)

    def test_negative_integer_exponent(self) -> None:
        self.assertEqual(calculate_power(2.0, -3.0), 0.125)

    def test_zero_exponent(self) -> None:
        self.assertEqual(calculate_power(5.0, 0.0), 1.0)

    def test_base_one(self) -> None:
        self.assertEqual(calculate_power(1.0, 12345.0), 1.0)

    def test_negative_base_with_odd_integer_exponent(self) -> None:
        self.assertEqual(calculate_power(-2.0, 3.0), -8.0)

    def test_negative_base_with_even_integer_exponent(self) -> None:
        self.assertEqual(calculate_power(-2.0, 4.0), 16.0)

    def test_negative_base_with_negative_odd_exponent(self) -> None:
        self.assertAlmostEqual(calculate_power(-2.0, -3.0), -0.125)

    def test_zero_base_with_positive_exponent(self) -> None:
        self.assertEqual(calculate_power(0.0, 3.0), 0.0)

    def test_power_by_squaring_positive_exponent(self) -> None:
        self.assertEqual(power_by_squaring(3.0, 4), 81.0)

    def test_power_by_squaring_negative_exponent(self) -> None:
        self.assertEqual(power_by_squaring(4.0, -2), 0.0625)

    def test_square_root_through_decimal_path(self) -> None:
        self.assertAlmostEqual(calculate_power(4.0, 0.5), 2.0, places=12)

    def test_cube_root_through_decimal_path(self) -> None:
        self.assertAlmostEqual(
            calculate_power(8.0, 1.0 / 3.0), 2.0, places=12
        )

    def test_positive_decimal_exponent(self) -> None:
        self.assertAlmostEqual(calculate_power(9.0, 1.5), 27.0, places=11)

    def test_negative_decimal_exponent(self) -> None:
        self.assertAlmostEqual(calculate_power(4.0, -0.5), 0.5, places=12)

    def test_fractional_exponent_with_base_below_one(self) -> None:
        self.assertAlmostEqual(calculate_power(0.25, 0.5), 0.5, places=12)

    def test_zero_to_zero_raises_unsupported_domain_error(self) -> None:
        with self.assertRaisesRegex(
            UnsupportedDomainError, r"0\^0 is undefined"
        ):
            calculate_power(0.0, 0.0)

    def test_zero_to_negative_exponent_raises_domain_error(self) -> None:
        with self.assertRaisesRegex(
            UnsupportedDomainError, "negative exponent"
        ):
            calculate_power(0.0, -3.0)

    def test_negative_fractional_power_raises_domain_error(self) -> None:
        with self.assertRaisesRegex(
            UnsupportedDomainError, "requires an integer exponent"
        ):
            calculate_power(-2.0, 0.5)

    def test_negative_base_cube_root_raises_domain_error(self) -> None:
        with self.assertRaises(UnsupportedDomainError):
            calculate_power(-8.0, 1.0 / 3.0)

    def test_non_finite_base_raises_invalid_input_error(self) -> None:
        for base in (float("nan"), float("inf")):
            with self.subTest(base=base):
                with self.assertRaises(InvalidInputError):
                    calculate_power(base, 2.0)

    def test_non_finite_exponent_raises_invalid_input_error(self) -> None:
        for exponent in (float("nan"), float("inf")):
            with self.subTest(exponent=exponent):
                with self.assertRaises(InvalidInputError):
                    calculate_power(2.0, exponent)

    def test_large_finite_result_is_not_classified_as_overflow(self) -> None:
        result = calculate_power(1.0e150, 2.0)
        self.assertTrue(math.isfinite(result))
        self.assertTrue(math.isclose(result, 1.0e300, rel_tol=1.0e-15))

    def test_true_overflow_raises_result_overflow_error(self) -> None:
        with self.assertRaisesRegex(
            ResultOverflowError, "exceeds the supported numeric range"
        ):
            calculate_power(1.0e200, 2.0)

    def test_extreme_negative_power_triggers_underflow_policy(self) -> None:
        with self.assertRaisesRegex(NumericRangeError, "too small"):
            calculate_power(10.0, -400.0)

    def test_small_normal_result_is_accepted(self) -> None:
        result = calculate_power(1.0e-153, 2.0)
        self.assertTrue(math.isfinite(result))
        self.assertTrue(math.isclose(result, 1.0e-306, rel_tol=1.0e-15))


if __name__ == "__main__":
    unittest.main()
