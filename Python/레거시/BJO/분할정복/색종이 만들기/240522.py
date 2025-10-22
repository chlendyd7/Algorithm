import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
white = blue = 0

def cut(x,y,n):
    global white, blue
    color = board[x][y]
    next = n//2

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != board[i][j]:
                cut(x,y,next)
                cut(x,y+next,next)
                cut(x+next,y,next)
                cut(x+next,y+next,next)
                return

    if color == 1:
        blue+=1
    else:
        white+=1

cut(0,0,n)
print(white, blue)
