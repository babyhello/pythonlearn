course = {'name': "BDPY"}
print(course['name'])
# print(course['instructor'])
print('instructor' in course)
if 'instructor' in course:
    print(course['instructor'])
else:
    print(False)

Bs = [True, False, 100, 3.14, None, "hello world"]

for b in Bs:
    print(True and b)