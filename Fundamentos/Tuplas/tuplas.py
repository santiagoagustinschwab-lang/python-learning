### tupolas ###

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35, 1.70, "santiago", "schwab")
my_other_tuple = (35, 40, 60)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

# count cuenta cuantas veces hay x
print(my_tuple.count("schwab"))

# index dice en que pocision esta x
print(my_tuple.index("schwab"))

# las tuplas son constantes e inmutables, almacenan datos pero no se modifican
#my_tuple[1] = 1.80
#print(my_tuple)

# se pueden concatenar y se almacenan todos los datos en una
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

# se pueden acceder a los datos concatenados
print(my_sum_tuple[3:6])

# se le puede cambiar el tipo a lista por ejemplo, sirve para agregar datos, solo casos especificos
my_tuple = list(my_tuple) 
print(type(my_tuple))

my_tuple[3] = "nuevo"
my_tuple.insert(1, "nuevo 2")

# luego de modificar los datos, puede volver a ser tupla
my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

del my_tuple
print(my_tuple)