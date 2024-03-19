#Задание 1 
def triangle_area(x1, y1, x2, y2, x3, y3):
    a = sqrt((x2-x1)**2 + (y2-y1)**2)
    b = sqrt((x3-x2)**2 + (y3-y2)**2)
    c = sqrt((x1-x3)**2 + (y1-y3)**2)
    s = (a + b + c) / 2.0
    return sqrt(s * (s-a) * (s-b) * (s-c))

#Задание 2 
array = [5, 0, -3, 0, 7, 0, 0, 2, -1, 0, 4, 0, 9, -2, 0]

zero_indices = [i for i, num in enumerate(array) if num == 0]
last_positive_index = max([i for i, num in enumerate(array) if num > 0])

print("Номера нулевых элементов массива:", zero_indices)
print("Номер последнего положительного элемента:", last_positive_index)

#Задание 3 
array = [int(input(f"Введите элемент {i+1}: ")) for i in range(17)]

summa = 0
for num in array:
    if num < 0:
        break
    summa += num

print("Сумма всех элементов до первого отрицательного:", summa)

#Задание 4

array1 = [int(input(f"Введите элемент {i+1} для первого массива: ")) for i in range(10)]
array2 = [int(input(f"Введите элемент {i+1} для второго массива: ")) for i in range(10)]

if array1 == array2:
    print("Массивы равны.")
else:
    print("Массивы не равны.")

if array1 != array2:
    print("Массивы неравны.")
else:
    print("Массивы равны.")

#Задание 5
array = [int(input(f"Введите элемент {i+1} для массива: ")) for i in range(20)]
indexes_of_zeros = [i for i, x in enumerate(array) if x == 0]

print("Номера нулевых элементов в массиве:", indexes_of_zeros)

