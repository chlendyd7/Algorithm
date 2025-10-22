import sys

def cut(x,y,n):
    color = graph[x][y]
    
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != graph[i][j]:
                print('(', end='')
                cut(x, y, n // 2)        # 1사분면
                cut(x, y + n // 2, n // 2)      # 2사분면
                cut(x + n // 2, y, n // 2)      # 3사분면
                cut(x + n // 2, y + n // 2, n // 2)
                print(")", end='')
                return
    print(color, end='')







if __name__ == '__main__':
    n = int(input())
    graph = [list(map(int, input())) for _ in range(n)]

    cut(0, 0, n)