import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

web = requests.get("https://webscraper.io/test-sites/e-commerce/static/phones")
web.encoding = "utf-8"

html = BeautifulSoup(web.text, "html.parser")

products = html.findAll("a", itemprop = "name")
prices = html.findAll("span", itemprop = "price")

products_list = []
prices_list = []
all_info = []

for product in products:
    products_list.append(product.text.strip())

for price in prices:
    prices_list.append(price.text)

for product, price in zip(products_list, prices_list):
    all = {"product":product, "price":price}
    all_info.append(all)

wb = Workbook()
sheet = wb.active

sheet.append(["PRODUCTS", "PRICES"])

for i in all_info:
    sheet.append([i["product"], i["price"]])

wb.save("Products.xlsx")