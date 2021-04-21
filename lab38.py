import requests, bs4

URL1 = "https://www.uuu.com.tw/"

r1 = requests.get(URL1)
# print(r1.content)
soup = bs4.BeautifulSoup(r1.content, "html.parser")
print(type(soup), soup.title.name, soup.title.text)
# print(soup.prettify())
courseList = soup.find('div', {'id': 'course_list'})
for course in courseList:
    print(type(course))
    print(course)