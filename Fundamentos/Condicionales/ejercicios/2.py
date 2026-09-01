#2
producto = {
    "Stock":5,
}

if producto["Stock"] == 0:
    print("Sin stock")
elif producto["Stock"] < 5:
    print("Ultimas unidades")
else:
    print("Disponible")