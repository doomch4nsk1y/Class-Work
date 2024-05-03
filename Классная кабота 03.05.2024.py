#Задание 30
import numpy as np
M = 3
N = 4
B = np.random.randint(-10, 10, size=(M, N))
print("Матрица B:")
print(B)
positive_product = 1
for row in B:
    for element in row:
        if element > 0:
            positive_product *= element

print("Произведение положительных элементов матрицы B:", positive_product)

#Задание 31
import numpy as np
M = 4
N = 5
B = np.random.randint(0, 100, size=(M, N))
print("Матрица B:")
print(B)

min_element = np.min(B)
min_index = np.unravel_index(np.argmin(B), B.shape)

print("Минимальный элемент матрицы B:", min_element)
print("Его координаты:", min_index)

#Задание 32
import numpy as np
M = 3
N = 4
D = np.random.randint(0, 100, size=(M, N))
print("Матрица D:")
print(D)
min_index = np.unravel_index(np.argmin(D), D.shape)
max_index = np.unravel_index(np.argmax(D), D.shape)
D[min_index], D[max_index] = D[max_index], D[min_index]
print("\nМатрица D после замены минимального и максимального элементов:")
print(D)

#Задание 33 
import numpy as np
M = 5
N = 4
P = np.random.randint(1, 10, size=(M, N))
print("Матрица P:")
print(P)
column_products = np.prod(P, axis=0)
print("\nПроизведения элементов каждого столбца матрицы:")
print(column_products)

#Задание 34
import numpy as np
M = 4
N = 5
F = np.random.randint(-10, 10, size=(M, N))
print("Матрица F:")
print(F)
negative_counts = np.sum(F < 0, axis=1)
print("\nКоличество отрицательных элементов в каждой строке матрицы:")
print(negative_counts)



