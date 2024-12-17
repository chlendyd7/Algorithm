import sys
from collections import deque
sys.stdin=open("input.txt", "r")
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]
ch=[[0]*n for _ in range(n)] # 체크 리스트
sum=0
Q=deque()
ch[n//2][n//2]=1 # 중앙 지점을 체크
sum+=a[n//2][n//2] # 중앙 값 누적
Q.append((n//2, n//2)) # Q에 넣어둠
L=0 # 레벨은 0
while True:
    if L==n//2:
        break
    size=len(Q) # 사이즈는 1
    for i in range(size):
        tmp=Q.popleft()
        for j in range(4):
            x=tmp[0]+dx[j]
            y=tmp[1]+dy[j]
            if ch[x][y]==0:
                sum+=a[x][y]
                ch[x][y]=1
                Q.append((x, y)) # 여기서 사이즈 변경
    L+=1
print(sum)
    
