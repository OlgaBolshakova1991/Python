# человек против бота


import random

def game_player_vs_bot():
    candies = 2021
    get_max = 28
    count = 0
    step = 0
    player_1 = input("Имя первого игрока: ")
    player_2 = "Бот-Сладкоежка"
    print ("Имя второго игрока: Бот-Сладкоежка")
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
        if first == player_1:
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
                print(f"Cейчас ходит {second}: ")
                if get_max <= candies:
                    
                    step = candies % (get_max + 1)
                if candies < get_max:
                    step == candies
                
                print (step)
                
                candies = candies - step
            if candies > 0:
                print(f"Осталось еще {candies} конфет")
                count = 0
            else:
                print("Конфеток больше нет")



        if first == player_2:
            if count == 0:
                print(f"Cейчас ходит {first}: ")
                if candies > get_max:
                    step = candies % (get_max + 1)
                    if candies <= get_max:
                        step == candies
                    
                    print (step)
                
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
        print(f'{second} ПОБЕДИЛ')
    if count == 0:
        print(f'{first} ПОБЕДИЛ')

game_player_vs_bot()
