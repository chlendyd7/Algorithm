import sys


def cut(x, y, n):
    next =  n//3
    color = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != board[i][j]:
                cut(x,y,next)
                cut(x,y+next,next)
                cut(x,y+(next)*2,next)
                
                cut(x+next, y, next)
                cut(x+next, y+next, next)
                cut(x+next, y+(next)*2, next)
                
                cut(x+(next)*2, y, next)
                cut(x+(next)*2, y+next, next)
                cut(x+(next)*2, y+(next)*2, next)
                return
    result[color] += 1


if __name__=='__main__':
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n)]
    result = {
        -1:0,
        0:0,
        1:0
    }
    cut(0,0,n)
    print(result)


