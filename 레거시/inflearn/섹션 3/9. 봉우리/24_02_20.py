n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,0,1,0]
dy = [0,1,0,-1]


ls.append([0]*n)
ls.insert(0, [0]*n)
cnt = 0 
for x in ls:
    x.insert(0,0)
    x.append(0)


for i in range(1, n+1):
    for j in range(1, n+1):
        if all(ls[i][j]>ls[i+dx[k]][j+dy[k]]for k in range(4)):
            cnt+=1

print(cnt)