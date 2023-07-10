# Задание № 4, гибридный тип, Демоверсия 2023

def Del(n, m):
    return n % m == 0

for A in range(1, 1000):
    A1 = True
    for x in range(1, 1000):
        if ((Del(x, 2) <= (not(Del(x, 3)))) or (x + A >= 100)) == False:
            A1 = False
            break
    if A1:
        print(A)
        break