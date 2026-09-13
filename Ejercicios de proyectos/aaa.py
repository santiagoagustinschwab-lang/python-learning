import requests
from openpyxl import workbook
from bs4 import BeautifulSoup

title_list = []
price_list = []
books = []
num_pages = range(1,5)

for i in num_pages:
    try:
        web = requests.get(f"https://books.toscrape.com/catalogue/page-{i}.html")
        if web.status_code == 404:
            raise ValueError(f"Error {web.status_code}")
    except ValueError as error:
        print(error)