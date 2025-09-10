'''
    bar은 가로 방향으로 W개 붙여서 만들어짐
    두께 D(세로), 가로 크기 W

    세로 방향 셀들의 특성을 중요하다
    동일한 특성의 셀 K개 이상 연속적으로 있음

    막 내 모든 셀의 특성이 넣는 약품으로 변경

    => 회원가입

    메모리 걱정이 필요함
    
'''
# import os
# import sys


# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
# sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

def calculate(board):
    cnt = 0
    W = len(board[0])
    for w in range(W):
        yunsok = 0
        film = None
        for i in range(len(board)):
            if board[i][w] == film:
                yunsok += 1
                if yunsok == K:
                    cnt += 1
                    break
            else:
                yunsok = 1
                film = board[i][w]

    if cnt == W:
        return True

    return False

A = (0,)*20
B = (1,)*20

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    visited = [0] * D
    result = K

    def dfs(cnt, board):
        global result

        if cnt >= result:
            return

        if calculate(board):
            result = min(result, cnt)
            return

        next_board = board[:]
        for d in range(1, D):
            next_board[d] =

            visited[d] = 1
            board[d] = [0] * W
            dfs(cnt + 1, board)
            board[d] = [1] * W
            dfs(cnt + 1, board)
            visited[d] = 0
            board[d] = tmp

    dfs(0, board)
    print(f'#{tc} {result}')
