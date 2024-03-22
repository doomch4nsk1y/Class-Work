#Задание 1 
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(a,"Большее число")
elif a == b:
    print("Числа равны")
else:
    print(b,"Большее число")
    
#Задание 2
a = int(input("Введите первую сторону треуголника: "))
b = int(input("Введите вторую сторону треуголника: "))
c = int(input("Введите третью сторону треуголника: "))
if a + b >= c:
    print("YES")
elif a + c >= b:
    print("YES")
elif b + c >= a:
    print("YES")
else:
    print("NO")

#Задание 3 
a = int(input("Введите число: "))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("YES")
else:
    print("NO")