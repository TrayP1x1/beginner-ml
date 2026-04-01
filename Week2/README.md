# Week2

Use one day folder at a time and code the solutions from your IDE.

- Day 8: loading CSVs with pandas and writing inspection helpers
- Day 9: filter, sort, group, and reusable query functions
- Day 10: clean missing values with strategy functions
- Day 11: matplotlib plots with plotting helpers
- Day 12: feature engineering with explicit transformation steps
- Day 13: splitting, normalization, and leakage-safe preprocessing
- Day 14: week 2 project with modular analysis code

Suggested workflow:

1. Read the matching notebook section.
2. Open the day folder for the exercise brief.
3. Write your solution in your IDE.
4. Turn notebook-style work into small reusable functions.
5. Commit your progress with git.
6. If the exercise needs libraries, run the notebook or training code in Colab.

Week 2 should feel like the jump from "I can use pandas" to "I can write structured data code."
By the end of Week 2, you should be able to:

- move beyond one-off notebook cells and write reusable pandas helpers
- separate loading, cleaning, plotting, and reporting into distinct functions
- use type hints and small config constants where they help readability
- explain the difference between raw data work and a clean preprocessing pipeline
- feel comfortable enough with Python structure that Week 3 can focus on modeling instead of basic syntax

Week 2 is also the setup week for modeling.
Before you touch PyTorch, you should already understand:

- what your feature matrix looks like
- what your target column looks like
- why train/validation/test splits matter
- why normalization must use training statistics only
- how to package preprocessing into reusable helpers
