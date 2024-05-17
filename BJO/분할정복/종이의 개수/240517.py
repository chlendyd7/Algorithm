import sys

def cut(x,y,n):
    global first, second, third
    num = paper[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                cut(x,y,n//3)



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

    first, second, third = 0, 0, 0
    cut(0, 0, n)
    print(white, blue, sep='\n')