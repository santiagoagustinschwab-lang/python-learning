import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

list_of_names = []
list_of_prices = []
total_data = []
num_of_pages = range(1,51)

for i in num_of_pages:
    web = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
    html = BeautifulSoup(web.text, "html.parser")

    names = html.findAll("a", title = True)
    prices = html.findAll("p", class_ = "price_color")

    for name in names:
        list_of_names.append(name["title"])

    for price in prices:
        list_of_prices.append(price.text)

for name, price in zip(list_of_names, list_of_prices):
    data = {"name":name, "price":price}
    total_data.append(data)

wb = Workbook()
sheet = wb.active

sheet.append(["Products", "Price"])

for product in total_data:
    sheet.append([product["name"], product["price"]])

wb.save("Books.xlsx")