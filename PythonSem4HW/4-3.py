#задача 3. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
#*Пример:* 
#- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
def polynom(k):
    
    degree_of_num = []
    for i in range(0, k + 1):
        degree_of_num.append(i)

    coeff = [random.randint(0, 100) for _ in range(k + 1)]
    print (coeff)
    with open('file.txt', 'w') as m:
        for i in range(len(coeff)):
            if k - i != 1 and k - i != 0:
                m.write(f"{coeff[i]}x^{degree_of_num[k - i]} + ")
            elif k - i == 1:
                m.write(f'{coeff[i]}x + ')
            elif k - i == 0:
                m.write(f'{coeff[i]} = 0') 
    
try:
    k = int(input("Введите степень числа: "))
    polynom(k)
except:
    print ("Ошибка")


