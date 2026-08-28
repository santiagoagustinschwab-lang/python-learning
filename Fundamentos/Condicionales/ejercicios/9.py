string = input("Introduce un str: ")

if string == "":
    print("El string no puede estar vacio")
elif len(string) < 3:
    print("El string es muy corto")
else:
    print(string.capitalize())