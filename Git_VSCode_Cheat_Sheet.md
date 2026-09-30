# Git in VS Code: Code Cheat Sheet

Open this file in VS Code. Press **Ctrl + Shift + V** to preview it.
Run individual commands in **Terminal > New Terminal**, inside your project folder.
These are independent examples, not one script to run from top to bottom.
Replace example filenames, branch names, URLs, names, and emails with your own.

## 1. The basic workflow

**Edit > Save > Stage > Commit > Push**

- Save: update the file on your computer.
- Stage: choose changes for the next commit.
- Commit: record those staged changes in local history.
- Push: upload commits to the remote repository, such as GitHub.
- Pull: download and integrate remote changes into your current branch.
- Fetch: download remote updates without integrating them into your files.

## 2. First-time setup

```bash
# Check whether Git is installed.
git --version

# Set the author information attached to future commits.
# This does not sign you into GitHub.
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# Check the saved settings.
git config --global user.name
git config --global user.email
```

## 3. Start a project: choose ONE option

### Option A: Download an existing repository

```bash
# Copy an existing GitHub repository to your computer.
git clone https://github.com/USERNAME/REPOSITORY.git

# Move into the downloaded project folder.
cd REPOSITORY

# Open this folder in VS Code, if the code command is available.
code .
```

### Option B: Track an existing local project

Open your project folder in VS Code, then open its terminal.

```bash
# Create a new local repository in the current folder.
git init

# Review the files before staging them.
git status

# Stage a specific file. Repeat for other files you want to include.
git add analysis.R

# Save the first snapshot locally.
git commit -m "Add initial analysis"
```

## 4. Inspect your work

```bash
# Show the current branch and changed, staged, or untracked files.
git status

# Show unstaged changes to tracked files.
# New untracked files do not appear in this diff.
git diff

# Show staged changes that will go into the next commit.
git diff --staged

# Show recent commits, one per line.
git log --oneline -10

# Show branch history as a compact graph.
git log --oneline --graph --all
```

## 5. Stage and commit

```bash
# Stage one file.
git add analysis.R

# Stage multiple named files.
git add analysis.R README.md

# Alternatively, stage all changes under the current folder,
# including additions, edits, and deletions. Review first.
git add .

# Record the staged changes in local history.
git commit -m "Fix rider ranking calculation"
```

A commit includes the staged version. If you edit a file again after staging it,
run git add again to include the latest edits.

## 6. Connect a local project to GitHub

Create an empty repository on GitHub first. These commands assume you already
have a local commit and do not already have a remote named origin.

```bash
# Name the current branch main.
git branch -M main

# Connect this local repository to the GitHub repository.
git remote add origin https://github.com/USERNAME/REPOSITORY.git

# Upload main and remember its remote branch for future push/pull commands.
git push -u origin main

# Display configured remote addresses.
git remote -v
```

If you cloned the repository, origin is normally already configured.
GitHub authentication may be requested when accessing the remote.

## 7. Download and upload changes

```bash
# Download remote updates without changing your working files.
git fetch

# Download and integrate updates into your current branch.
# Commit or stash unfinished work first.
git pull

# Upload your local commits to the connected remote branch.
git push
```

If a push is rejected because the remote has new commits, pull and resolve any
conflicts before pushing again. If Git asks you to choose a reconciliation
strategy, git pull --no-rebase integrates using a merge.

## 8. A normal work session

This example assumes the current branch already has a connected remote branch.

```bash
# Before editing, check that the working folder is clean and get updates.
git status
git pull

# Now edit and SAVE your files in VS Code.

# Review, stage, commit, and upload your work.
git diff
git add analysis.R
git diff --staged
git commit -m "Add rider performance summary"
git push
```

## 9. Create and switch branches

A branch lets you develop changes separately from main.

```bash
# List local branches. The asterisk marks your current branch.
git branch

# Create a branch and switch to it.
git switch -c new-analysis

# Switch to an existing branch.
git switch main

# Return to your work branch.
git switch new-analysis

# After committing changes, publish this branch for the first time.
git push -u origin new-analysis
```

Commit or stash unfinished work before switching branches.
Publishing a branch does not merge it into main. On GitHub, you can open a pull
request to propose merging it.

## 10. Merge a branch locally

```bash
# Switch to the branch that should RECEIVE the changes.
git switch main

# Update it first.
git pull

# Bring new-analysis into main.
git merge new-analysis

# Upload the updated main branch.
git push

# Optional: delete the local work branch after it has been merged.
git branch -d new-analysis
```

## 11. Undo or set aside changes

```bash
# Unstage a file while KEEPING your edits.
git restore --staged analysis.R

# CAUTION: discard unstaged edits to a tracked file.
# Restores the staged version, or the last committed version if unstaged.
git restore analysis.R

# Undo a particular commit by creating a NEW reversing commit.
# Replace abc1234 with the commit ID shown by git log --oneline.
git revert abc1234

# Temporarily store tracked changes and untracked files.
# Ignored files are not included.
git stash push -u -m "Unfinished analysis"

# List saved stashes.
git stash list

# Restore the latest stash; removes it from the list if successful.
git stash pop
```

Discarded uncommitted edits may not be recoverable through Git.
Revert and stash pop can produce conflicts that need manual resolution.

## 12. Resolve a merge conflict

1. Run git status to identify conflicted files.
2. Open each file in VS Code and inspect both versions.
3. Use the conflict actions or Merge Editor to produce the intended result.
4. Remove any remaining conflict markers and save the file.
5. Stage the resolved files, then finish the merge:

```bash
# Mark a file as resolved after editing and saving it.
git add analysis.R

# Complete a standard merge after all conflicts are resolved.
git commit

# Upload the result.
git push

# Alternative: cancel an in-progress merge instead of completing it.
git merge --abort
```

This sequence is for a merge. A rebase or revert has its own continuation command;
follow the instructions printed by git status for those operations.

## 13. Ignore files with .gitignore

Create a file named .gitignore in the project root. For an R project, its contents
could be:

```gitignore
# R session and project metadata
.Rhistory
.RData
.Ruserdata
.Rproj.user/

# Local environment settings, often containing secrets
.env
```

These are file patterns, not terminal commands. Git ignores matching untracked
files. Files that are already tracked remain tracked.

## 14. VS Code controls and indicators

| Task | VS Code action (Windows) |
| --- | --- |
| Open Source Control | Ctrl + Shift + G |
| Open Command Palette | Ctrl + Shift + P |
| Open a terminal | Terminal > New Terminal |
| Review changes | Click a file under Changes |
| Stage a file | Click + beside it |
| Unstage a file | Click the minus button beside it under Staged Changes |
| Commit | Enter a message, then click Commit |
| Push or pull | Source Control > ... menu |
| Sync Changes | Pulls first, then pushes |
| Switch branch | Click the branch name in the bottom-left status bar |
| Clone | Command Palette > Git: Clone |
| Start tracking | Source Control > Initialize Repository |

| File indicator | Meaning |
| --- | --- |
| M | Modified |
| U | Untracked |
| A | Added to staging |
| D | Deleted |

## Official references

- https://code.visualstudio.com/docs/sourcecontrol/overview
- https://code.visualstudio.com/docs/sourcecontrol/staging-commits
- https://code.visualstudio.com/docs/sourcecontrol/repos-remotes
- https://git-scm.com/docs
