#задача 1. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


def find_simple_multiplier(n):
    
    simple_multiplier = []
    divider = 2
    if n > 0:
        while(divider <= n):
            if (n % divider == 0):
                simple_multiplier.append(divider)
                n = n / divider
            else:
                divider += 1
        return simple_multiplier

try:
    n = int(input("Введите число: "))
    print(find_simple_multiplier(n))
except: 
    print("Ошибка. Введите натуральное число.")
            