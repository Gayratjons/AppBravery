from bs4 import BeautifulSoup
# import lxml

with open(r"C:\Python\AppBravery\AppBravery-2\Days 45-58\Day 45\index.html") as file:
    contents = file.read()
soup = BeautifulSoup(contents, 'html.parser')
# print(soup.prettify())

all_anchor_tags = soup.find_all(name="p")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())

heading = soup.find(name="h1")
# print(heading) 

portal_url = soup.select_one(selector="p a")
# print(portal_url)

