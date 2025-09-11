def move(i, j, dr):
    back = -1
    for cnt in range(1,10):
        


def dfs(n, ri, rj, bi, bj):
    global ans
    if (n, ri, rj, bi, bj) in v_set:
        return
    v_set.add((n, ri, rj, bi, bj))

    if n > 10:
        return

    for dr in range(4):
        r_cnt = move(ri, rj, dr)

di = [-1, 1, 0, 0]
dj = [ 0, 0,-1, 1]
# 지도입력 및 빨간색(ri,rj), 파란색(bi,bj) 초기좌표
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
for i in range(N) :
    for j in range(M) :
        if arr[i][j] == 'R' :
            ri, rj = i, j
        if arr[i][j] == 'B' :
            bi, bj = i, j

v_set = set()   # 해당 시도회수때 R,B 구슬좌표가 같다면 => 이미해본 경우!
ans = 11
dfs(1,ri,rj,bi,bj)
if ans==11:
    ans=-1
print(ans)
