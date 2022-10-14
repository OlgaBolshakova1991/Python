#Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


try:
    X = bool(input())
    Y = bool(input())
    Z = bool(input())
    
    if (not(X or Y or Z) == (not X and not Y and not Z)):
        print ('True')
    else:
        print ('False')
except:
    print ('error')
 
