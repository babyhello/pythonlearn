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

file3 = open('data/clone1', 'w', encoding='UTF8')
file3.write(data1)
file3.close()

with open('data/clone2','w',encoding='UTF8') as file4:
    file4.write(data2)