import sys
'''
5 5 6
1 1
3 2
2 3
5 1
5 4
'''

sys.stdin = open('input.txt', 'r')
N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

def check():
    for curr in range(1, N+1):
        col = curr
        for r in range(1, H+1):
            if board[r][col] == 1:
                col = col+1
            elif board[r][col-1] == 1:
                col = col-1
        if col != curr:
            return False
    return True

mx = 4
def dfs(cnt, r, c):
    global mx
    if mx <= cnt:
        return
    if check():
        mx = cnt
        return
    if cnt == 3:
        return

    for rr in range(r, H+1):
        if rr == r:
            col = c
        else:
            col = 1
        for cc in range(col, N):
            if board[rr][cc] == 0 and board[rr][cc+1] == 0 and board[rr][cc-1] == 0:
                board[rr][cc] = 1
                dfs(cnt+1, rr, cc+2)
                board[rr][cc] = 0
dfs(0,1,1)
print(mx if mx != 4 else -1)
