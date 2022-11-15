#Задача 2. Напишите программу вычисления арифметического выражения заданного строкой. Используйте операции +,-,/,*. приоритет операций стандартный.

#*Пример:* 

#2+2 => 4; 

#1+2*3 => 7; 

#1-2*3 => -5;

# Добавьте возможность использования скобок, меняющих приоритет операций.

 #   *Пример:* 

  #  1+2*3 => 7; 

   # (1+2)*3 => 9;



def add(a, b):
    return a + b

def diff(a, b):
    return a - b

def mult(a, b):
    return a * b

def delim(a, b):
    return a / b

def app(txt):
    sign = ''
    for s in '+-*/':
        if s in txt:
            sign = s
            break
    if sign == '':
        return int(txt)
    else:
        a, b = txt.split(sign)
        if sign == '*': return mult(app(a), app(b))
        elif sign == '/': return delim(app(a), app(b))
        elif sign == '+': return add(app(a), app(b))
        elif sign == '-': return diff(app(a), app(b))

print (app(input()))