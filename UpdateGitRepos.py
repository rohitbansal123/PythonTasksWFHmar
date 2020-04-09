import git

repo = git.Repo('/home/ro.bansal/PycharmProjects/PythonTasksWFHmar')
#assert repo.bare == False
repo.remotes.origin.pull()
current = repo.head.commit
if current != repo.head.commit:
   print("it changed")
# checking update works or not
