#За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров? Программа получает на вход числа n и m.
from math import ceil
a = int(input("введите число"))
b = int(input("введите число"))
print(ceil(b / a))