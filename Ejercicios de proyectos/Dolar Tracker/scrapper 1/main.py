import requests
import openpyxl
from openpyxl import Workbook
from bs4 import BeautifulSoup 
from datetime import datetime

price_list = []

web = requests.get("https://dolarhoy.com/cotizacion-dolar-blue")
html = BeautifulSoup(web.text, "html.parser")

prices = html.find_all("div", class_ = "value")

for price in prices:
    price_list.append(price.text[1:])

now = datetime.now().strftime("%d/%m/%y %H:%M")

try:
    wb = openpyxl.load_workbook("DolarTracker.xlsx")
except FileNotFoundError:
    wb = Workbook()
    sheet = wb.active
    sheet.append(["FECHA", "COMPRA", "VENTA"])
    wb.save("DolarTracker.xlsx")

sheet = wb.active
sheet.append([now, price_list[0], price_list[1]])

wb.save("DolarTracker.xlsx")