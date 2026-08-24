### sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # inicialmente es un diccionario ( dict )

my_other_set = {"santiago", "schwab", 17}
print(type(my_other_set))

print(len(my_other_set))

# un set no es una estructura ordenada
my_other_set.add("MoureDev")
print(my_other_set)

# un set no admite repetidos
my_other_set.add("MoureDev")
print(my_other_set)

# se puede corroborar si existen elementos en los set, los resultados son booleanos
print("santiago" in my_other_set)
print("santiag" in my_other_set)

# tambien se pueden remover elementos
my_other_set.remove("santiago")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_set = {"santiago", "schwab", 17}
my_list = list(my_set)
print(my_list)

my_other_set = {"HTML", "CSS", "Python"}

# cojn union se pueden concatenar
my_new_set = my_set.union(my_other_set)
print(my_new_set)

# con diference te dice la diferencia de x con y, imprime x
print(my_other_set.difference(my_set))