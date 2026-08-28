#7
usuario = input("Introduce tu usuario: ")
contraseña = input("Introduce tu contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido")
else:
    print("Acceso denegado")