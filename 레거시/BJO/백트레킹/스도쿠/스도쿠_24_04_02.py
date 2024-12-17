def row(a, n):
    for i in range(9):
        if n == sudoku[a][i]:
            return False
    return True

def colum(a, n):
    for i in range(9):
        if n == sudoku[i][a]:
            return False
    return True

def square(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == sudoku[x//3*3 +i][y//3*3 +j]:
                return False
    return True


def dfs(n):
    if n==len(blank):
        for i in sudoku:
            print(*i)
        exit()
    for i in range(1,10):
        x=blank[n][1]
        y=blank[n][0]
        if row(x,i) and colum(y,i) and square(x,y,i):
            sudoku[x][y]=i
            dfs(n+1)
            sudoku[x][y]=0


import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            blank.append([i,j])
dfs(0)