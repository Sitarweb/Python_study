#Шахматный ферзь ходит по диагонали, горизонтали или вертикали.
# Даны две различные клетки шахматной доски, определите, может ли ферзь попасть с первой клетки на вторую одним ходом
a = int(input("введите число"))
b = int(input("введите число"))
c = int(input("введите число"))
d = int(input("введите число"))
if abs(a - b) == abs(c - d) or a == b or c == d:
    print("yes")
else:
    print("no")