CONTEXT

I am completing Delivery 2 of an individual SOEN 6011 Software Engineering
Processes project at Concordia University.

My assigned function is:

    F7: x^y

Delivery 1 already established:

- a goal-directed persona;
- a supported real-valued mathematical domain;
- ISO/IEC/IEEE 29148-style requirements;
- two candidate algorithms;
- selection of a Hybrid Power Evaluation algorithm;
- a Python textual user interface.

The selected D1 algorithm uses:

1. exponentiation by squaring for integer-valued exponents;
2. the identity x^y = exp(y * ln(x)) for positive bases with
   non-integer exponents.

Delivery 2 must extend the D1 implementation instead of redesigning the
project from the beginning.

The D2 implementation must be written from scratch in Python. Apart from
operations related to input, output, arithmetic, iteration, exception
handling, and graphical user-interface design, it must not use Python
built-in or library mathematical functions to perform the power,
logarithm, or exponential evaluation.

The application must use a Tkinter graphical user interface, provide
exception handling, display helpful error messages, run independently
of any particular IDE, be stored in a public Git repository, include a
README file, use meaningful commit messages, and provide an updated
requirements list.

The public repository is:

    https://github.com/prprtracy/6011_F7.git


AUDIENCE

The primary audience consists of:

- the SOEN 6011 professor;
- the teaching assistant evaluating Delivery 2;
- software engineering students reviewing the implementation;
- a fictional second-year engineering student named Alex Chen, who
  requires clear inputs, understandable outputs, and helpful error
  messages.

The response must use technically accurate but accessible language.
Avoid unexplained mathematical or programming jargon.


SCOPE

Work only on Delivery 2 Problems 5, 6, and 7.

Problem 5 scope:

- modify the D1 implementation;
- implement x^y from scratch;
- preserve the supported real-valued domain;
- use Tkinter;
- include exception handling;
- provide helpful error messages;
- avoid built-in mathematical power, logarithm, and exponential
  operations;
- ensure the calculation layer can run without dependence on an IDE.

Problem 6 scope:

- organize the source code in a public GitHub repository;
- include the repository address;
- include a complete README;
- use high-quality commit messages;
- preserve D1 and D2 in separate directories.

Problem 7 scope:

- revise the D1 requirements based on the D2 implementation;
- use uniquely identified ISO/IEC/IEEE 29148-style requirements;
- preserve traceability between implementation decisions and
  requirements.

Do not work on Delivery 3 requirements such as Flake8, Pylint, pdb,
Semantic Versioning, accessibility evaluation, or unit testing unless
they are only mentioned as future work.


TASKS

Complete the following tasks.

TASK 1 — INSPECT THE EXISTING PROJECT

Inspect the D1 implementation and documentation before making changes.

Identify:

- the existing supported domain;
- the selected algorithm;
- the current input validation;
- the existing error handling;
- the D1 requirements affected by the D2 changes.

Do not delete, overwrite, rename, or unnecessarily modify D1 files.


TASK 2 — IMPLEMENT INTEGER EXPONENTS FROM SCRATCH

Implement integer-valued exponents using exponentiation by squaring.

The implementation must:

- support positive integer exponents;
- support zero exponents;
- support negative integer exponents;
- support negative bases when the exponent is integer-valued;
- use multiplication, division, comparison, modulo, integer division,
  and loops;
- require O(log |y|) loop iterations;
- detect overflow and severe underflow;
- not use pow(), math.pow(), or the ** operator.


TASK 3 — IMPLEMENT NON-INTEGER EXPONENTS FROM SCRATCH

For a positive base and a non-integer exponent, calculate:

    x^y = exp(y * ln(x))

Implement both ln(x) and exp(x) from scratch.

For natural_log():

- require a positive finite input;
- use range reduction based on powers of two;
- reduce the mantissa to a range suitable for convergence;
- use an iterative logarithmic series;
- update powers through multiplication rather than built-in
  exponentiation;
- use a convergence tolerance;
- use a maximum iteration limit;
- raise a clear convergence exception if necessary.

For exponential():

