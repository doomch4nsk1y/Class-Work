#Задание 1 
array1 = [1, 2, 3, 4, 5, 1, 2, 3, 6, 7, 8, 9, 10, 10, 11, 12, 13]
array2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 20, 21, 22, 23]
unique_array = list(set(array1 + array2))
print(unique_array)

#Задание 2 
M = int(input("Введите размерность матрицы M: "))
matrix = []
for i in range(M):
    row = list(map(int, input(f"Введите {M} элементов {i+1}-й строки через пробел: ").split()))
    matrix.append(row)
print("Матрица B:")
for row in matrix:
    print(row)
non_zero_count = sum(1 for row in matrix for elem in row if elem != 0)
print(f"Количество ненулевых элементов в матрице: {non_zero_count}")

#Задание 3 
M = int(input("Введите количество строк M: "))
N = int(input("Введите количество столбцов N: "))
matrix = []
for i in range(M):
    row = list(map(int, input(f"Введите {N} элементов {i+1}-й строки через пробел: ").split()))
    matrix.append(row)
print("Матрица D:")
for row in matrix:
    print(row)
negative_product = 1
for row in matrix:
    for elem in row:
        if elem < 0:
            negative_product *= elem

print(f"Произведение отрицательных элементов в матрице: {negative_product}")

#Задание 4 
import numpy as np

M = int(input("Введите размерность M: "))
matrix_B = np.random.randint(-10, 10, size=(M, M))
print("Матрица B:")
print(matrix_B)

positive_elements = matrix_B[matrix_B > 0]
positive_product = np.prod(positive_elements)

print(f"Произведение положительных элементов в матрице: {positive_product}")

#Задание 5 
import numpy as np

M = int(input("Введите размерность M: "))

matrix_B = np.random.randint(-10, 10, size=(M, M))

print("Матрица B:")
print(matrix_B)

min_element = np.min(matrix_B)
min_element_index = np.unravel_index(np.argmin(matrix_B), matrix_B.shape)

print(f"Минимальный элемент в матрице: {min_element}")
print(f"Его координаты: {min_element_index}")

