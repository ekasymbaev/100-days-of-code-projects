from bs4 import BeautifulSoup
# import lxml (if 'html.parser' does not work)
with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup.prettify())
all_anchor_tags = soup.find_all(name = "a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))


heading = soup.find(name = "h1", id="name")
print(heading.getText())

section_heading = soup.find(name="h3", class_= "heading")
print(section_heading.getText())