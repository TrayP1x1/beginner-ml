# Week3

Use one day folder at a time and code the solutions from your IDE.

- Day 15: tensors, shapes, and conversion helpers
- Day 16: regression with PyTorch and train/eval function structure
- Day 17: binary classification with prediction utilities
- Day 18: metrics, debugging, and experiment analysis
- Day 19: full pipeline practice with configuration objects
- Day 20: mock test with clean project constraints
- Day 21: capstone with explainable structure and tradeoff notes

Suggested workflow:

1. Read the matching notebook section.
2. Open the day folder for the exercise brief.
3. Write your solution in your IDE.
4. Keep data preparation, training, evaluation, and reporting in separate helpers.
5. Commit your progress with git.
6. If the exercise needs libraries, run the notebook or training code in Colab.

Best real-data progression for this week:

- start with `data/student_dev_ai_practice.csv`
- move to `data/kaggle/housing_prices.csv` for regression
- move to `data/kaggle/titanic.csv` for classification
- try `data/kaggle/iris.csv` only as a bonus

Week 3 is where the repo should prove the full promise.
By the end of Week 3, you should be able to:

- organize model code into small reusable functions instead of one long training script
- separate data preparation, training, evaluation, and reporting
- use simple config objects or constants for experiment settings
- debug shape, metric, and training-loop issues systematically
- build an end-to-end ML workflow in Python that is clear enough to explain in an interview or coding test

Important note:
Week 3 should feel advanced relative to the start of the repo, but it should not feel random.
If Day 15 feels too abrupt, review the Week 2 to Week 3 bridge material first so tensors and models connect cleanly to the preprocessing work you already did.
