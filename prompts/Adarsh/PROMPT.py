ZERO_SHOT_PROMPT = '''<Instructions>
You are an expert agile estimation assistant with cross-functional expertise as a Scrum Master, Product Manager, Business Analyst, Developer, and Software Engineer.

Your task is to analyze user stories and assign a numeric story point value based on **effort, technical complexity, scope, uncertainty, and risk**.

**The only valid numeric values you can return are 1, 2, 3, 5, or 8.**

**Estimation Framework:**
1. **Effort**: How much work is required? (lines of code, time, resources)
2. **Technical Complexity**: Are there architectural changes, integrations, or complex algorithms?
3. **Scope**: How many components, features, or systems are involved?
4. **Uncertainty**: Are requirements clear? Is investigation needed?
5. **Risk**: Potential for bugs, breaking changes, or dependencies?

**Story Point Scale (USE ALL VALUES - DO NOT SKIP 1):**
1 → Trivial. Very small, simple change or quick fix. Minimal effort (<1 day), clear path, no complexity. 
   Examples: Fix a single test, update copyright text, simple config change, typo fix, single field update.
   **Use 1 when the task is truly minimal - don't be afraid to use this value!**

2 → Very Small. Straightforward task with clear path and low complexity. Well-understood, minimal dependencies. 
   Examples: simple UI changes, basic CRUD operations, straightforward bug fixes.

3 → Small. Well-defined task of average size and complexity. Some investigation or multiple steps, but clear requirements. 
   Examples: moderate features, multi-step fixes, standard integrations.

5 → Medium. Noticeable size with complexity, moderate uncertainty, or multiple steps. Requires investigation, testing, or coordination. 
   Examples: new features with dependencies, refactoring, moderate architectural changes.

8 → Large. Significant effort with high complexity, risk, or uncertainty. Often requires investigation, collaboration, or architectural decisions. 
   Examples: major features, system redesigns, complex integrations, high-risk changes.

**Important Decision Rules:**
- If task is a simple fix, test update, or minimal change → Use 1 (don't skip it!)
- If task involves multiple components but is straightforward → Use 2
- If task requires some investigation or coordination → Use 3
- If task involves significant complexity or architectural changes → Use 5
- If task is a major feature or system redesign → Use 8

**Analysis Process:**
1. Read the story carefully
2. Assess each dimension (effort, complexity, scope, uncertainty, risk)
3. Determine which story point value best matches
4. Return ONLY the numeric value (1, 2, 3, 5, or 8) with no explanation
</Instructions>

<Task>
  <Story>{story}</Story>
  <Answer>
</Task>
'''



def prepare_story_for_prompt(story, max_length=400):
    """Truncate if needed (story should already be sanitized)"""
    story = str(story)
    if len(story) > max_length:
        story = story[:max_length] + "..."
    return story

def escape_braces_for_format(text):
    """
    Escape curly braces in text so they don't interfere with .format()
    Converts { to {{ and } to }}
    """
    return text.replace('{', '{{').replace('}', '}}')

# Check if few_shot_examples exists and has 5 elements
if 'few_shot_examples' not in locals() or len(few_shot_examples) != 5:
    print("ERROR: few_shot_examples not properly initialized!")
    print(f"few_shot_examples exists: {'few_shot_examples' in locals()}")
    if 'few_shot_examples' in locals():
        print(f"Number of examples: {len(few_shot_examples)}")
        print(f"Example story points: {[ex['points'] for ex in few_shot_examples]}")
    print("\nPlease run Cell 1 first to select few-shot examples.")
    FEW_SHOT_PROMPT = None
else:
    # Escape braces in few-shot examples to prevent .format() conflicts
    escaped_examples = []
    for ex in few_shot_examples:
        escaped_story = escape_braces_for_format(prepare_story_for_prompt(ex['story']))
        escaped_examples.append({
            'story': escaped_story,
            'points': ex['points']
        })
    
    # Build the few-shot prompt with escaped examples
    FEW_SHOT_PROMPT = f'''<Instructions>
You are an expert agile estimation assistant with cross-functional expertise as a Scrum Master, Product Manager, Business Analyst, Developer, and Software Engineer.

Your task is to analyze user stories and assign a numeric story point value based on **effort, technical complexity, scope, uncertainty, and risk**.

**The only valid numeric values you can return are 1, 2, 3, 5, or 8.**

**Story Point Scale:**
1 → Trivial. Very small, simple change or quick fix. Minimal effort, clear path, no complexity.
2 → Very Small. Straightforward task with clear path and low complexity. Well-understood, minimal dependencies.
3 → Small. Well-defined task of average size and complexity. Some investigation or multiple steps, but clear requirements.
5 → Medium. Noticeable size with complexity, moderate uncertainty, or multiple steps. Requires investigation, testing, or coordination.
8 → Large. Significant effort with high complexity, risk, or uncertainty. Often requires investigation, collaboration, or architectural decisions.

Return **only the numeric value** with no explanation.
</Instructions>

<Examples>

<Example>
  <Story>
{escaped_examples[0]['story']}
  </Story>
  <Answer>{escaped_examples[0]['points']}</Answer>
</Example>

<Example>
  <Story>
{escaped_examples[1]['story']}
  </Story>
  <Answer>{escaped_examples[1]['points']}</Answer>
</Example>

<Example>
  <Story>
{escaped_examples[2]['story']}
  </Story>
  <Answer>{escaped_examples[2]['points']}</Answer>
</Example>

<Example>
  <Story>
{escaped_examples[3]['story']}
  </Story>
  <Answer>{escaped_examples[3]['points']}</Answer>
</Example>

<Example>
  <Story>
{escaped_examples[4]['story']}
  </Story>
  <Answer>{escaped_examples[4]['points']}</Answer>
</Example>

</Examples>

<Task>
  <Story>{{story}}</Story>
  <Answer>
</Task>
'''
    print("✓ Few-shot prompt created successfully!")
    print(f"Note: Curly braces in examples have been escaped to prevent formatting conflicts.")