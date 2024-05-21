import sys
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def cut(a, b, n):
    global white, blue
    next = n//2
    paper = board[a][b]

    for i in range(a, a+n):
        for j in range(b, b+n):
            if board[i][j] != paper:
                cut(a, b, next),
                cut(a, b+next, next)
                cut(a+next , b, next)
                cut(a+next, b+next, next)
                return

    if paper == 0:
        white +=1
    else:
        blue +=1

white = 0
blue = 0
cut(0,0, n)
print(white)
print(blue)