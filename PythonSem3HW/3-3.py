#Задача 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной 
# части элементов.

#*Пример:*

#- [1.1, 1.2, 3.1, 5, 10.01] => 0.19


def find_diff_fract_max_min(n):
    
    list = []
    fract_num = []
   
    for i in range(n):
        list.append(float(input()))
        fract_num.append(list[i] - int (list[i]))

    min = fract_num[0]
    max = fract_num[0]
    for i in range(1, n):
        if (fract_num[i] > max):
            max = fract_num[i]

        if (fract_num[i] < min):
            min = fract_num[i]
    return (max - min)

try: 
    n = int (input("Введите количество элементов списка: "))   
    print("Введите элементы списка: ")
    print (f"Разница между максимальным и минимальным значением дробной части заданных элементов равна {round(find_diff_fract_max_min(n), 2)}")

except:
    print("Ошибка. Список задан неверно.")

