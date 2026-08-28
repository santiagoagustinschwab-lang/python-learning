#8
persona = {
    "Nombre":"Santiago",
    "Edad":17,
}

if "Email" in persona:
    print("Email esta en persona")
else:
    email = input("Introduce tu mail")
    persona["Mail"] = email
    print(persona)
