# бот против бота



import random

def game_bot_vs_bot():
    candies = 2021
    get_max = 28
    count = 0
    step = 0
    player_1 = "Бот-Обжорка"
    print ("Имя первого игрока: Бот-Обжорка")
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
        
            if count == 0:
                print(f"Cейчас ходит {first}: ")
                
                
                if candies > get_max:
                    step = candies % (get_max + 1) 
            
                candies = candies - step
                if candies <= get_max:
                    step == candies
                    break
                print (step)
                print(f"Осталось еще {candies} конфет")
                if candies > 0:
                    count = 1
                if candies <= 0:
                    print("Конфеток больше нет")
                    break
            if count == 1:
                print(f"Cейчас ходит {second}: ")
            
                if candies <= get_max:
                    step == candies
                    break
                if candies > get_max:
                    step = step = random.randint(1, get_max)
                print (step)
                candies = candies - step
                print(f"Осталось еще {candies} конфет")
                if candies > 0:
                    count = 0
                if candies <= 0:
                    print("Конфеток больше нет")
                    break
    if count == 1:
        print(f'{second} ПОБЕДИЛ')
    if count == 0:
        print(f'{first} ПОБЕДИЛ')


game_bot_vs_bot()