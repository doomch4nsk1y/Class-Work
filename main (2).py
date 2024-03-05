#Задание 6
N = int(input("Введите натуральное число: "))
a = 1
while a < N:
    print(a)
    a += 1
    
#Задание 7 
a = float(input("Введите вещественное число: "))
n = 1 
sum = 0
while sum <= a:
    sum += 1/n 
    if sum > a:
        print(n)
        break
    n += 1

#Задание 8 
n = int(input("Введите натуральное число: "))
a = 1
while a**2 < n:
    if a**2 == n:
        continue
    a += 1 
    if a**2 > n:
        print("Число, возводимое в квадрат: ", a)
        print("Число в квадрате: ", a**2)
        break

#Задание 9 
a = 201
while a % 17 != 0:
    a += 1 
print(a)

#Задание 10
a = 600
while a % 28 != 0:
    a -= 1
print(a)