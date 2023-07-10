#Задание № 1 на поразрядную конъюнкцию

for A in range(1000):
    A1 = True
    for x in range(1000):
        if ((x & 105 == 0) <= ((x & 58 != 0) <= (x & A != 0))) == False:
            A1 = False
            break
    if A1:
        print(A)
