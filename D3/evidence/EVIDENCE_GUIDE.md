# Deliverable 3 Evidence Guide

Run terminal commands from the `D3` directory. Capture real screenshots only;
do not edit terminal output or create substitute images.

## A. Flake8 Screenshot

Run in PowerShell:

```powershell
flake8 power_calculator.py test_power_calculator.py
if ($LASTEXITCODE -eq 0) {
    Write-Output "Flake8 completed successfully - no PEP 8 violations found."
}
```

The screenshot must include the command, both filenames, and the visible
success message. Crop it closely while keeping the text readable. Save it as:

```text
evidence/flake8/flake8_success.png
```

## B. Pylint Screenshot

Run:

```powershell
pylint --persistent=no power_calculator.py test_power_calculator.py
```

Include the command, both filenames, and the final `10.00/10` line. Save it as:

```text
evidence/pylint/pylint_10.png
```

Persistence is disabled only because the environment may not permit writing
the optional Pylint cache. It does not disable code checks.

## C. PyUnit Screenshot

Run:

```powershell
python -m unittest test_power_calculator.py -v
```

Include the command, representative test names, and both D2 regression tests:

```text
test_large_finite_result_is_not_classified_as_overflow
test_true_overflow_raises_result_overflow_error
```

The final lines must visibly show `Ran 34 tests` and `OK`. If one image cannot
show readable test names and the summary, take readable cropped images rather
than shrinking the terminal. Save the primary image as:

```text
evidence/unittest/unittest_34_passed.png
```

## D. Debugger Screenshots

Use the VS Code Python debugger with the negative exponent case:

```text
base = 2
exponent = -3
```

1. Open `power_calculator.py` and `test_power_calculator.py` in VS Code.
2. Add breakpoints inside `calculate_power()`, at the
   `exponent_is_integer` assignment, at the entry to
   `power_by_squaring()`, inside its negative-exponent branch, and before its
   final return.
3. In the Testing panel, debug `test_negative_integer_exponent`.
4. At the first stops, show `base = 2.0`, `exponent = -3.0`, and
   `exponent_is_integer = True` in the Variables panel.
5. Continue into `power_by_squaring()` and step over reciprocal handling. Show
   `factor = 0.5` or the corresponding `remaining` value.
6. Continue to the return and show `result = 0.125`.
7. Keep the source, Variables panel, and Call Stack readable in each capture.

Do not insert `pdb.set_trace()` in the submitted program. Save the real images
as:

```text
evidence/debugger/debugger_integer_check.png
evidence/debugger/debugger_negative_exponent.png
evidence/debugger/debugger_final_result.png
```

## E. GUI Screenshots

Launch the application with `python power_calculator.py`, then capture these
real cases:

1. Enter base `2` and exponent `-3`; calculate and show result `0.125`. Save as
   `evidence/gui/gui_negative_exponent.png`.
2. Enter base `-2` and exponent `0.5`; show the specific unsupported-domain
   message. Save as `evidence/gui/gui_domain_error.png`.
3. Enter base `0` and exponent `0`; show the `0^0` error. Save as
   `evidence/gui/gui_zero_zero_error.png`.
4. Capture the visible labels, status message, version number, and keyboard
   focus where possible. Save as `evidence/gui/gui_accessibility.png`.

For accessibility evidence, also manually confirm Tab navigation, Enter to
calculate, and Escape to clear. Use readable crops and do not obscure labels.

## F. UIDP Mind Map

Use this center node:

```text
Power Function Calculator GUI
```

Connect each applied principle to real GUI evidence:

- **Consistency** — consistent labels, button layout, and status messages.
- **Visibility** — visible Base, Exponent, Result, and Status labels.
- **Feedback** — success messages, specific errors, immediate result display.
- **Error Prevention** — empty-input, invalid-number, and domain validation.
- **Affordance** — clearly clickable buttons and editable text fields.
- **Simplicity** — a one-screen workflow without unnecessary menus.

Add an accessibility branch containing Tab navigation, Enter to calculate,
Escape to clear, readable text, and errors that do not rely on color alone.

Mark these principles as limited or not applicable:

- Undo/Redo
- Advanced shortcuts
- Complex navigation

Export the completed, readable mind map as:

```text
evidence/uidp/uidp_mind_map.png
```

This guide does not claim that any screenshot or mind-map image already
exists; each must be captured or exported manually from real evidence.
