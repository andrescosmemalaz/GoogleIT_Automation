# Practice Quiz: Branching & Merging
# Total points: 5
# Score: 100%

# Question 1
# When we merge two branches, one of two algorithms is used. If the branches have diverged, which algorithm is used?

# three-way merge
# fast-forward merge
# merge conflict
# orphan-creating merge
# A three-way-mergeoccurs when the two commits have diverged previously, and a new commit is created.


# Question 2
# The following code snippet represents the result of a merge conflict. Edit the code to fix the conflict and keep the version represented by the current branch.

print("Keep me!")

# Question 3
# What command would we use to throw away a merge, and start over?

# git checkout -b
# git merge --abort
# git log --graph --oneline
# git branch -D
# If there are merge conflicts, the --abort flag can be used to abort the merge action.


# Question 4
# How do we display a summarized view of the commit history for a repo, showing one line per commit?

# git log --format=short
# git branch -D
# git log --graph --oneline
# git checkout -b
# The command git log --graph --oneline shows a summarized view of the commit history for a repo.


# Question 5
# The following script contains the result of a merge conflict. Edit the code to fix the conflict, so that both versions are included.

def main():
    print("Start of program>>>>>>>")
    print("End of program!")

main()