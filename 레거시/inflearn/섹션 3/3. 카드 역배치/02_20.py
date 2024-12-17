a= list(range(21))
for i in range(10):
    ai, bi = map(int,input().split())
    for j in range((bi-ai+1)//2):
        a[ai+j], a[bi-j] = a[bi-j], a[ai+j]
a.remove(0)
for x in a:
    print(x, end=' ')