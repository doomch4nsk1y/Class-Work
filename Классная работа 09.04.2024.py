#Задание 35
import numpy as np 
matrix = np.random.randint(-10,10,(7,4))
print("Сгенерированная матрица: ")
print(matrix)
sums = np.array([sum(row[row > 0])for row in matrix])
print("Массив сумм положительных элементов каждой строки:")
print(sums)

#Задание 37
import numpy as np

M = 4
N = 5 

matrix = np.random.randint(0,10,(M, N))

print("Сгенерированная матрица:")
print(matrix)

counts = np.array([np.count_nonzero(row) for row in matrix])
print(" Массив количества нулевых элементов каждой строки:")
print(counts)

#Задание 39
import numpy as np
 M = 3
 N = 4
 
 matrix = np.random.randint(0,10,(M, N))
 
 print("Сгенерированная матрица:")
 print(matrix)
 
 min_elements = np.min(matrix, axis=1)
 print("Массив минимальных элементов каждой строки матрицы:")
 print(min_elements)
 
 #Задание 40
 import numpy as np
 M = 3 
 N = 4 
 matrix = np.random.randint(0,10, (M,N))
 print("Сгенерированная матрица:")
 print(matrix)
 non_zero_counts = np.count_nonzero(matrix, axis=1)
 print("Массив количества нулевых элементов каждой строки матрицы:")
 print(non_zero_counts)
 
 #Задание 43.1 
 import numpy as np
 M = 4 
 N = 3 
 matrix = np.random.randint(0,10, (M,N))
 print("Сгенерированная матрица:")
 print(matrix)
 zero_counts = np.sum(matrix == 0, axis=1)
 print("Массив количества нулевых элементов каждой строки матрицы:")
 print(zero_counts)
 
 #Задание 43.2
 import numpy as np
 M = 4 
 N = 3 
 matrix = np.random.randint(0,10, (M,N))
 print("Сгенерированная матрица:")
 print(matrix)
 nonzero_counts = np.sum(matrix != 0, axis=0)
 print("Массив количества нулевых элементов каждого столбца матрицы:")
 print(nonzero_counts)
 