# Listas
# Se denominan como variables, pueden estar dentro de corchetes o parentises
my_list =  list()
my_other_list = []

# La longitud de la lista depende de su contenido, no caracteres, si hay 2 datos, su logitud es de 2
print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]
print(len(my_list))

# Las listas pueden almacenar distitos tipos de datos, str, int, floats, etc
my_other_list = [17, 1.73, "Santiago", "Schwab"]
print(type(my_list))

# Acceder a distintas pocisiones
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1]) # con negativos va de derecha a izquierda, tomando el primer numero (de la parte derecha) como "1"
print(my_other_list[-3])

# count cuenta la cantidad de veces que aparece el valor x
print(my_other_list.count("Schwab"))
print(my_list.count(30))

# Dependiendo de la pocicion en la que este cada variable va a tomar el valor que este en esa pocicion en la lista, en my other list, el 3r valor es "santiago", asi que si imprimo name, es esta en la 3ra poscicion imprimira santiago
edad, altura, nombre, apellido = my_other_list
print(nombre)

# Se pueden asignar pocisiones asi, pero es un quilombo no recomendable
nombre, altura, edad, apellido = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(edad)

# Se pueden concatenar
print(my_list + my_other_list)


# Una lista con un str, es de clase str no list
my_list = "hola python"
print(my_list)
print(type(my_list))
# Pero si le defino q es si es una lista
my_list_lts = list("hola python")
print(type(my_list_lts))

# append aparece una variable x al final
my_other_list.append("Aparte")
print(my_other_list)

# insert inserta en x poscicion x variable
my_other_list.insert(1, "azul")
print(my_other_list)

# remove elimina x variable
my_other_list.remove("azul")
print(my_other_list)

# pop remueve la ultima variable
my_other_list.pop()
print(my_other_list)
# si imprimimos pop nos los devuelve
print(my_other_list.pop())