- use range reduction based on ln(2);
- express the value as k * ln(2) + r;
- approximate exp(r) using an iterative Taylor series;
- calculate each new term from the previous term;
- restore the scale using a custom integer-power function;
- detect overflow and severe underflow;
- use a convergence tolerance and maximum iteration limit.


TASK 4 — PRESERVE THE SUPPORTED DOMAIN

Preserve this real-valued domain:

Positive base:

    x > 0

Support finite integer-valued and finite non-integer decimal exponents.

Zero base:

    x = 0

Support only y > 0.

Reject:

    0^0
    zero raised to a negative exponent

Negative base:

    x < 0

Support only integer-valued exponents.

Reject negative bases with non-integer exponents.

Return real-valued results only.

Reject:

- non-numeric input;
- NaN;
- positive and negative infinity;
- unsupported domain combinations;
- overflow;
- severe underflow;
- convergence failure.


TASK 5 — IMPLEMENT EXCEPTION HANDLING

Create a clear custom exception hierarchy similar to:

    PowerCalculatorError
    InvalidInputError
    UnsupportedDomainError
    NumericRangeError
    ConvergenceError

Use specific exceptions.

Do not use a bare except clause.

Expected input and domain errors must not terminate the GUI.

Unexpected programming errors must not be silently hidden.


TASK 6 — CREATE THE TKINTER GUI

Create a Tkinter application containing:

- a title;
- a short explanation;
- a labelled input field for base x;
- a labelled input field for exponent y;
- a Calculate button;
- a Clear button;
- an Exit button;
- a clearly labelled result field;
- a separate status or error-message area.

Required behavior:

Calculate:

- parse both inputs;
- validate the inputs;
- calculate the result;
- display the formatted result;
- display helpful errors without closing the application.

Clear:

- clear both input fields;
- clear the result;
- restore the default status;
- return focus to the base field.

Exit:

- close the application normally.

The Enter key should perform the calculation.

The calculation functions must be importable without automatically
launching the GUI.

Use:

    if __name__ == "__main__":

to control application startup.


TASK 7 — PROVIDE HELPFUL ERROR MESSAGES

Use plain-language, field-specific messages.

Examples:

    Please enter a numeric value for the base x.

    Please enter a numeric value for the exponent y.

    NaN and infinity are not supported. Please enter a finite number.

    The expression 0^0 is undefined. Please enter a positive exponent
    when the base is zero.

    Zero cannot be raised to a negative exponent.

    A negative base requires an integer exponent because this calculator
    returns real-valued results only.

    The result is too large to be represented by this calculator.

    The result is too small to be represented accurately by this
    calculator.

    The calculation did not converge within the supported number of
    iterations.

Do not display only “Math Error” or an unexplained Python traceback.


TASK 8 — VERIFY THE IMPLEMENTATION

Verify representative valid cases:

    2^3 = 8
    2^-10 = 0.0009765625
    4^0.5 ≈ 2
    16^0.25 ≈ 2
    (-2)^3 = -8
    (-2)^4 = 16
    (-2)^-3 = -0.125
    0^3 = 0
    5^0 = 1
    0.25^0.5 ≈ 0.5

Verify invalid cases:

    0^0
    0^-1
    (-2)^0.5
    abc as the base
    abc as the exponent
    NaN
    infinity
    overflow
    severe underflow

After each invalid case, confirm that:

- the GUI remains open;
- the result field is cleared;
- a helpful message appears;
- the user can correct the input and calculate again.


TASK 9 — VERIFY PROHIBITED MATHEMATICAL OPERATIONS

Confirm that the production calculation code does not use:

    pow()
    math.pow()
    **
    math.log()
    math.exp()
    math.isfinite()
    numpy
    scipy
    decimal
    fractions
    sympy
    cmath
    eval()

Tkinter is allowed.

Input conversion, output formatting, basic arithmetic, comparison,
iteration, and exception handling may be used where required.

Do not make the inaccurate claim that no Python built-in functions are
used at all.

Use this precise statement:

    No built-in mathematical power, logarithm, or exponential operation
    is used to evaluate x raised to y.


TASK 10 — ORGANIZE THE GITHUB REPOSITORY

Use this repository:

    https://github.com/prprtracy/6011_F7.git

