"""Terminal user interface for the SOEN 6011 power calculator.

Requirement coverage:
- IR-001, UR-001, UR-002: plain-language textual prompts for x and y.
- IR-004, ER-004: invalid input is handled without a traceback.
- OR-001: results are displayed with a clear label.
- UR-003: repeated calculations continue until the user exits.
"""

from __future__ import annotations

import math

from src.power_calculator import DomainError, NumericRangeError, hybrid_power


EXIT_COMMANDS = {"q", "quit", "exit"}


def read_finite_float(prompt: str) -> float | None:
    """Read one finite float from the terminal, or None for an exit command."""
    while True:
        raw_value = input(prompt).strip()
        if raw_value.lower() in EXIT_COMMANDS:
            return None
        if raw_value == "":
            print("Error: the base and exponent must be numeric values.")
            continue

        try:
            value = float(raw_value)
        except ValueError:
            print("Error: the base and exponent must be numeric values.")
            continue

        if not math.isfinite(value):
            print("Error: NaN and infinity are not supported.")
            continue

        return value


def ask_to_continue() -> bool:
    """Ask whether the user wants another calculation."""
    while True:
        answer = input(
            "Would you like to perform another calculation? (y/n): "
        ).strip().lower()

        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"} | EXIT_COMMANDS:
            return False

        print("Please enter y to continue or n to exit.")


def format_result(result: float) -> str:
    """Format a finite result without hiding useful precision."""
    return format(result, ".12g")


def main() -> None:
    """Run the textual calculator until the user exits."""
    print("Power Function Calculator: x^y")
    print("Enter finite numeric values. Type q, quit, or exit to leave.")

    while True:
        base = read_finite_float("Enter the base x: ")
        if base is None:
            break

        exponent = read_finite_float("Enter the exponent y: ")
        if exponent is None:
            break

        try:
            result = hybrid_power(base, exponent)
        except DomainError as error:
            print(f"Error: {error}")
        except NumericRangeError as error:
            print(f"Error: {error}")
        else:
            print(f"Result: {format_result(result)}")

        print()
        if not ask_to_continue():
            break
        print()

    print("Goodbye.")


if __name__ == "__main__":
    main()
