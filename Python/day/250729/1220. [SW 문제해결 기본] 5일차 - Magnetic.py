'''
1은 N극 자성체 2는 S극 자성체
윗부분 N극 아래부분 S극
'''
def solution():
    _ = input()
    board = [list(map(int, input().split())) for _ in range(100)]
    cnt = 0
    for col in range(100):
        check = 0
        for row in range(100):
            if board[row][col] == 1:
                check = 1
            elif board[row][col] == 2:
                if check:
                    cnt += 1
                    check = 0

    return cnt

for t in range(1, 11):
    print(f'#{t} {solution()}')