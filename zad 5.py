# Задание № 5, отрезки

D = list(range(17, 59))
C = list(range(29, 81))
A = []
for x in range(1, 100):
    if ((x in D) <= (((not(x in C)) and (not(x in A))) <= (not(x in D)))) == False:
        A.append(x)
print(A)

