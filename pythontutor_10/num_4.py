#Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.
a = set()
for i in input().split():
    if i in a:
        print("Yes")
    else:
        print("No")
        a.add(i)