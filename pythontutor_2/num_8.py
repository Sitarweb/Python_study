#Шахматный слон ходит по диагонали.
# Даны две различные клетки шахматной доски, определите, может ли слон попасть с первой клетки на вторую одним ходом.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if abc(a - b) == abs(c - d):
    print("yes")
else:
    print("no")