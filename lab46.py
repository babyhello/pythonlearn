# make data directory
# generate a file Python_Introduction

file1 = open('data/Python_Introduction', encoding='UTF8')
data1 = file1.read()
file1.close()
print(type(file1), type(data1))
print(len(data1), data1[:50])

with open('data/Python_Introduction', encoding='UTF8') as file2:
    data2 = file2.read()

print(type(data2), len(data2), data2[:50])