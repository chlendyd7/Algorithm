import sys
input = sys.stdin.readline
n=int(input())
board = [list(map(int,input().split())) for _ in range(n)]
result = {
    -1:0,
    0:0,
    1:0
}

def cut(x,y,n):
    color = board[x][y]
    next = n//3
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != board[i][j]:
                cut(x,y,next)
                cut(x,y+next,next)
                cut(x,y+(next)*2,next)
                
                cut(x+next,y,next)
                cut(x+next,y+next,next)
                cut(x+next,y+(next*2),next)
                
                cut(x+(next*2),y,next)
                cut(x+(next*2),y+next,next)
                cut(x+(next*2),y+(next*2),next)
                return
    result[color] += 1

cut(0,0,n)
for key,value in result.items():
    print(value)
