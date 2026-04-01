# Local IDE To Colab Workflow

This is a simple workflow that fits the bootcamp goal well.
The main idea is:

- write and organize code locally
- track progress with git
- use Colab when your machine is missing packages or when notebook execution is easier there

## Why This Workflow Works

- your IDE is better for writing and organizing code
- git keeps your progress safe and visible
- Colab gives you the libraries and notebook environment when your local machine is missing packages

## Recommended Flow

1. Open the bootcamp folder locally in your IDE.
2. Write your `.py` files and notes locally.
3. Commit your progress with git.
4. Push to GitHub.
5. Open Google Colab.
6. Upload the notebook or pull your repo into Colab.
7. Run the heavier notebook or training cells there.
8. Bring useful improvements back into the repo as normal Python files when possible.

## Two Easy Ways To Use Colab

### Option 1: Upload The Notebook

This is the simplest option.

1. Go to Colab.
2. Upload `ai_bootcamp.ipynb`.
3. Upload the dataset you want to use.
4. Run the notebook cells.

### Option 2: Use Your GitHub Repo

This is better once your repo is set up well.

1. Push this bootcamp repo to GitHub.
2. Open Colab.
3. Open the notebook from GitHub.
4. Run the notebook there.

## Suggested Habit

- write code locally
- commit locally
- push to GitHub
- run notebook training in Colab when needed
- copy improvements back into the repo

## Practical Tip

If you save plots, models, or temporary outputs in Colab, decide whether they belong in your repo.
Usually:

- code and notes should go in git
- temporary generated outputs usually should not
