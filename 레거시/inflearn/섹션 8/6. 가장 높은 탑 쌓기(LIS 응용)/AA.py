# 파이팅
n = int(input())
bricks=[]
for i in range(n):
    a, b, c = map(int,input().split())
    bricks.append((a,b,c))
bricks.sort(reverse=True)
print(bricks)
dy= [0]*n
dy[0]= bricks[0][1]
res = bricks[0][1]
for i in range(n):
    max_h=0
    for j in range(i-1,-1,-1): #0번까지 돌게 하기 위해서
        if bricks[j][2]>bricks[i][2] and dy[j]>max_h:
            max_h=dy[j]
        dy[i]=max_h+bricks[i][1]
    res=max(res, dy[i])
print(res)
# dy의 2차원 함수로 받는 방법 비교 값이 두개 이상일 시 코드 짜는 방법.