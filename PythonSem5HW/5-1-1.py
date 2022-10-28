#задача 1. Создайте программу для игры с конфетами человек против человека.

#Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
#За один ход можно забрать не более чем 28 конфет.
#Все конфеты оппонента достаются сделавшему последний ход. 
#Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# человек против человека


import random

def game_player_vs_player():
    candies = 2021
    get_max = 28
    count = 0
    player_1 = input("Имя первого игрока: ")
    player_2 = input("Имя второго игрока:")


    print("Определим, кто ходит первый!")
    x = random.randint(1, 2)
    if x == 1:
        first = player_1
        second = player_2
    else:
        first = player_2
        second = player_1
    print(f"{first} ходит первый!")

    while candies > 0:
        if count == 0:
            step = int(input(f"Cейчас ходит {first}: "))
            if step > candies or step > get_max:
                step = int(input(f"Можно взять только {get_max} конфет. Еще одна попытка: "))
            candies = candies - step
        if candies > 0:
            print(f"Осталось еще {candies} конфет")
            count = 1
        else:
            print("Конфеток больше нет")

        if count == 1:
            step = int(input(f"Cейчас ходит {second}: "))
            if step > candies or step > get_max:
                step = int(input(f"Можно взять только {get_max} конфет. Еще одна попытка: "))
            candies = candies - step
        if candies > 0:
            print(f"Осталось еще {candies} конфет")
            count = 0
        else:
            print("Конфеток больше нет")

    if count == 1:
        print(f'{second} победитель! УРА!!!')
    if count == 0:
        print(f'{first} победитель! УРА!!!')

game_player_vs_player()
