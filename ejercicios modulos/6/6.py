import random

numero = random.randint(1, 10)

try:
    print(numero / 100)
except ZeroDivisionError:
    print("no se puede dividir por 0")