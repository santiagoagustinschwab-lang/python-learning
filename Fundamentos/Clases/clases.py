### Clases ###

class MyEmptyPerson:
    pass

print(MyEmptyPerson)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.edad = 17

my_person = Person("Santiago", "Schwab")
print(f"mi nombre es {my_person.name} {my_person.surname} y tengo {my_person.edad}")

class Persona:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname}, ({alias})"
        self.__name = name

    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} esta caminando")

mi_persona = Persona("santiago", "Schwab", "Santi")
print(mi_persona.full_name)
print(mi_persona.get_name())

mi_persona.walk()

my_other_person = Persona("Ricardo", "Schwab")
my_other_person.full_name = "nicolas artem (el joyero uncraniano)"
print(my_other_person.full_name)
my_other_person.walk()