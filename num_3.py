#n школьников делят k яблок поровну, неделящийся остаток остается в корзинке. Сколько яблок достанется каждому школьнику?
# Сколько яблок останется в корзинке? Программа получает на вход числа n и k и должна вывести искомое количество яблок
# (два числа).
n = int(input("введите число"))
k = int(input("введите число"))
print(k // n)
print(k % n)