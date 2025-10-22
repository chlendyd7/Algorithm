def solution():
    N = int(input())
    board = [list(input()) for _ in range(8)]

    def find_row(row, start_col):
        left = start_col
        right = start_col + N - 1
        while start_col <= right:
            if board[row][left] != board[row][right]:
                return False
            left += 1
            right -= 1
        return True

    def find_col(col, start_row):
        left = start_row
        right = start_row + N - 1
        while start_row <= right:
            if board[left][col] != board[right][col]:
                return False
            left += 1
            right -= 1
        return True

    cnt = 0
    for i in range(8):  # 각 행에 대해
        for j in range(8 - N + 1):  # 가능한 시작 위치
            if find_row(i, j):
                cnt += 1
    
    # 열에서 팰린드롬 찾기
    for j in range(8):  # 각 열에 대해
        for i in range(8 - N + 1):  # 가능한 시작 위치
            if find_col(j, i):
                cnt += 1
        
    return cnt

for t in range(1, 11):
    print(f'#{t} {solution()}')