---
layout: post
title: "LLM Useful Prompts"
date: 2024-12-03 23:17:00 +0000
categories: llm notes
permalink: /notes/llm/prompts
---

### Email

Rewrite the email to be concise, professional, and free of overly polite language. Ensure the tone is formal and respectful, avoiding colloquialisms and redundant information. Aim to reduce the number of sentences while maintaining clarity and professionalism. The email is: {email}.

### Python Code Refactor

Refactor the code to adhere to Python best practices, including PEP 8 guidelines, DRY principles, and SOLID principles. The code should be concise, clean, and effective, with a focus on readability and maintainability. Ensure that the observable behavior remains largely unchanged unless the design is significantly flawed. If necessary, suggest relevant concepts such as design patterns, optimization techniques, or Python-specific libraries that could enhance the code. The code is {code}.

### Pytest Unit Test
Help me write unit tests using pytest for this piece of code, which may contain classes and functions. Ensure the tests cover all edge cases, including boundary conditions, invalid inputs, and exceptional cases. Organize the tests by function or class, and use fixtures for setup and teardown. Aim for comprehensive coverage and maintain readability and maintainability of the test code.


### Add this prompt at the beginning of each new chat
Whenever I give you any instruction, you will:

1. Refine the instruction to improve clarity, specificity, and effectiveness.
2. Create a relevant perspective to adopt for interpreting the instruction.
3. Present the refined version of the instruction using the format 'Refined: [refined instruction]'.
4. State the perspective you'll adopt using the format 'Perspective: [chosen perspective]'.
5. Execute the refined instruction from the chosen perspective and present the result using the format 'Execution: [answer]'.
