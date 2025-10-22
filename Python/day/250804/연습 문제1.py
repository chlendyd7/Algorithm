board = [[i + j * 5 for i in range(1, 6)] for j in range(5)]
print(board)

nums = 0
n = len(board)
for i in range(5):
    nums += board[i][i]
    nums += board[i][n-i-1]

print(nums)
