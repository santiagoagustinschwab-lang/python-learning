import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

title_list = []
price_list = []
books = []
num_of_pages = range(1,51)

for i in num_of_pages:
    web = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")    
    web.encoding ="utf-8"
    html = BeautifulSoup(web.text, "html.parser")

    prices = html.findAll("p", class_ = "price_color")

    titles = html.findAll("a", title = True)

    for title in titles:
        title_list.append(title["title"])    

    for price in prices:
        price_list.append(price.text)


for title, price in zip(title_list, price_list):
    book = {"title":title, "price":price}
    books.append(book)

wb = Workbook()
sheet = wb.active

for book in books:
        sheet.append([book["title"], book["price"]])

wb.save("Books.xlsx")