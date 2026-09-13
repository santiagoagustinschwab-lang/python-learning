#https://books.toscrape.com/catalogue/page-1.html

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

titles_list = []
price_list = []
books = []
num_pages = range(1,51)
wb = Workbook()
sheet = wb.active

for i in num_pages:
    web = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    html = BeautifulSoup(web.text, "html.parser")

    titles = html.findAll("a", title = True)
    prices = html.findAll("p", class_ = "price_color")

    for title in titles:
        titles_list.append(title["title"])

    for price in prices:
        price_list.append(price.text)

for title, price in zip(titles_list, price_list):
    book = {"title":title, "price":price}
    books.append(book)

sheet.append(["TILES", "PRICES"])

for book in books:
    sheet.append([book["title"], book["price"]])

wb.save("Books.xlsx")