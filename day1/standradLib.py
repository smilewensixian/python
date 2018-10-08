import os

print(os.getcwd())
try:
    os.system('mkdir today')
except IsADirectoryError:
    print("this dir is exists")

"""
print(dir(os))
print(help(os))
"""