#задача 3. Напишите программу, удаляющую из текста все слова, содержащие "абв". Функции FIND и COUNT юзать нельзя.

def del_str():
    return 'abc' in i

text = input("Введите текст: ") 
text = text.split()
new_text = ''
for i in text:
    if 'abc' not in i:
        new_text += i + ' '
print(new_text)

