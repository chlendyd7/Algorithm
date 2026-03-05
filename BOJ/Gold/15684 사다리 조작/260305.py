import os
import sys

# sys.stdin = open('D:\Coding\Algorithm\BOJ\Gold\15684 사다리 조작\input.txt', 'r')
sys.stdin = open('input.txt', 'r')

N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a][b] = 1

def check():
    for c in range(1, N+1):
        idx = c
        for r in range(1, H+1):
            if board[r][idx] == 1:
                idx += 1
            elif board[r][idx-1] == 1:
                idx -= 1
        if idx != c:
            return False
    return True

mx = 4
def dfs(cnt, r, c):
    global mx
    if cnt >= mx:
        return
    if check():
        mx = cnt
        return
    if cnt == 3:
        return

    for i in range(r, H+1):
        if i==r:
            k = c
        else:
            k = 1
        for j in range(k, N):
            if board[i][j] == 0 and board[i][j-1] == 0 and board[i][j+1] == 0:
                board[i][j] = 1
                dfs(cnt+1, i, j+2)
                board[i][j] = 0

dfs(0,1,1)
print(mx)
