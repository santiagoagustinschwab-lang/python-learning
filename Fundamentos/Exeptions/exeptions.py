### Exepciones ###

numberOne = 5
numberTwo = 1
numberTwo = "1"
try:
    print(numberOne + numberTwo)
    print("no se ah producido un error")
except:
    print("se ah producido un error")


try:
    print(numberOne + numberTwo)
    print("no se ah producido un error")
except:
    print("se ah producido un error")
else:
    print("La ejecucion continua correctamente")
finally:
    print("La ejecucion continua")

try:
    print(numberOne + numberTwo)
    print("no se ah producido un error")
except ValueError:
    print("se ah producido un error de valor")
except TypeError:
    print("se ah producido un error tipado")

try:
    print(numberOne + numberTwo)
    print("no se ah producido un error")
except ValueError as error:
    print(error)
except Exception as exception:
    print(exception)
