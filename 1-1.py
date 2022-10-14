#задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

#1 вариант
""" 
try:
    day = int(input('Введите число '))

    if(day >= 1 and day <= 5):
        print('Будни')
    elif (day == 5 or day == 6):
        print('Выходной')
    else:
        print('Введите число от 1 до 7 ')
except:
    print('Введите число ')

 
 """


#2 вариант

try:
    day = int(input("Введите число  "))
    if(day == 1):
        print ('пн')
    elif(day == 2):
        print('вт')
    elif(day == 3):
        print('ср')
    elif(day == 4):
        print('чт')
    elif(day == 5):
        print('пт')
    elif(day == 6):
        print('сб - выходной')
    elif(day == 7):
        print('вс - выходной')
    else:
        print('Введите число от 1 до 7 ')
except:
    print('Ошибка')

 