import os
cwd = os.getcwd()
print(cwd)
os.chdir("..")
cwd = os.getcwd()
newwd = os.path.join(cwd,"..")
print(cwd)
print(newwd)