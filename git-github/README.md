# Git and GitHub Homework

This folder contains my tasks and screenshots for Git operations (`git commit -a -m` vs `git commit -m` and `git cherry-pick`).

---

## Task 1: `git commit -a -m` vs `git commit -m`

### What I Learned
* **`git commit -m "message"`**: Only commits files that have already been staged using `git add`. If you modified a tracked file but didn't run `git add`, it won't be included in the commit.
* **`git commit -a -m "message"`**: Automatically stages and commits all modified or deleted tracked files in a single step. (Note: It does not automatically stage new untracked files).

### Screenshot
![Git Commit Difference](./screenshots/git_commit_diff.png)

---

## Task 2: Git Cherry-Pick

### What I Learned & Steps Executed
`git cherry-pick` allows you to pick a specific commit from another branch and apply it to your current branch without merging the whole branch.

1. Made commits on `main` branch.
2. Created a new branch (`feature-branch`) and made 3 commits.
3. Used `git log --oneline` to find the commit hash of the bugfix commit.
4. Switched back to `main` branch using `git checkout main`.
5. Ran `git cherry-pick <commit-hash>` to bring only that bugfix commit into `main`.
6. Verified with `git log` that the commit was added to `main`.

### Screenshot
![Git Cherry Pick Walkthrough](./screenshots/git_cherrypick.png)
