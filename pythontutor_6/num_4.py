#В первый день спортсмен пробежал x километров, а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу y определите номер дня, на который пробег спортсмена составит не менее y километров.
#Программа получает на вход действительные числа x и y и должна вывести одно натуральное число
x = int(input())
y = int(input())
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)

