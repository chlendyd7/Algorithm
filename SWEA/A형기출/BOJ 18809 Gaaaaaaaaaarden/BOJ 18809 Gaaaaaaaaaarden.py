# https://www.acmicpc.net/problem/18809
from collections import deque
def bfs(tlst):
    # [0] 큐생성 및 v 등 필요한 변수생성
    # q = []
    q = deque()
    v = [[0]*(M+2) for _ in range(N+2)]
    cnt = 0

    # [1] 큐에 초기데이터들 삽입(v표시)
    for i in range(TC):
        if tlst[i]==0:  continue
        ti,tj = lst[i]
        q.append((ti,tj))
        v[ti][tj]=tlst[i]

    while q:
        # ci,cj = q.pop(0)
        ci,cj = q.popleft()
        if v[ci][cj]==25000:    continue

        # 네방향, 범위내(X), (미방문), 호수(꽃)가 아니면
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if arr[ni][nj]==0 or v[ni][nj]==25000:
                continue

            if v[ni][nj]==0:  # 처음 방문
                if v[ci][cj]<0: # R: 1 감소
                    v[ni][nj]=v[ci][cj]-1
                    q.append((ni,nj))
                else:           # G: 1 증가
                    v[ni][nj]=v[ci][cj]+1
                    q.append((ni,nj))
            else:               # 이미 기록 => 꽃 체크
                if v[ci][cj]<0: # R
                    if v[ni][nj]+v[ci][cj]-1==0:
                        cnt+=1
                        v[ni][nj]=25000
                else:
                    if v[ni][nj]+v[ci][cj]+1==0:
                        cnt+=1
                        v[ni][nj]=25000
    return cnt

def dfs(n, rcnt, gcnt, tlst):
    global ans
    if n == TC:     # 모든 땅을 결정했으면 종료
        if rcnt==RC and gcnt==GC:
            ans = max(ans, bfs(tlst))
        return

    dfs(n+1, rcnt+1, gcnt, tlst+[-1])   # 빨간씨앗
    dfs(n+1, rcnt, gcnt+1, tlst+[1])    # 초록씨앗
    dfs(n+1, rcnt, gcnt, tlst+[0])      # 안 뿌리는 경우


N, M, RC, GC = map(int, input().split())
arr = [[0]*(M+2)]+[[0]+list(map(int, input().split()))+[0] for _ in range(N)]+[[0]*(M+2)]

lst = []
for i in range(1, N+1):
    for j in range(1, M+1):
        if arr[i][j]==2:    # 배양액 가능한 땅이면(좌표저장)
            lst.append((i,j))
TC = len(lst)

# [1] 가능한 모든 장소에 배양액 뿌리는 방법 순회
ans = 0
dfs(0, 0, 0, [])
print(ans)