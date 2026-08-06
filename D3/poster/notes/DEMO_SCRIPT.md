# Deliverable 3 Demonstration Script

Target duration: approximately 3–5 minutes.

1. Launch the GUI:

   ```text
   python power_calculator.py
   ```

2. Show a normal integer exponent: `2^3 = 8`.
3. Show a negative exponent: `2^-3 = 0.125`.
4. Show a decimal exponent: `4^0.5 = 2`.
5. Show a negative base with an integer exponent: `(-2)^3 = -8`.
6. Show the rejected domain case `(-2)^0.5` and its specific message.
7. Show the zero boundary `0^0` and its specific message.
8. Demonstrate accessibility:
   - use Tab to move between controls;
   - press Enter to calculate; and
   - press Escape to clear.
9. Run the tests:

   ```text
   python -m unittest test_power_calculator.py -v
   ```

10. Point out the verified tool evidence:
    - Flake8: no violations;
    - Pylint: 10.00/10; and
    - PyUnit: 34 tests passed.
11. Explain the D2 regression correction:
    - a valid large finite result is accepted; and
    - a genuine overflow is rejected.

Keep transitions brief and prioritize readable, real evidence over showing
every test case individually.
