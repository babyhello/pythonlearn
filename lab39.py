import requests, bs4

URL1 = "https://dlink.com/"

r1 = requests.get(URL1)
# print(r1.content)
soup = bs4.BeautifulSoup(r1.content, "html.parser")
print(type(soup), soup.title.name, soup.title.text)
# print(soup.prettify())
courseList = soup.find('div', {'class': 'c-tiles__body'})
for course in courseList:
    print(type(course))
    print(course)
courseHeader = courseList.findAll('image')
for header in courseHeader:
    print(header.text)

courseContent = courseList.findAll('p')
for content in courseContent:
    print(content.text)

for header, content in zip(courseHeader, courseContent):
    print("[%s]==>[%s]" % (header.text, content.text))