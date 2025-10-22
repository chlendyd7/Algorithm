'''
- 메모리 초기화
- 해당 값이 메모리 끝까지 덮어씌어짐
- 원래 상태로 돌아가는데 최소 몇번이나 고쳐야 하는지 계산
- 그리디인가?
- 완탐?

'''

def solution():
    def is_palindrome_line(line, length):
        left, right = 0, length - 1
        while left < right:
            if line[left] != line[right]:
                return False
            left += 1
            left -= 1
        return True

    def find_max_palindrome(board):
        N = 100

        for length in range(N, 1, -1):
            for r in range(N):
                for c in range(N - length + 1):
                    # 가로
                    if is_palindrome_line(board[r][c:c+length], length):
                        return length
                    # 세로
                    col_segment = [board[c+k][r] for k in range(length)]
                    if is_palindrome_line(col_segment, length):
                        return length
        return 1
                    
    
    check = False
    bits = list(map(int, input()))
    cnt = 0
    for b in bits:
        if b != check:
            cnt += 1
            check = not check

    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')