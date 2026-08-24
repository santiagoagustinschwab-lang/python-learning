#1
primera_tupla = ("santiago", "schwab", 17, 1.70)
print(primera_tupla[0])
print(primera_tupla[3])
#2
primera_tupla = ("santiago", "schwab", 17, 1.70, "santiago")
print(primera_tupla.count("santiago"))

#3
print(primera_tupla.index(17))

#4
segunda_tupla = ("compu", "celu", "tele")
tercera_tupla = ("mate", "termo", "plato")
dos_tuplas = segunda_tupla + tercera_tupla
print(dos_tuplas[1:4])

#5
primera_tupla = list(primera_tupla)
primera_tupla = ("santiago", "schwab", 17, 1.70, "rubio")
primera_tupla = tuple(primera_tupla)
print(primera_tupla)
