#Задача 1
def schet ():
    a = input("Введите первое число: ")
    a = float(a)
    b = input("Введите второе число: ")
    b = float(b)
    c = input("Введите третье число: ")
    if a > b:
        print(a - b)
    else:
        print(b - a)
    return a,b
    if a > c:
        print(a - c)
    else:
        print(c - a)
    return a, c
    if b > c:
        print (b - c)
    else:
        print(c - b)
    return b, c

c, d = schet ()
e, f = schet ()
z, x = schet ()