Preserve D1.

Use a structure similar to:

    D1/
    D2/
        power_calculator.py
        README.md
        IMPLEMENTATION.md
        screenshots/
            README.md
            verification images
    .gitignore
    README.md

Do not rewrite existing Git history.

Do not amend, squash, rebase, or force-push existing commits.

Use real and meaningful changes for each commit.


TASK 11 — USE HIGH-QUALITY COMMIT MESSAGES

Use concise imperative commit messages describing actual changes.

Suitable examples:

    Add Python and editor files to gitignore

    Improve D2 README and execution instructions

    Document D2 architecture and numerical limitations

    Document D2 GUI verification evidence

Avoid vague messages such as:

    update
    fix
    changes
    final
    D2 update


TASK 12 — WRITE THE README

Ensure D2/README.md includes:

- project title;
- course and deliverable;
- assigned function;
- supported real-valued domain;
- from-scratch implementation;
- exponentiation by squaring;
- custom logarithm;
- custom exponential;
- Tkinter GUI behavior;
- exception handling;
- execution instructions;
- representative test cases;
- known numerical limitations;
- repository structure.

Execution instructions:

    cd D2
    python power_calculator.py

State that Tkinter support is required.

Document honestly that:

- subnormal results below the minimum supported normal magnitude are
  rejected;
- extremely large floating-point values are limited by binary
  floating-point precision;
- the implementation returns real-valued results only.


TASK 13 — UPDATE THE REQUIREMENTS

Revise D1 requirements using the ISO/IEC/IEEE 29148-style structure:

    The system shall ...

Assign every requirement a unique identifier.

Include requirements covering:

- from-scratch computation;
- the supported real-valued domain;
- finite numeric inputs;
- integer-valued exponent detection;
- Tkinter GUI;
- Calculate, Clear, and Exit controls;
- Enter-key calculation;
- labelled output;
- helpful error messages;
- recovery after invalid input;
- overflow detection;
- severe underflow detection;
- convergence failure;
- prohibition of built-in mathematical power, logarithm, and
  exponential operations;
- accuracy for representative verified cases.

For every requirement, provide:

- identifier;
- requirement statement;
- source or rationale;
- verification method;
- D1 status: retained, modified, or new.

Maintain traceability:

    Persona or D2 constraint
        → requirement
        → implementation element
        → verification evidence


RESTRICTIONS

Do not:

- delete D1;
- narrow the domain without explanation;
- claim support for complex-valued results;
- use a built-in mathematical power, logarithm, or exponential
  operation;
- use external numerical libraries;
- use eval();
- hide errors with a bare except;
- invent verification results;
- invent screenshots;
- invent Git commits;
- claim that code was tested if it was not executed;
- claim that all possible floating-point values are supported;
- include Delivery 3 work as completed D2 work;
- copy external content verbatim without attribution.


OUTPUT FORMAT

Return the result in the following structure:

1. Existing D1 design inspected
2. D2 implementation summary
3. Files created or modified
4. From-scratch numerical algorithms
5. Tkinter GUI design
6. Exception hierarchy
7. Supported-domain behavior
8. Verification results
9. Prohibited-operation check
10. GitHub repository organization
11. Commit messages created or recommended
12. README summary
13. Complete updated requirements
14. Requirements-to-code traceability
15. Known numerical limitations
16. Remaining manual actions

Use tables where they improve clarity.

Keep all claims evidence-based.


FORMAT AND STYLE

Use professional software-engineering language.

Use concise explanations suitable for presentation slides and technical
documentation.

Use mathematical notation where appropriate.

Use Python identifiers exactly as they appear in the source code.

Clearly distinguish:

- implemented behavior;
- verified behavior;
- design decisions;
- assumptions;
- known limitations.

Do not present GAI output as authoritative.
Mark anything requiring student confirmation.


FINAL REVIEW

Before finishing:

- compare the result against every D2 requirement;
- confirm that Problem 5, Problem 6, and Problem 7 are all covered;
- confirm that the proposed requirements match the actual code;
- confirm that no unsupported claim is made;
- identify anything that still requires manual verification;
- provide a concise final compliance checklist.