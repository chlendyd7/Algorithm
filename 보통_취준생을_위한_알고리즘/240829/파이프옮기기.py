# https://www.acmicpc.net/problem/17070
# 추후 db로 시간 초과 잡기

n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int,input().split())))
count = 0

def dfs(y, x, state):
    global count
    if x == n -1 and y == n -1:
        count += 1
        return
    
    if state == 0:
        if x == n-1:
            return

        if 0<= y < n and 0<= x+1 < n and house[y][x+1] == 0:
            dfs(y, x+1, 0)
        if 0<= y+1 < n and 0<= x+1 < n and house[y][x+1] == 0 and \
            house[y+1][x] == 0 and house[y+1][x+1] == 0:
            dfs(y+1, x+1, 2)
    
    elif state == 1:
        if y == n-1:
            return
        if 0<= y+1 < n and 0<= x < n and house[y+1][x] == 0:
            dfs(y+1, x, 1)
        
        if 0<=y+1<n and 0<=x+1<n and house[y][x+1] == 0 and house[y+1][x+1] == 0 and house[y][x+1] == 0:
            dfs(y+1, x+1, 2)
    
    elif state == 2:
        if 0<=y<n and 0<=x+1<n and house[y][x+1] == 0:
            dfs(y, x+1, 0)
        if 0<=y+1<n and 0<=x<n and house[y+1][x] == 0:
            dfs(y+1, x, 1)
        if 0<=y+1<n and 0<=x+1<n and house[y+1][x] == 0 and house[y][x+1] == 0 and house[y+1][x+1] == 0:
            dfs(y+1, x+1, 2)

dfs(0,1,0)
print(count)

'''
import sys
count = 0
N = int(input())
home = []

for _ in range(N):
    home.append([int(x) for x in sys.stdin.readline().rstrip().split()])

def dfs(x,y,state): # state 0: 가로, 1: 세로 , 2: 대각선
    global count
    if x == N - 1 and y == N - 1:
        count += 1
        return

    if state == 0:
        if y == N - 1: # 이동불가
            return

        if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
            dfs(x, y + 1, 0)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 2)

    elif state == 1:
        if x == N - 1: # 이동불가
            return

        if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
            dfs(x + 1, y, 1)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 2)

    elif state == 2:
        if 0 <= x < N and 0 <= y + 1 < N and home[x][y + 1] == 0:
            dfs(x, y + 1, 0)

        if 0 <= x + 1 < N and 0 <= y < N and home[x + 1][y] == 0:
            dfs(x + 1, y, 1)

        if 0 <= x + 1 < N and 0 <= y + 1 < N and home[x][y + 1] == 0 and home[x + 1][y] == 0 and home[x + 1][
            y + 1] == 0:
            dfs(x + 1, y + 1, 2)

dfs(0,1,0)
print(count)
'''