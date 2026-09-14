import requests
from openpyxl import Workbook
from bs4 import BeautifulSoup

title_list = []
price_list = []
books = []
num_pages = range(1,52)

wb = Workbook()
sheet = wb.active

for i in num_pages:
    try:
        web = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
        if web.status_code == 404:
            raise ValueError (f"ERROR {web.status_code} in {i}")

        html = BeautifulSoup(web.text, "html.parser")

        titles = html.find_all("a", title = True)
        prices = html.find_all("p", class_ = "price_color")

        for title in titles:
            title_list.append(title["title"])

        for price in prices:
            price_list.append(price.text)

    except ValueError as error:
        print(error)

for title, price in zip(title_list, price_list):
    book = {"title":title, "price":price}
    books.append(book)

sheet.append(["TITLES", "PRICES"])

for book in books:
    sheet.append([book["title"], book["price"]])

wb.save("BOOKS.xlsx")