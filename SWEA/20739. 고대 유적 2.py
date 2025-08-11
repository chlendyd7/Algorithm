'''
1. 구조물이 있는 자리는 1, 빈땅은 0
2. 해상도 N,M 
3. 직선인 구조만 고려하면 됨
'''
def solution():
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    if not board:
        return 0

    reverse_board_zip = zip(*board)
    r_board = [list(b) for b in reverse_board_zip]
    print('r_board:', r_board)

    def find_max_langth(board):
        mx = 0
        for i in range(len(board)):
            cnt = 0
            row = [0] + board[i] + [0]
            for num in row:
                if num:
                    cnt += 1
                else:
                    mx = max(mx, cnt)
                    cnt = 0
        return mx

    return max(find_max_langth(board), find_max_langth(r_board))



T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
