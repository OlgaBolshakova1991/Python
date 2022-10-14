#задача 4. Напишите простой калькулятор, который считывает с пользовательского ввода три строки: первое число,
# второе число и операцию, после чего применяет операцию к введённым числам ("первое число" "операция" "второе число") 
# и выводит результат на экран.


#Поддерживаемые операции: +, -, /, *, mod, pow, div, где
#mod — это взятие остатка от деления,
#pow — возведение в степень,
#div — целочисленное деление.

#Если выполняется деление и второе число равно 0, необходимо выводить строку "Деление на 0!".
#На вход программе приходят вещественные числа.


try:

    first_num = float (input('Введите первое число: '))
    operation = str(input('Введите операцию: '))
    second_num = float (input('Введите второе число: '))
    if (operation == '+'):
        print (first_num + second_num)
    elif (operation == '-'):
        print (first_num - second_num)
    elif (operation == '*'):
        print (first_num * second_num)
    elif (operation == '/'):
        if(second_num == 0 ):
            print ('error')
        print (first_num / second_num)
    elif (operation == 'mod'):
        if(second_num == 0 ):
            print ('error')
        print (first_num % second_num)
    elif (operation == 'pow'):
        print (first_num ** second_num)
    elif (operation == 'div'):
        if(second_num == 0 ):
            print ('error')
        print (first_num // second_num)
except:
    print("Некорректный ввод данных")

