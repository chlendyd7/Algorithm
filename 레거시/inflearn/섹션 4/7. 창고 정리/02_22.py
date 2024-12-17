# 가장 큰값 index 값 -1, 가장 작은 값 index, -1 반복 횟수 m
# sort 계속해주기 !!

l = int(input())
board = list(map(int,input().split()))
m = int(input())

for _ in range(m):
    board.sort()
    board[0] +=1
    board[l-1] -=1

print(max(board) - min(board))
    
