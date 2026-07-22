"""Tkinter power calculator with from-scratch numerical algorithms.

The calculation layer is independent of the graphical interface so it can be
imported and tested without creating a window.
"""

from __future__ import annotations

import tkinter as tk
from tkinter import ttk


LN_2 = 0.6931471805599453
MAX_FLOAT = 1.7976931348623157e308
MIN_NORMAL = 2.2250738585072014e-308
SERIES_TOLERANCE = 1e-16
MAX_SERIES_ITERATIONS = 1000
MAX_RANGE_REDUCTIONS = 2048


class PowerCalculatorError(Exception):
    """Base class for expected calculator errors."""


class InvalidInputError(PowerCalculatorError):
    """Raised when entered text is not a supported finite number."""


class UnsupportedDomainError(PowerCalculatorError):
    """Raised when a base/exponent combination has no supported real result."""


class NumericRangeError(PowerCalculatorError):
    """Raised when a result overflows or severely underflows."""


class ConvergenceError(PowerCalculatorError):
    """Raised when an iterative approximation does not converge."""


def absolute_value(value: float) -> float:
    """Return the non-negative magnitude of value."""
    return -value if value < 0.0 else value


def is_nan(value: float) -> bool:
    """Detect NaN using its unequal-to-itself property."""
    return value != value


def is_finite_number(value: float) -> bool:
    """Return whether value is neither NaN nor infinity."""
    return not is_nan(value) and -MAX_FLOAT <= value <= MAX_FLOAT


def is_integer_value(value: float) -> bool:
    """Return whether a finite floating-point value is integer-valued."""
    if not is_finite_number(value):
        return False
    return value == int(value)


def _checked_multiply(left: float, right: float) -> float:
    """Multiply while detecting overflow and severe underflow."""
    if left == 0.0 or right == 0.0:
        return 0.0

    left_size = absolute_value(left)
    right_size = absolute_value(right)
    if left_size > MAX_FLOAT / right_size:
        raise NumericRangeError(
            "The result is too large to be represented by this calculator."
        )

    result = left * right
    if absolute_value(result) < MIN_NORMAL:
        raise NumericRangeError(
            "The result is too small to be represented accurately by this "
            "calculator."
        )
    return result


def power_by_squaring(base: float, exponent: int) -> float:
    """Evaluate an integer power in logarithmic time using multiplication."""
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
    factor = float(base)
    result = 1.0

    while remaining > 0:
        if remaining % 2 == 1:
            result = _checked_multiply(result, factor)
        remaining //= 2
        if remaining > 0:
            factor = _checked_multiply(factor, factor)

    if not negative_exponent:
        return result

    reciprocal = 1.0 / result
    if reciprocal == 0.0 or absolute_value(reciprocal) < MIN_NORMAL:
        raise NumericRangeError(
            "The result is too small to be represented accurately by this "
            "calculator."
        )
    return reciprocal


def natural_log(value: float) -> float:
    """Approximate the natural logarithm for a positive finite value.

    Range reduction writes the input as a mantissa times a power of two. The
    mantissa logarithm uses the odd atanh series, whose powers are updated by
    multiplication rather than a built-in power operation.
    """
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
        if reductions > MAX_RANGE_REDUCTIONS:
            raise ConvergenceError(
                "The calculation did not converge within the supported "
                "number of iterations."
            )
    while mantissa < 0.75:
        mantissa *= 2.0
        scale -= 1
        reductions += 1
        if reductions > MAX_RANGE_REDUCTIONS:
            raise ConvergenceError(
                "The calculation did not converge within the supported "
                "number of iterations."
            )

    z = (mantissa - 1.0) / (mantissa + 1.0)
    z_squared = z * z
    term = z
    total = 0.0
    denominator = 1

    for _ in range(MAX_SERIES_ITERATIONS):
        addition = term / denominator
        total += addition
        if absolute_value(addition) <= (
            SERIES_TOLERANCE * (1.0 + absolute_value(total))
        ):
            return 2.0 * total + scale * LN_2
        term *= z_squared
        denominator += 2

    raise ConvergenceError(
        "The calculation did not converge within the supported number of "
        "iterations."
    )


def exponential(value: float) -> float:
    """Approximate the exponential using range reduction and a Taylor series."""
    if not is_finite_number(value):
        raise NumericRangeError(
            "The result is outside the supported finite numeric range."
        )

    quotient = value / LN_2
    scale = int(quotient + 0.5) if quotient >= 0.0 else int(quotient - 0.5)
    remainder = value - scale * LN_2

    term = 1.0
    total = 1.0
    for index in range(1, MAX_SERIES_ITERATIONS + 1):
        term = term * remainder / index
        total += term
        if absolute_value(term) <= (
            SERIES_TOLERANCE * absolute_value(total)
        ):
            if scale > 1023:
                raise NumericRangeError(
                    "The result is too large to be represented by this "
                    "calculator."
                )
            if scale < -1022:
                raise NumericRangeError(
                    "The result is too small to be represented accurately by "
                    "this calculator."
                )
            scale_factor = power_by_squaring(2.0, scale)
            return _checked_multiply(total, scale_factor)

    raise ConvergenceError(
        "The calculation did not converge within the supported number of "
        "iterations."
    )


