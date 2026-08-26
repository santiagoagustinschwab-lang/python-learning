### Diccionarios ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))

# Los diccionarios sirven para almacenar datos de tipo clave, valor, osea a : b
my_other_dict = {"Nombre":"santiago", "Apellido":"schwab","Edad":17, 1:"Python"}

# Van identados
my_dict = {
    "Nombre":"santiago",
    "Apellido":"schwab",
    "Edad":17,
    "Lenguajes":{"Python", "HTML", "CSS"},
    1:1.70
    }

print(my_dict)
print(my_other_dict)

# El len imprime la cantidad de elementos clave valor
print(len(my_other_dict))

# Con corchetes llamas al valor de x clave
print(my_dict["Nombre"])

# Se puede acceder y modificar los valores de las claves
my_dict["Nombre"] = "pedro"
print(my_dict["Nombre"])

print(my_dict[1])

# Se le pueden agregar claves y valores, se agregan a lo ultimo automaticamente
my_dict["Calle"] = "Belgrano"
print(my_dict)

# Con del eliminas clave y valor
del my_dict["Calle"]
print(my_dict)

# Cuando se verifique con IN, busca la clave, no el valor, santiago este en el dict, pero como valor de "Nombre", asi que es falso
print("santiago" in my_dict)
print("Nombre" in my_dict)

# Items agrupa claves y valores en parentesis 
print(my_dict.items())

# Keys retorna solo las llaves
print(my_dict.keys())

# Values retorna los valoes de las llaves
print(my_dict.values())

# Cuando se transforma en lista imprime solo las claves
print(list(my_dict))

# A tupla lo iimprime como tupla sin mas
print(tuple(my_dict))

# Lo mismo con set
print(set(my_dict))

# Este es un dato aparte, dict_values
my_values = my_dict.values()
print(type(my_values))

print(my_values)