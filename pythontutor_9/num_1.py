#Найдите индексы первого вхождения максимального элемента. Выведите два числа: номер строки и номер столбца, в которых стоит наибольший элемент в двумерном массиве.
# Если таких элементов несколько, то выводится тот, у которого меньше номер строки, а если номера строк равны то тот, у которого меньше номер столбца.
n, m = [int(i) for i in input().split()]
h, k = 0, 0
a = []
for i in range(n):
    s = input()
    a.append([int(j) for j in s.split()])

f = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > f:
            f = a[i][j]
            h = i
            k = j
print(h, k)