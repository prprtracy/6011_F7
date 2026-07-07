# Delivery 1 CASTROFF-Based GAI Prompt

## CASTROFF Mapping

* **Constraints**: Follow the SOEN 6011 D1 project scope only. The work must be completed individually. The assigned function is F7: (x^y), where (x) and (y) are real variables. Use LaTeX-ready structure. Make assumptions explicit. Avoid unsupported claims. Do not copy external text verbatim. Include citation needs for all non-original work. Keep the implementation simple enough for D1 and suitable for later D2 modification. Do not apply D2 from-scratch implementation or GUI requirements to D1.
* **Audience**: SOEN 6011 course instructor and evaluator during a Zoom presentation and D1 demonstration.
* **Structure**: Organize output by D1 Problem 1, Problem 2, Problem 3, Problem 4, plus assumptions, GAI use explanation, citations, and validation checklist.
* **Tone**: Academic, concise, evidence-based, and presentation-ready.
* **Role**: Act as a software engineering analyst, requirements analyst, and scientific calculator design assistant for scientific computing software supporting the function (x^y).
* **Output format**: Markdown tables and lists; include Mermaid or text-based mind maps where useful; include language-independent pseudocode; include Python code for a textual user interface.
* **Focus**: Persona creation, ISO/IEC/IEEE 29148-style requirements, two algorithms for (x^y), algorithm selection using a mind map, and Python textual user interface implementation.
* **Function**: Brainstorm and organize a first draft, not produce final unverified submission content.

## Prompt To Use

