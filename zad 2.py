# Задание № 2, функция Del
def Del(n, m):
    return n % m == 0


for A in range(1, 1000): #начинаем с 1, т.к. А натуральное число
    A1 = True
    for x in range(1, 1000):
        if ((not(Del(x, A))) <= (Del(x, 6) <= (not(Del(x, 9))))) == False:
            A1 = False
            break
    if A1:
        print(A)