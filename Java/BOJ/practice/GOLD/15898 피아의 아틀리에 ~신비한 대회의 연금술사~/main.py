N = int(input())
jaelyo = []
for _ in range(N):
    power = []
    for i in range(4):
        power_i = list(map(int, input().split()))
        power.append(power_i)
    color = []
    for i in range(4):
        color_i = list(input().split())
        color.append(color_i)

for i in range(N):
    jaelyo.append((power[i], color[i]))

# 먼저 첫 번째 요소를 넣는거, 회전시키는거 해보자
# n = 넣은 재료 수
# 현재 board
# 회전도 해야하고
def dfs(n):
    pass    


def rotate(board):
    n = len(board)
    m = len(board[0])
    temp_board = [row[:]for row in board]
    
    for i in range(n):
        for j in range(m):
            temp_board[j][n-1-i] = board[i][j]
    return temp_board

lst =  [[0,1,2], [3,4,5], [6,7,8]]
print(rotate(lst))