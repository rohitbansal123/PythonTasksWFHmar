import git

repo = git.Repo('/home/ro.bansal/PycharmProjects/PythonTasksWFHmar')
assert repo.bare == False
#repo.remotes.origin.pull()
print(repo.remotes.origin.pull())

