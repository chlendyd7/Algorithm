import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

def cut(x, y, n):
    next = n//2
    color = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != board[i][j]:
                print('(', end='')
                cut(x, y, next)
                cut(x+next, y, next)
                cut(x, y+next, next)
                cut(x+next, y+next, next)
                print(')', end='')
                return
    print(color, end='')

cut(0,0,n)
