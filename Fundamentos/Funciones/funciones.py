### Funciones ###

def my_function ():
    print("Esto es una funcion")

my_function ()
my_function ()
my_function ()

def sum_two_values (first_value, second_value):
    print(first_value + second_value)

sum_two_values(1, 2)
sum_two_values("a", "f")
sum_two_values(1.4, 5.2)

def sum_two_values_with_return (first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name(surname = "Santiago", name = "Schwab")


def print_name_with_default (name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Santiago", "Schwab", "Santi")
print_name_with_default("Santiago", "Schwab")

def print_upper_texts (*texts):
    for text in texts:
        print(text.upper())

print_upper_texts("Hola", "python", "Santi")

def print_nums (*nums):
    for numeros in nums:
        print(numeros)

print_nums(1,2,3,4)