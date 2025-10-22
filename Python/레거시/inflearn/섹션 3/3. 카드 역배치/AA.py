ls = list(range(21))
for i in range(10):
    ai, bi = map(int, input().split())
    for j in range((bi- ai +1)//2):
        ls[ai+j], ls[bi-j] = ls[bi-j], ls[ai+j]
ls.remove(0)
for x in ls:
    print(x, end=' ')