#Дан текст: в первой строке записано число строк, далее идут сами строки. Определите, сколько различных слов содержится в этом тексте.
a = set()
for i in range(int(input())):
    a.update(input().split())
print(len(a))
