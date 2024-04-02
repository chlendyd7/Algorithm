def row(a, n):
    for i in range(9):
        if a == sudoku[n][i]:
            return False
    return True

def colum(a, n):
    for i in range(9):
        if a == sudoku[i][n]:
            return False
    return True

def square(x,y,a):
    for i in range(3):
        for j in range(3):
            if a == sudoku[y//3*3+i][x//3*3+j]:
                return False
    return True

def dfs(n):
    if n==len(blank):
        for i in sudoku:
            print(*i)
        exit()
    for i in range(1,10):
        y = blank[n][0]
        x = blank[n][1]
        if row(i, y) and colum(i, x) and square(x,y,i):
            sudoku[y][x]=i
            dfs(n+1)
            sudoku[y][x]=0


import sys
sudoku = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            blank.append([i,j])
dfs(0)