acumulador_1 = 0
acumulador_2 = 0


for i in range(101):
    if i % 2 == 0:
        acumulador_1 = acumulador_1 + i
    elif i % 2 == 1:
        acumulador_2 = acumulador_2 + i

print(f"La suma de todos los pares es: {acumulador_1} y la suma de todos los impares es {acumulador_2}")