def calculate_power(base: float, exponent: float) -> float:
    """Evaluate a supported real power using the hybrid algorithm."""
    if not is_finite_number(base) or not is_finite_number(exponent):
        raise InvalidInputError(
            "NaN and infinity are not supported. Please enter a finite number."
        )

    exponent_is_integer = is_integer_value(exponent)
    if base == 0.0:
        if exponent == 0.0:
            raise UnsupportedDomainError(
                "The expression 0^0 is undefined. Please enter a positive "
                "exponent when the base is zero."
            )
        if exponent < 0.0:
            raise UnsupportedDomainError(
                "Zero cannot be raised to a negative exponent."
            )
        return 0.0

    if base < 0.0 and not exponent_is_integer:
        raise UnsupportedDomainError(
            "A negative base requires an integer exponent because this "
            "calculator returns real-valued results only."
        )

    if exponent == 0.0 or base == 1.0:
        return 1.0
    if exponent_is_integer:
        return power_by_squaring(base, int(exponent))

    logarithm = natural_log(base)
    product = exponent * logarithm
    if not is_finite_number(product):
        if (exponent > 0.0) == (logarithm > 0.0):
            raise NumericRangeError(
                "The result is too large to be represented by this calculator."
            )
        raise NumericRangeError(
            "The result is too small to be represented accurately by this "
            "calculator."
        )
    return exponential(product)


def parse_number(text: str, field_name: str) -> float:
    """Parse one GUI field and give a field-specific validation message."""
    try:
        value = float(text.strip())
    except ValueError as error:
        raise InvalidInputError(
            f"Please enter a numeric value for the {field_name}."
        ) from error
    if not is_finite_number(value):
        raise InvalidInputError(
            "NaN and infinity are not supported. Please enter a finite number."
        )
    return value


def format_result(value: float) -> str:
    """Format a result with enough precision for meaningful reuse."""
    return format(value, ".15g")


class PowerCalculatorApp:
    """Simple Tkinter interface for the independent calculation functions."""

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        root.title("Power Function Calculator")
        root.resizable(False, False)

        frame = ttk.Frame(root, padding=24)
        frame.grid(row=0, column=0)
        frame.columnconfigure(1, weight=1)

        ttk.Label(
            frame, text="Power Function Calculator", font=("TkDefaultFont", 16, "bold")
        ).grid(row=0, column=0, columnspan=2, pady=(0, 4))
        ttk.Label(frame, text="Compute x raised to the power y").grid(
            row=1, column=0, columnspan=2, pady=(0, 18)
        )

        ttk.Label(frame, text="Base x:").grid(row=2, column=0, sticky="w", pady=5)
        self.base_entry = ttk.Entry(frame, width=28)
        self.base_entry.grid(row=2, column=1, sticky="ew", padx=(12, 0), pady=5)

        ttk.Label(frame, text="Exponent y:").grid(row=3, column=0, sticky="w", pady=5)
        self.exponent_entry = ttk.Entry(frame, width=28)
        self.exponent_entry.grid(row=3, column=1, sticky="ew", padx=(12, 0), pady=5)

        buttons = ttk.Frame(frame)
        buttons.grid(row=4, column=0, columnspan=2, pady=16)
        ttk.Button(buttons, text="Calculate", command=self.calculate).grid(row=0, column=0, padx=4)
        ttk.Button(buttons, text="Clear", command=self.clear).grid(row=0, column=1, padx=4)
        ttk.Button(buttons, text="Exit", command=root.destroy).grid(row=0, column=2, padx=4)

        ttk.Label(frame, text="Result:").grid(row=5, column=0, sticky="nw")
        self.result_text = tk.StringVar()
        ttk.Label(
            frame, textvariable=self.result_text, relief="sunken", anchor="w", width=32
        ).grid(row=5, column=1, sticky="ew", padx=(12, 0), ipady=5)

        ttk.Label(frame, text="Status:").grid(row=6, column=0, sticky="nw", pady=(12, 0))
        self.status_text = tk.StringVar(value="Enter a base and exponent.")
        self.status_label = ttk.Label(
            frame, textvariable=self.status_text, wraplength=300, justify="left"
        )
        self.status_label.grid(row=6, column=1, sticky="w", padx=(12, 0), pady=(12, 0))

        root.bind("<Return>", self.calculate)
        self.base_entry.focus_set()

    def calculate(self, _event: tk.Event | None = None) -> None:
        """Validate both fields, calculate, and keep the GUI responsive."""
        self.result_text.set("")
        try:
            base = parse_number(self.base_entry.get(), "base x")
            exponent = parse_number(self.exponent_entry.get(), "exponent y")
            result = calculate_power(base, exponent)
        except PowerCalculatorError as error:
            self.status_text.set(f"Error: {error}")
            return

        self.result_text.set(format_result(result))
        self.status_text.set("Calculation completed successfully.")

    def clear(self) -> None:
        """Reset all fields and return keyboard focus to the base."""
        self.base_entry.delete(0, tk.END)
        self.exponent_entry.delete(0, tk.END)
        self.result_text.set("")
        self.status_text.set("Enter a base and exponent.")
        self.base_entry.focus_set()


def main() -> None:
    """Create and run the graphical application."""
    root = tk.Tk()
    PowerCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
