import sys
input = sys.stdin.readline
n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(list(map(int,input().split())))

m, k =map(int,input().split())
b = []
for _ in range(m):
    b.append(list(map(int,input().split())))

c = [[0 for _ in range(k)] for _ in range(n)]

for n in range(n):
    for k in range(k):
        for m in range(m):
            c[n][k] += a[n][m] * b[m][k]

print(c)
for i in c:
    for j in i:
        print(j, end=' ')
    print()