n, m = map(int,input().split())
dy = [0]*(n+m+1) # list index 오류 매번 초기화 해줄 것
max = 0
for i in range(1, n):
    for j in range(1, m):
        dy[i+j] +=1

for i in range(len(dy)):
    if max<dy[i]:
        max = dy[i]

for i in range(len[dy]): #함수 사용 조심
    if dy[i] == max:
        print(dy[i], end='')
