import sys

def cut(x,y,n):
    current = paper[x][y]
    next = n//3
    double = (n//3)*2
    for i in range(x, x+n):
        for j in range(y, y+n):
            if current != paper[i][j]:
                cut(x, y, next)
                cut(x, y+next, next)
                cut(x, y+(next*2), next)
                cut(x+next, y, next)
                cut(x+next, y+next, next)
                cut(x+next, y+double, next)
                cut(x+double, y, next)
                cut(x+double, y+next, next)
                cut(x+double, y+double, next)
                return
    result[current] +=1
    return



if __name__ == '__main__':
    n = int(sys.stdin.readline())
    paper = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    result = {
        -1:0,
        0:0,
        1:0
    }

    cut(0, 0, n)
    for key, value in result.items():
        print(value)