```markdown
You are assisting an individual student in SOEN 6011: Software Engineering Processes with Deliverable 1.

Act as a software engineering analyst, requirements analyst, and scientific calculator design assistant.

Context:
- This is an individual software engineering project.
- The assigned function is F7: \(x^y\), where \(x\) and \(y\) are real variables.
- The project concerns scientific computing software that supports the assigned function \(x^y\), similar to a function in a scientific calculator.
- The project process includes elements of agile methodologies and DevOps.
- D1 must focus only on Problems 1–4.
- Every problem must use one or more publicly available GAI tools that rely on LLMs.
- The prompts must be based on the CASTROFF prompt engineering framework: Constraints, Audience, Structure, Tone, Role, Output format, Focus, and Function.
- All non-original work must be cited and referenced appropriately.
- Claims must be evidence-based.
- Do not copy external text verbatim.
- The deliverable should be suitable for LaTeX.

Delivery 1 tasks:
1. Problem 1: Create a persona for a user of the assigned function. There are multiple templates for creating a persona. Use a mind map to decide which template should be used.
2. Problem 2: Express requirements for the function based on one of the styles and guidelines given in the ISO/IEC/IEEE 29148 Standard. Associate each requirement with a unique identifier. Make all assumptions explicit. Problem 2 must be informed by Problem 1.
3. Problem 3: List two different algorithms in an established pseudocode format for implementing the function. The algorithms must be independent of any programming language. Problem 3 must be informed by Problem 2.
4. Problem 4: Use a mind map to decide which algorithm should be selected. Implement the function in Python using the selected algorithm. The implementation must have a textual user interface for input and output. Problem 4 must be informed by Problem 3.

Function information:
- Function identifier: F7
- Function: \(x^y\)
- Variables: \(x\) and \(y\) are real variables.
- The calculator should aim to produce real-valued results.
- The D1 implementation should remain simple and presentation-ready.

Important assumptions:
- The calculator supports real-valued output only.
- Complex number output is outside the D1 scope.
- For real-valued \(y\), \(x > 0\) is the main supported domain.
- The case \(x = 0\) must be handled carefully.
- Negative bases are not fully supported in D1 unless the exponent can be safely treated as an integer.
- The Python D1 implementation may use normal Python arithmetic and standard mathematical functions unless later deliverables impose stricter restrictions.
- Do not apply D2 from-scratch implementation or GUI requirements to D1.
- The implementation should be simple enough to modify later in D2.
- The implementation must use a textual user interface, not a GUI, in D1.

Course concepts to apply:
- Requirements should be clear, feasible, verifiable, and traceable.
- Use one selected style or guideline from ISO/IEC/IEEE 29148 rather than attempting to reproduce the full standard.
- Each requirement should have a unique identifier.
- Requirements should be informed by the user persona.
- Algorithms should be expressed in language-independent pseudocode.
- Algorithm selection should be justified using a mind map.
- The final implementation should be connected to the selected algorithm.
- The GAI output should be reviewed, modified, and verified by the student before submission.

Output requirements:

1. Start with a short overview of the D1 project:
   - Assigned function
   - Individual project scope
   - Main D1 artifacts
   - Dependency among the four problems

2. Provide a slide-by-slide outline for D1 with suggested slide titles and bullet points:
   - Title slide
   - Project overview
   - GAI and CASTROFF usage
   - Problem 1 persona mind map
   - Problem 1 final persona
   - Problem 2 assumptions
   - Problem 2 requirements
   - Problem 3 algorithm 1
   - Problem 3 algorithm 2
   - Problem 3 comparison
   - Problem 4 algorithm selection mind map
   - Problem 4 Python textual UI implementation
   - Demonstration plan
   - Limitations and future work
   - References

3. For Problem 1, include:
   - A mind map comparing at least three persona template options:
     1. Goal-directed persona
     2. Role-based persona
     3. Scenario-based persona
     4. Lightweight academic persona
   - Criteria for comparison:
     - Relevance to scientific computing software
     - Usefulness for requirements engineering
     - Level of detail
     - Suitability for an individual student project
     - Ease of presentation
   - Selected persona template
   - Justification for the selected template
   - Final persona with:
     - Name
     - Role
     - Background
     - Technical skill level
     - Goals
     - Needs
     - Pain points
     - Usage scenario
     - Expectations from the \(x^y\) calculator
     - How the persona informs requirements

4. For Problem 2, include:
   - A short list of assumptions.
   - A requirements table using one selected ISO/IEC/IEEE 29148 style or guideline.
   - Each requirement must have a unique identifier.
   - Use requirement IDs such as:
     - FR-001 for functional requirements
     - IR-001 for input requirements
     - OR-001 for output requirements
     - ER-001 for error-handling requirements
     - UR-001 for usability requirements
     - AR-001 for accuracy requirements
     - CR-001 for constraint requirements
   - The requirements table should include:
     - Requirement ID
     - Requirement statement
     - Rationale
     - Persona link
     - Verification method
   - Requirements should cover:
     - Functional behavior
     - Input handling
     - Output display
     - Domain restrictions
     - Error messages
     - Usability
     - Accuracy or precision
     - Textual user interface constraints
   - Include a short explanation of how Problem 1 informed Problem 2.

5. For Problem 3, include two different algorithms in established pseudocode format:

   Algorithm 1: Direct Power Evaluation
   - Purpose
   - Input
   - Output
   - Preconditions
   - Postconditions
   - Language-independent pseudocode
   - Domain limitations
   - Advantages
   - Disadvantages
   - Requirements supported

   Algorithm 2: Logarithm-Exponential Transformation
   - Use the identity \(x^y = e^{y \ln(x)}\)
   - Purpose
   - Input
   - Output
   - Preconditions
   - Postconditions
   - Language-independent pseudocode
   - Domain limitations
   - Advantages
   - Disadvantages
   - Requirements supported

   The algorithms must be independent of Python-specific syntax.

6. For Problem 4, include:
   - A mind map comparing Algorithm 1 and Algorithm 2.
   - Criteria for comparison:
     - Simplicity
     - Correctness for real-valued outputs
     - Ease of implementation in Python
     - Compatibility with textual user interface
     - Understandability for users
     - Domain handling
     - Alignment with D1 requirements
     - Suitability for future D2 modification from scratch
   - Selected algorithm.
   - Justification for selection.
   - Rejected algorithm and reason for not selecting it.
   - Risks or limitations of the selected algorithm.
   - Link back to Problem 3 and Problem 2.

7. For the Python implementation, include:
   - Python source code.
   - The program should prompt the user to enter \(x\).
   - The program should prompt the user to enter \(y\).
   - The program should calculate \(x^y\).
   - The program should display the result clearly.
   - The program should handle invalid numeric input.
   - The program should handle domain restrictions for real-valued outputs.
   - The program should not return complex numbers.
   - The program should include clear error messages.
   - The code should be beginner-friendly and suitable for D1.
   - Include example input and output.
   - Explain how the implementation satisfies the requirements from Problem 2.
   - Include known limitations.

8. Include a section named "GAI Use Explanation" with:
   - What this prompt was intended to obtain.
   - Which prompt type was used for each problem.
   - How the output should be reviewed and modified before submission.
   - Which parts require external citation or verification.
   - How the student manually checks correctness.
   - Why the GAI output should not be treated as final truth.

9. Include a section named "Prompt Types Used" with a table:
   - Problem number
   - Prompt type
   - Purpose
   - Expected output
   - Manual review needed

   Use these prompt types:
   - Problem 1: Ideation and decision-support prompt
   - Problem 2: Requirements elicitation and specification prompt
   - Problem 3: Algorithm generation and comparison prompt
   - Problem 4: Decision-making and code generation prompt
   - Final integration: Organization and presentation prompt

10. Include a section named "Potential References To Verify" with credible source categories:
   - ISO/IEC/IEEE 29148 requirements engineering standard
   - Python documentation
   - Mathematical references for exponentiation and logarithm-exponential transformation
   - Persona design or user-centered design references
   - CASTROFF framework reference
   Do not invent exact bibliographic details unless they are real and verifiable.

11. Include a section named "Validation Checklist" with:
   - D1 only
   - Individual work stated
   - Function F7 \(x^y\) stated
   - Persona included
   - Persona template selected using mind map
   - Requirements use unique IDs
   - Assumptions explicit
   - Problem 2 informed by Problem 1
   - Two algorithms included
   - Problem 3 informed by Problem 2
   - Algorithm selected using mind map
   - Python textual UI included
   - Problem 4 informed by Problem 3
   - GAI use documented
   - Prompt types documented
   - Output explanations included
   - Citations and references planned
   - LaTeX-ready structure

Important constraints:
- Do not present generated content as final truth.
- Do not invent standards, references, or mathematical claims.
- If uncertain, state uncertainty and suggest what source should be checked.
- Keep the language concise enough for slide conversion.
- Use original wording rather than copying from source material.
- Keep the implementation simple and appropriate for D1.
- Focus only on D1, not D2 or D3.
```

## Expected Output Use

The expected GAI output should be treated as brainstorming, organization support, and a first draft only. Before using it in slides or a LaTeX report, the student should:

* Verify mathematical claims about (x^y), especially domain restrictions for real-valued outputs.
* Review requirements for clarity, feasibility, and verifiability.
* Ensure each requirement has a unique identifier.
* Confirm that Problem 2 is informed by the persona from Problem 1.
* Confirm that Problem 3 is informed by the requirements from Problem 2.
* Confirm that Problem 4 is informed by the algorithms from Problem 3.
* Test the Python textual user interface manually.
* Rewrite generated text into the student’s own wording.
* Add citations for all non-original ideas, standards, definitions, or references.
* Ensure the final document is typeset in LaTeX.

## Reference For CASTROFF Definition

Tavakoli, H. (2026). The CASTROFF Framework: A Professional Standard for Prompt Engineering. In *Prompt Engineering for Everyone*. Apress. https://doi.org/10.1007/979-8-8688-2338-1_6
