#Задание 1 
def sum(start, end):
    if start > end:
        start, end = end, start
    total = 0
    for i in range(start, end + 1):
        total += i

    return total

result = sum(3, 7)
print(result) 

#Задание 2
def func1(x):
    y = x + 1
    return y

result = func1(3)
print(result)

def func2(x):
    result = x * y
    return result

y = 2
output = func2(3)
print(output)

def func3(x, y):
    z = x + y
    return z

result = func3(2, 5)
print(result)

#Задание 3 
def three_args(*, var1=None, var2=None, var3=None):
    args = []
    if var1 is not None:
        args.append(f"var1 = {var1}")
    if var2 is not None:
        args.append(f"var2 = {var2}")
    if var3 is not None:
        args.append(f"var3 = {var3}")

    if len(args) > 0:
        print("Переданы аргументы: " + ", ".join(args))
    else:
        print("Нет переданных аргументов")

three_args(var1=2, var3=10)
three_args(var2="Hello")
three_args(var1=5, var2="World", var3=7)

#Задание 4 
import datetime

def time_now():
    current_time = datetime.datetime.now()
    message = "Текущее время:"
    print(f"{message} {current_time}")

time_now()
time_now()

#Задание 5
import datetime

def time_now():
    current_time = datetime.datetime.now()
    message = "Текущее время:"
    print(f"{message} {current_time}")


time_now()
time_now()



