    # https://www.acmicpc.net/problem/2630

import sys
n = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

white = 0
blue = 0

def divide_conquer(x, y, n):
    global blue, white
    same_color = board[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if board[i][j] != same_color:
                divide_conquer(x, y, n//2)
                divide_conquer(x+n//2, y, n//2)
                divide_conquer(x, y+n//2, n//2)
                divide_conquer(x+n//2, y+n//2, n//2)
                return
    
    if same_color == 0:
        white +=1
        return
    else:
        blue +=1
        return

divide_conquer(0,0,n)
print(white)
print(blue)