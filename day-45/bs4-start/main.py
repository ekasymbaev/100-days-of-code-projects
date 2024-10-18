from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
span_tags = soup.find_all(name="span", class_="titleline")


span_texts = []
span_links = []
for span_tag in span_tags:
    text = span_tag.getText()
    span_texts.append(text)
    link = span_tag.find('a')["href"]
    span_links.append(link)
# span_upvotes = soup.find_all(name="span", class_='score').getText()
span_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name = "span", class_="score")]


# print(span_texts)
# print(span_links)
# print(span_upvotes)

needed_index = span_upvotes.index(max(span_upvotes))
highest_element = []
highest_element.append(span_texts[needed_index])
highest_element.append(span_links[needed_index])
highest_element.append(span_upvotes[needed_index])


print(highest_element)















# # import lxml (if 'html.parser' does not work)
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.prettify())
# all_anchor_tags = soup.find_all(name = "a")
#
# # for tag in all_anchor_tags:
# #     print(tag.getText())
# #     print(tag.get("href"))
#
#
# # heading = soup.find(name = "h1", id="name")
# # print(heading.getText())
# #
# # section_heading = soup.find(name="h3", class_= "heading")
# # print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")