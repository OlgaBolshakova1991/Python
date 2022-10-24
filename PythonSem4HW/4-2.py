#задача 2 . Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
def unique_digit(n):
    
    arr = []

    for i in range(n):
        arr.append(int(input()))
        
    print(arr)

    new_arr = []
    for j in arr:
        count = 0
        for k in arr:
            if j == k:
                count += 1
        if count == 1:
            new_arr.append(j)  
    return new_arr

try:
    n = int (input("Введите размер последовательности чисел: "))
    print (unique_digit(n))
except:
    print("Ошибка. Некорректный ввод данных")



