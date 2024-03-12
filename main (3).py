#Задание 15
import random

def get_array_size():
    size = int(input("Введите размерность одномерного массива: "))
    return size

def generate_array(size):
    array = [random.randint(0, 100) for _ in range(size)]
    return array

def square_element(element):
    return element * element

def cube_element(element):
    return element * element * element

def square_array(array):
    return [square_element(element) for element in array]

def cube_array(array):
    return [cube_element(element) для element в array]

size = get_array_size()
array = generate_array(size)
squared_array = square_array(array)
cubed_array = cube_array(array)

print("Исходный массив:", array)
print("Квадраты элементов:", squared_array)
print("Кубы элементов:", cubed_array)


#Задание 16
def get_numbers():
    numbers = []
    for _ in range(3):
        number = int(input("Введите число: "))
        numbers.append(number)
    return numbers

def find_minimum(numbers):
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum

numbers = get_numbers()
minimum = find_minimum(numbers)
print("Наименьшее число:", minimum)

#Задание 17 
def get_input():
    symbol = input("Введите символ: ")
    number = int(input("Введите целое число: "))
    return symbol, number

def calculate_remainder(symbol, number):
    return symbol % number

symbol, number = get_input()
remainder = calculate_remainder(symbol, number)
print("Остаток от деления кода введенного символа на число:", remainder)

#Задание 18 
def get_input():
    symbol = input("Введите символ: ")
    number = float(input("Введите вещественное число: "))
    return symbol, number

def calculate_integer_part(symbol, number):
    return int(number / symbol)

symbol, number = get_input()
integer_part = calculate_integer_part(symbol, number)
print("Целая часть от деления числа на код введенного символа:", integer_part)

#Задание 19 
def get_coordinates():
    x1 = float(input("Введите координату x первой вершины: "))
    y1 = float(input("Введите координату y первой вершины: "))
    x2 = float(input("Введите координату x второй вершины: "))
    y2 = float(input("Введите координату y второй вершины: "))
    x3 = float(input("Введите координату x третьей вершины: "))
    y3 = float(input("Введите координату y третьей вершины: "))
    return x1, y1, x2, y2, x3, y3

def calculate_area(x1, y1, x2, y2, x3, y3):
    a = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)
    return a

x1, y1, x2, y2, x3, y3 = get_coordinates()
area = calculate_area(x1, y1, x2, y2, x3, y3)
print("Площадь треугольника:", area)

#Задание 20 
import numpy as np

def get_array():
    array = np.random.randint(-100, 100, size=15)
    return array

def find_zero_elements(array):
    zero_elements = [i for i in range(len(array)) if array[i] == 0]
    return zero_elements

def find_last_positive_element(array):
    for i in range(len(array) - 1, -1, -1):
        if array[i] > 0:
            return i
    return None

array = get_array()
zero_elements = find_zero_elements(array)
last_positive_element = find_last_positive_element(array)

if zero_elements:
    print("Номера нулевых элементов:", zero_elements)
else:
    print("В массиве нет нулевых элементов")

if last_positive_element is not None:
    print("Номер последнего положительного элемента:", last_positive_element)
else:
    print("В массиве нет положительных элементов")
