### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print("Se detiene la condicion")
        break
    print(my_condition)

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (35, 1.70, "santiago", "schwab")

for element in my_tuple:
    print(element)

my_set = {"santiago", "schwab", 17}

for element in my_set:
    print(element)

my_dict = {"Nombre":"santiago", "Apellido":"schwab","Edad":17, 1:"Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para mi diccionario finalizo")