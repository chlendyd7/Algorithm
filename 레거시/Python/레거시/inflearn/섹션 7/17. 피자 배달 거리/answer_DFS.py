import sys
sys.stdin=open("input.txt", "r")
def DFS(L, s):
    global res
    if L==m:
        sum=0
        for j in range(len(hs)):
            x1=hs[j][0] # 집 하나 결정
            y1=hs[j][1]
            dis=2147000000
            for x in cb: # m개 for문
                x2=pz[x][0] 
                y2=pz[x][1]
                dis=min(dis, abs(x1-x2)+abs(y1-y2)) #거리
            sum+=dis
        if sum<res:
            res=sum    
    else:
        for i in range(s, len(pz)): # 조합 구하는 방법 복습 필요
            cb[L]=i # 0~5까지 돔
            DFS(L+1, i+1)


if __name__=="__main__":
    n, m=map(int, input().split())
    board=[list(map(int, input().split())) for _ in range(n)]
    hs=[]
    pz=[]
    cb=[0]*m # 살아남는 갯수, 조합의 경우를 나타냄
    res=2147000000
    for i in range(n): # board 순회 새로운 좌표 hs, pz에 넣어줌
        for j in range(n):
            if board[i][j]==1:
                hs.append((i, j))
            elif board[i][j]==2:
                pz.append((i, j))
    DFS(0, 0)
    print(res)

