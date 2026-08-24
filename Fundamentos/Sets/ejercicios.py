#1
primer_set = set({})

primer_set.add("santiago")

primer_set.add("schwab")

primer_set.add(17)

primer_set.add(1.70)
print(primer_set)

#2
segundo_set = {1, 2, 2, 4, 5}
print(segundo_set)
# lo que paso es que al ser un set, no permite repetidos y lo omite

#3
tercer_set = {"santiago", "schwab", 17, 1.70}
print("santiago" in tercer_set)
print("santi" in tercer_set)

#4
cuarto_set = {"santiago", "schwab", 17, 1.70}
quinto_set = {17, 1.70, "parish", "rubio"}
print(cuarto_set.union(quinto_set))

#5
print(cuarto_set.difference(quinto_set))
print(quinto_set.difference(cuarto_set))