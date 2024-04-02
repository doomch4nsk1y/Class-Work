def is_year_leap(y):
    if y % 4 == 0:
        t = 'Год високосный'
    else:
        t = 'Год не високосный'
        return t
a = int(input("Введите год: "))
otvet = is_year_leap(a)
print(otvet)