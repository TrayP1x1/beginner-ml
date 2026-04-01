# Day 19 - Full Pipeline Practice

Rebuild the full workflow from memory.

## Tasks

- Load the CSV.
- Inspect and clean it.
- Engineer one or two features.
- Split, normalize, tensorize, train, and evaluate a model.
- Organize the solution into helper functions instead of one giant script.
- Make the full pipeline runnable from `main()`.
- End the file with `if __name__ == "__main__": main()`.
- Introduce a small config class or dataclass for paths and hyperparameters.
- Return intermediate artifacts in a clear structure instead of relying on globals.
- Add at least one error check for a missing target column or empty dataset.

## Structure Goal

Use a structure close to this:

- imports
- a small config class or constants section
- `load_data()`
- `prepare_features()`
- `train_model()`
- `evaluate_model()`
- `main()`

This is close to what you want in a real coding test: readable, fast to explain, and easy to debug.

## Stronger Python Goal

This should feel like a small application with stages, not a loose experiment.

## Suggested Output Files

- one `.py` file or notebook scratch file created from your IDE
- optional `.png` plots for visualization days
- a short text summary in comments or markdown

## Data

- Week 1 mainly uses `data/tiny_scores.csv`
- Week 2 and Week 3 mainly use `data/student_dev_ai_practice.csv`

## Git Checkpoint

Make one clean commit only after the full pipeline works from top to bottom.

## Colab Note

If a library is missing on your machine, keep writing code locally in your IDE,
commit the code to git, then run the training or notebook part in Google Colab.
