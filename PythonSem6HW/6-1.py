# Крестики-нолики

X='X'
O='0'
razmer_doski=9
step=' '
nobody='Ничья'

def instrukciya():
    print('''
Поиграем в "Крестики-нолики"!
Чтобы сделать ход, введи номер ячейки,
куда хочешь поставить свой символ:

0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8


''')

def nachalo(vopros):
    otvet=None
    while otvet not in ('да','нет'):
        otvet=input(vopros).lower()
    return otvet

def first_step():
    perviy_hod=nachalo("Хочешь сделать первый ход? Да или нет?  ")
    if perviy_hod=='да':
        print('Хорошо, ты играешь крестиками!')
        human=X
        comp=O
    else:
        print('Хорошо, я делаю первый ход крестиками')
        human=O
        comp=X
    return comp, human
        
def hod_number(low,high):
    otvet=None
    while otvet not in range(low,high):
        otvet=int(input("Делай свой ход (введи номер ячейки от 0 до 8): "))
    return otvet


def new_doska():
    doska=[]
    for i in range(razmer_doski):
        doska.append(step)
    return doska

def pokaz_doski(doska):
    print('\n', doska[0], '|', doska[1], '|', doska [2])
    print('---------')
    print('\n'
          , doska[3], '|', doska[4], '|', doska [5])
    print('---------')
    print('\n', doska[6], '|', doska[7], '|', doska [8], '\n')

def dostupnie_hodi(doska):
    dostupnie_hodi=[]
    for i in range(razmer_doski):
        if doska[i]== step:
            dostupnie_hodi.append(i)
    return dostupnie_hodi

def winner(doska):
    config=((0,1,2),
            (3,4,5),
            (6,7,8),
            (0,3,6),
            (1,4,7),
            (2,5,8),
            (0,4,8),
            (2,4,6))
    for i in config:
        if doska[i[0]]==doska[i[1]]==doska[i[2]]!=step:
            winner=doska[i[0]]
            return winner
        if step not in doska:
            return nobody
    return None
def human_hod(doska,human):
    dostupnie=dostupnie_hodi(doska)
    hod=None
    while hod not in dostupnie:
        hod=hod_number(0,razmer_doski)
        if hod not in dostupnie:
            print('Поле занято. Напиши другой номер: ')
    print('Отлично!')
    return hod
def comp_hod(doska,comp,human):
    doska=doska[:]
    best_step=(4,0,2,6,8,1,3,5,7)
    print('Мой ход: ')
    for i in dostupnie_hodi(doska):
        doska[i]=comp
        if winner(doska)==comp:
            print(i)
            return i
        doska[i]=step
    for j in dostupnie_hodi(doska):
        doska[j]=human
        if winner(doska)==human:
            print(j)
            return j
        doska[j]=step
    for k in dostupnie_hodi(doska):
        print(k)
        return k
def next_ochered(ochered):
    if ochered==X:
        return O
    else:
        return X
def pozdrav_pobeditela(pobeditel,comp,human):
    if pobeditel!=nobody:
        print('Выстроена линия ', pobeditel)
    else:
        print(nobody)
    if pobeditel==comp:
        print('Компьютер выиграл!')
    elif pobeditel==human:
        print('Ты победил!')
    elif pobeditel==nobody:
        print(nobody)
def main():
    instrukciya()
    comp,human=first_step()
    ochered=X
    doska=new_doska()
    pokaz_doski(doska)
    while not winner(doska):
        if ochered==human:
            hod=human_hod(doska,human)
            doska[hod]=human
        else:
            hod=comp_hod(doska,comp,human)
            doska[hod]=comp
        pokaz_doski(doska)
        ochered=next_ochered(ochered)
    pobeditel=winner(doska)
    pozdrav_pobeditela(pobeditel,comp,human)

#
main()
input('\n Нажми Entr, чтобы выйти')