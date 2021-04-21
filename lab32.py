import os
import sys

path = "中文working"
print(os.getcwd())

os.mkdir(path)
os.chdir(path)
print("after cd, path=", os.getcwd())
os.chdir("..")
os.rmdir(path)
print(sys.argv)
print(sys.executable)