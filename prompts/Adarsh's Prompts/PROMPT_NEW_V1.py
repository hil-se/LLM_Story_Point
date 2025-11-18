ZERO_SHOT_PROMPT = '''You are an experienced software developer estimating a development task. Think like a developer who needs to assess the actual time, effort, and work involved.

These are software development tasks. Estimate the story points based on how a developer would realistically assess the work, considering the time and effort required.

DEVELOPER ESTIMATION FACTORS (think about these as a developer would):

1. Implementation Time: How long will it actually take to code this? Consider writing code, debugging, and getting it working.

2. Level of Effort: How much mental effort and focus is required? Simple copy-paste vs. complex problem-solving?

3. Research & Learning: Do you need to learn new technologies, APIs, or patterns? How much time for research?

4. Code Complexity: How many files need changes? How many functions/classes to modify? How interconnected is the code?

5. Testing Effort: Unit tests, integration tests, manual testing - how much testing time is needed?

6. Debugging & Troubleshooting: How likely are you to hit unexpected issues? How much debugging time?

7. Code Review & Refactoring: How much code review feedback to address? Any refactoring needed?

8. Integration & Dependencies: How many other systems/components need to work together? Integration complexity?

9. Uncertainty & Unknowns: How clear are the requirements? How many "we'll figure it out as we go" moments?

10. Context Switching: Does this require understanding multiple codebases or systems?

DEVELOPER THINKING:

- Estimate as if you're the developer who will actually implement this

- Consider the full development cycle: understanding requirements, coding, testing, debugging, code review, deployment

- Think about real-world time: "This looks like a few hours" vs "This will take days" vs "This is a multi-week effort"

- Account for the hidden work: setup, configuration, dealing with edge cases, fixing bugs you discover

- More time and effort = higher story points

- Be consistent: if Task A clearly requires more developer time/effort than Task B, assign A a higher value

- Focus on RELATIVE effort compared to other development tasks

INSTRUCTIONS:

- These are software development tasks

- Estimate from a developer's perspective considering actual time and effort

- Assign a positive integer reflecting relative development effort

- Determine appropriate values based on the effort spectrum you observe

- Do NOT use predefined scales (Fibonacci, etc.)

- Do NOT explain your reasoning

- Do NOT include any text, labels, or prefixes

- Output ONLY a single integer

TASK TO ESTIMATE:

Title: {title}

Description: {description}

OUTPUT:
<integer>

'''
 
