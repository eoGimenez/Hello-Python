# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=10172

### Higher Order Functions ###

from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

### Closures ###


def sum_ten(original_value):
    print("ORIGINAL",original_value)
    def add(value):
        return value + 10 + original_value
    return add


add_closure = sum_ten(1)
print(add_closure(5))
print("??????",(sum_ten(1))(5)) # el orden de los valoers a las funciones closures es en el mismo orden en el que estan declaradas 

### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 3, 30]

# Map


def multiply_two(number):
    return number * 2

""" impresion = map(lambda number: number *2, numbers)
print("la lambda", type(impresion))  class 'map' 
para que tenga sentido hay que asignarlo a una lista
"""
print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))
testeandola = (list(filter(lambda number: number > 10, numbers))) # nos guardamos los resultados true en la nueva lista 
print("TESTEANDOLA",testeandola) # OK
# Reduce


def sum_two_values(first_value, second_value):
    return first_value + second_value


print(reduce(sum_two_values, numbers))
reduciendola = reduce(lambda numb, number: numb + number, numbers)
#no muta la array original,
print(reduciendola) 