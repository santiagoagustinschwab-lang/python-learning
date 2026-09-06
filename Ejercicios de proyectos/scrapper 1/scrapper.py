import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

web = requests.get("http://quotes.toscrape.com/")
web.encoding = "utf-8"

html = BeautifulSoup(web.text, "html.parser")

phrases = html.findAll("span", class_ = "text")
authors = html.findAll("small", class_ = "author")

list_of_phrases = []
list_of_authors = []
quotes = []

for phrase in phrases:
    list_of_phrases.append(phrase.text)

for author in authors:
    list_of_authors.append(author.text)

for phrase, author in zip(list_of_phrases, list_of_authors):
    quote = {"phrase":phrase, "written by": author}
    quotes.append(quote)

print(quotes)

wb = Workbook()
sheet = wb.active

sheet.append(["quote", "author"])

for quote in quotes:
    sheet.append([quote["phrase"], quote["written by:"]])

wb.save("quotes.xlsx")