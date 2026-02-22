n, m = map(int,input().split())
dy=[0]*(m+1)
for i in range(n):
    v, x = map(int,input().split())
    for j in range(v, m+1):
        dy[j] = max(dy[j], dy[j-v]+x)

print(dy[m])