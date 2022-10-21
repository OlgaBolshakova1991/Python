#Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#*Пример:*

#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]



def find_multiply_of_couple_elem(n):
    a = []
    m = []

    for i in range(n):
        a.append(int(input()))

    for i in range(len(a) // 2 + len(a) % 2):
            multiply = a[i] * a[-1 - i]
            m.append(multiply)
        
    return (m)

try:   
    n = int (input("Введите количество элементов списка: "))
    print("Введите элементы списка: ")
    print(f"Произведение пар чисел списка равно {find_multiply_of_couple_elem(n)}")

except:
    print("Ошибка. Введите число.")
