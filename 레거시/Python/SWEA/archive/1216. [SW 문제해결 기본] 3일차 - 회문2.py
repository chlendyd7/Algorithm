'''
1. 거꾸로 읽어도 똑같은거
2. 'A', 'B', 'C', 중 하나
3. 가로 세로에 대해서만 체크

회문은 투 포인터를 이용해 문자열 좌우를 비교하는게 가장 최적

'''
def solution():
    def is_palindrome_row(baord, r, c, length):
        left, right = 0, length -1
        while left < right:
            if board[r][c + left] != board[r][c + right]:
                return False
            left += 1
            right -= 1
        return True

    def is_palindrome_col(line, length):
        left, right = 0, length - 1
        while left < right:
            if line[left] != line[right]:
                return False
            left += 1
            right -= 1
        return True

    def find_max_palindrome(board):
        N = 100

        for length in range(N, 1, -1):
            for r in range(N):
                for c in range(N - length + 1):
                    # 가로
                    if is_palindrome_row(board, r, c, length):
                        return length
                    if is_palindrome_col(board, c, r, length):  # 세로 방향
                        return length
    board = [list(input()) for _ in range(100)]
    return find_max_palindrome(board)


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')