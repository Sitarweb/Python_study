# Дан список, упорядоченный по неубыванию элементов в нем. Определите, сколько в нем различных элементов.
s = 1
n = input()
a = [n for n in n.split()]
for i in range(len(a) - 1):
    if  a[i] != a[i+1]:
        s += 1
print(s)