# Git Cheat Sheet

These are the main commands you should practice during the bootcamp.

## Core Daily Commands

Check what changed:

```bash
git status
```

See line-by-line changes:

```bash
git diff
```

Add all current changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "finish day 3 functions practice"
```

See recent commits:

```bash
git log --oneline
```

Push to GitHub:

```bash
git push
```

Pull the latest version:

```bash
git pull
```

Fetch remote updates without merging yet:

```bash
git fetch
```

See which branch you are on:

```bash
git branch
```

See local and remote branches:

```bash
git branch -a
```

Switch to another branch:

```bash
git switch branch-name
```

Create and switch to a new branch:

```bash
git switch -c new-branch-name
```

Compare your local branch with the remote:

```bash
git status -sb
```

See commits in local that are not on GitHub yet:

```bash
git log origin/main..HEAD --oneline
```

See commits on GitHub that are not in your local branch yet:

```bash
git log HEAD..origin/main --oneline
```

See line changes between local and remote:

```bash
git diff origin/main..HEAD
```

## Branching And Merging

Make sure your local `main` knows about GitHub:

```bash
git switch main
git fetch
git pull
```

Create a branch for your work:

```bash
git switch -c week4-cleanup
```

After you finish and commit your work, merge it into `main`:

```bash
git switch main
git merge week4-cleanup
```

If the branch is no longer needed, delete it locally:

```bash
git branch -d week4-cleanup
```

Push a new branch to GitHub:

```bash
git push -u origin week4-cleanup
```

## Checking Local Vs GitHub

A very useful quick check:

```bash
git status -sb
```

Common meanings:

- `ahead 1`: you have local commits not pushed yet
- `behind 2`: GitHub has commits you do not have locally yet
- `ahead 1, behind 2`: both sides changed and you need to sync carefully

Update your view of GitHub first:

```bash
git fetch
```

Then compare:

```bash
git log --oneline --decorate --graph --all
```

## Safe Beginner Merge Flow

1. Finish your work on a branch.
2. Run `git status` and make sure everything is committed.
3. Run `git switch main`.
4. Run `git pull`.
5. Run `git merge your-branch-name`.
6. If there are no conflicts, run `git push`.
7. If the merge is complete and the branch is done, delete the branch.

## Good Beginner Workflow

1. Open the day exercise in your IDE.
2. Write code until one small part works.
3. Run `git status`.
4. Run `git add .`.
5. Run `git commit -m "clear message here"`.
6. Repeat in small steps.
7. Push to GitHub at the end of the day.

## Good Commit Message Examples

- `finish day 1 variables practice`
- `add csv reading for day 4`
- `clean titanic data and plot age distribution`
- `train first housing regression model`
- `complete mock test attempt`

## Useful Advice

- Commit small working steps instead of one giant messy commit.
- Use clear commit messages.
- Push often enough that your work is backed up.
- Run `git fetch` before comparing your local branch to GitHub.
- Use branches when trying a bigger change so `main` stays clean.
- Check `git status` before switching branches or merging.
- Do not worry about being perfect. The goal is consistency.
