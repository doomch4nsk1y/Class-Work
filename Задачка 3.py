#Задача 3
def zagadka ():
    a = "Рюкзак"
    print("Отгадай первую загадку!Висит груша, нельзя скушать: ")
    b = input()
    if b == a:
        print("Верно")
    else:
        print("Неверно")
    return a, b 
c, d = zagadka ()
def zagadka2 ():
    a = "Шоколад"
    print("Очень сладкая штука, от которой попа слипается")
    b = input()
    if b == a:
        print("Верно")
    else:
        print("Неверно")
    return a, b
c, d = zagadka2 ()
def zagadka3 ():
    a = "Яйцо"
    print("Без петель и замков. Белый дом. Слиток золота спрятан в нём")
    b = input()
    if b == a:
        print("Верно")
    else:
        print("Неверно")
    return a, b
c, d = zagadka3 ()    