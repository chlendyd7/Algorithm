import sys
sys.stdin = open("input.txt", "rt")

# nxn 벌통. 각 칸은 꿀의 양
# 최대한 많은 수익 얻기
# 두명의 일꿀 존재. 꿀을 채취할 수 있는 벌통 수 m
# 선택한 벌통에서 꿀 채취 가능. 둘 다 가로로 연속해서 m개의 벌통 선택.
# 각 일꿀은 채취할 수 있는 최대 양은 C
# 채취한 꿀의 제곱만큼의 수익.

def DFS(L,x,y,now,val):
    global res
    if now > c:
        return # 가지치기
    if L == m: # m개의 벌통 모두 확인 완료
        res = max(res, val)
    else:
        DFS(L+1, x,y+1,now + g[x][y], val + g[x][y] ** 2)
        DFS(L+1, x,y+1, now, val)


T = int(input())
for t in range(1,T+1):
    n,m,c = map(int, input().split()) # n,m,c
    g = [list(map(int, input().split())) for _ in range(n)]

    # 먼저 일꾼 A를 확정짓고 시작.
    res = 0
    resA = 0
    resB = 0
    최종수익 = 0
    for x1 in range(n):
        for y1 in range(n-m+1):
            res = 0
            DFS(0,x1,y1,0,0)
            resA = res
            for x2 in range(x1,n):
                start = 0
                if x1 == x2: # 같은 행인 경우 따져야함
                    start = y1 + m # 시작위치 조정
                for y2 in range(start,n-m+1):
                    res = 0
                    DFS(0,x2,y2,0,0)
                    resB = res
                    최종수익 = max(최종수익, resA + resB)
    print(f"#{t} {최종수익}")
