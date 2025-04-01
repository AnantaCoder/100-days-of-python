from bs4 import BeautifulSoup
# import lxml

with open('day-45 web scrapping/bs4-start/bs4-start/website.html') as file:
    contents = file.read()
    
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
print(soup.a.string)
all_anchor_tags = soup.find_all(name= 'a')

for i in all_anchor_tags:
    # print(i.getText())
    print(i.get('href'))
head = soup.find(name = 'h1' , id= 'name')
# print(head)

company_url = soup.select_one(selector='p a')
print(company_url)

name = soup.select_one(selector='#name')
print(name)
k = soup.select('.heading')
print(k)