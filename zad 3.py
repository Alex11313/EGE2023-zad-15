# Задание № 3, три переменных х, у, А

for A in range(1, 1000):
    A1 = True
    for x in range(1000):
        for y in range(1000):
            if ((2 * x + y != 70) or (x < y) or (A < x)) == False:
                A1 = False
                break
    if A1:
        print(A)
