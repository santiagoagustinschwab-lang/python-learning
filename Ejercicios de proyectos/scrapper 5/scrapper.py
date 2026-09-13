import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

titles_list = []
prices_list = []
books = []

num_pages = range(1,51)

wb = Workbook()
sheet = wb.active

for i in num_pages:
    try:
        web = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")

        if web.status_code == 404:
            raise ValueError(f"Error {web.status_code}")

        html = BeautifulSoup(web.text, "html.parser")

        titles = html.find_all("a", title = True)
        prices = html.find_all("p", class_ = "price_color")

        for title in titles:
            titles_list.append(title["title"])

        for price in prices:
            prices_list.append(price.text)

    except ValueError as error:
        print(f"Error {error}")

for title, price in zip(titles_list, prices_list):
    book = {"titles":title, "prices":price}
    books.append(book)

sheet.append(["TITLES", "PRICES"])

for book in books:
    sheet.append([book["titles"], book["prices"]])

wb.save("Books.xlsx")