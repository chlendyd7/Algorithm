n = input()
ls = []
for _ in n:
    ls.append(int(_))
ls.sort(reverse=True)
for i in ls:
    print(i, end='')