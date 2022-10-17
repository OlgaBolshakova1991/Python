#Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.

""" def find_sum_digit(num):
        sum = 0
        while (num != 0):
                sum += num % 10
                num //= 10
        
        print (sum)
        return (sum)

num = float(input("Введите число: "))
sum = find_sum_digit(num)
 """

def find_sum_digit(num):
        
        sum = 0
        for i in num:
                if i.isdigit():
                        sum += int(i)     
        print (sum)
        return (sum)

num = input("Введите число: ")
sum = find_sum_digit(num) 