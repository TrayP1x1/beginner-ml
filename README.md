# Student Dev AI Bootcamp

This folder is designed to be self-contained.
The main goal is ambitious on purpose:

- start from beginner Python or almost no Python
- become strong enough in 3 weeks to write clean, intensive, ML-ready Python
- understand the full beginner-to-ML workflow from CSV to model evaluation
- use Week 4 as extra sharpening for more advanced engineering habits

By the end of the main 3-week path, you should be able to:

- write clean Python with functions, type hints, small classes, and script structure
- read CSV files and validate inputs
- clean and explore tabular data with reusable helpers
- make plots and organize analysis code into functions
- train regression and classification models
- evaluate results and debug your pipeline
- practice a real IDE -> git -> Colab workflow
- understand the main moving parts of a neural network training pipeline well enough to keep learning from there

## What Is Inside

- `ai_bootcamp.ipynb`: the main teaching notebook
- `Week1`, `Week2`, `Week3`: the main 3-week Python-to-ML ramp
- `Week4`: the extra advanced engineering week for cleaner code, CLI tools, tests, and project structure
- `data`: practice datasets
- `GIT_CHEATSHEET.md`: git commands you should practice during the bootcamp
- `COLAB_WORKFLOW.md`: a simple local IDE to Colab workflow
- `Bonus`: extra optional exercises inspired by your earlier homework material
- `templates/test_ready_project`: a clean `main.py`-style starter for CSV -> model test practice
- `requirements.txt`: packages for local setup
- `.gitignore`: sensible defaults for a Python and notebook project

## Recommended Learning Flow

1. Read one section of `ai_bootcamp.ipynb`.
2. Open the matching day folder and do the exercise from your IDE.
3. Add type hints, helper functions, and one validation check whenever the exercise allows it.
4. Commit your progress with git.
5. Push to GitHub regularly.
6. Use Colab for notebook execution or model training when needed.

## Bootcamp Shape

- Week 1: build real Python foundations fast
- Week 2: turn raw data work into structured, reusable Python
- Week 3: turn that Python into full ML pipelines, model code, and neural-network intuition
- Week 4: extra advanced sharpening for engineering-style Python

## Teaching Style

This repo is meant to feel intense but logical.
The rule is:

- do not introduce a tool before the learner has seen the underlying Python idea
- start each day with easier tasks
- move into the core task of the day
- finish with a harder stretch that pushes toward cleaner or more advanced code

That means:

- functions come before larger multi-function scripts
- file paths and CSV reading come before reusable data loaders
- basic classes and dataclasses come after function structure is already familiar
- train/test splitting and normalization come before tensors and PyTorch
- tensor shape handling comes before full neural-network training loops

## Repo Structure

- `Week1`: beginner Python upgraded into strong script-writing habits
- `Week2`: pandas, cleaning, plotting, and reusable data helper design
- `Week3`: modeling, pipelines, and ML code structure
- `Week4`: advanced sharpening with CLI design, tests, refactoring, and project structure
- `templates/test_ready_project`: a small example project split into modules and runnable from `main.py`
- `main.py`: a simple repo-level entry point that runs the test-ready template

## How To Study This Repo

1. Learn the concept from the notebook and the matching week/day README.
2. Rebuild the exercise yourself in your own `.py` file.
3. Compare your structure against the provided starter scripts and `templates/test_ready_project`.
4. Practice making your final version runnable from `main.py`.
5. Add tests, error handling, and clearer function boundaries as the weeks progress.

## Python Growth Goal

This repo is not only about getting the right answer.
The goal is to finish each week with a stronger Python skill set:

- after Week 1, you should be comfortable writing small but clean scripts with helper functions, `main()`, type hints, and simple data structures
- after Week 2, you should be comfortable turning messy data tasks into reusable functions instead of one-off notebook code
- after Week 3, you should be strong enough to build an end-to-end ML workflow in readable Python and be ready to compete on beginner Kaggle-style problems
- after Week 4, you should be noticeably sharper at command-line execution, tests, modular structure, refactoring, and maintainable project design

## Best Dataset Progression

1. Start with `data/tiny_scores.csv`
2. Move to `data/student_dev_ai_practice.csv`
3. Practice real regression with `data/kaggle/housing_prices.csv`
4. Practice real classification with `data/kaggle/titanic.csv`
5. Try `data/kaggle/iris.csv` as a bonus multiclass project

## GitHub Goal

This folder is meant to be clean enough to upload to GitHub as your learning project.
That means:

- your notebook teaches the full path
- the exercise folders give you enough practice
- the datasets are already included
- the workflow docs are already included
- your code should become easier to review week by week

If you complete the exercises and keep your commits organized, this can become a very solid public study repo.
