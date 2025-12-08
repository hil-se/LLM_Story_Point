FEW_SHOT_PROMPT = "
You are an expert agile estimation assistant specialized in story point estimation for software development.

Use the following examples as reference to estimate the story point of the task described below:

FEW SHOT EXAMPLES:

Title: As a user I would like the Days Remaining Gadget to cascade down and select a release date that does exist, even if it is within a child version
Description: For instance, at present it selects the parent version which has no release date set (cause we don't yet know when we release). Instead, it should select the child version that has a release date.
Storypoint: 3

Title: Test Infrastructure: mocking integration tests
Description: This improvement is to allow developers to run the test suites more often by reducing the amount of time it takes to run a build. There are many integration tests that unnecessarily go all the way to the underlying storageproviders. These tests should be revisited with an eye towards mocking out the network calls where they are overly redundant.
Storypoint: 8

Title: as a user I want to see smart names for classes and functions in reports
Description: The point is that Scala code is being translated to a bytecode containing various "cryptic" names. For instance, "overloaded operators" have "$op" in method's name. Think how to reasonably represent methods, functions, inline classes, anonymous functions, case classes, traits etc etc in HTML report at least (XML / JSON are less important).
Storypoint: 20

Title: Studio can be a lot smarter when handling logic expressions. I'd rather not see AND, OR, NOT filters in the palette
Description: it seems we could have a single filter element in the flow control section that has one dialog that allows people to select an expression (this works for wildcard and regex) and have a section below to allow the user to add new filters with AND, OR or NOT. I think this provides much better usability as there is now only a single filter element not a whole palette. And it makes working with logic filters more natural for the user. i.e.it feels odd to have to start with an AND filter and then configure the expressions
Storypoint: 34

Title: Deploy FY16 Storage Expansion (part 2)
Description: Deploy infrastructure for FY16 storage expansion. This epic covers follow-on work to DM-3830. Deliverable: storage expansion Staff: 5 NCSA ICI engineers (networking, storage, systems) Effort: 45 days Planned Start: 6/1/2016 Planned End: 7/31/2016
Storypoint: 90


TASK TO ESTIMATE:
Title: {title}
Description: {description}

OUTPUT:
<integer>
"
