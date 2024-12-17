N, M = map(int, input().split())
a = [0]*(N+M+3)
max = 0
for i in range(1,N+1):
    for j in range(1,M+1):
        a[i+j] += 1

for i in range(N+M+1):
    if max<a[i]:
        max = a[i]

for i in range(N+M+1):
    if max == a[i]:
        print(i, end=' ')