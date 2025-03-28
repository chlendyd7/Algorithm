n = int(input())
dis = [[500]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    dis[i][i]=0

while True:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    dis[a][b]=1
    dis[b][a]=1 # 방향그래프 아님

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            dis[i][j] = min(dis[i][j], dis[i][k]+dis[k][j])

res=[0]*(n+1)
score = 100
for i in range(1, n+1):
    for j in range(1, n+1):
        res[i]=max(res[i], dis[i][j]) #1번 회원의 가장 큰 값이 저장
    score=min(score, res[i])
out =[]
for i in range(1, n+1):
    if res[i]==score:
        out.append(i)
print("%d %d" %(score, len(out)))

for x in out:
    print(x, end=' ')