'''
동일한 크기를 가진 bar
두께 D 가로크기 W

A, B가 나옴
합격 기준 K

충격은 보호 필름 단면의 세로 방향으로 가해짐
동일한 특성의 셀들이 K개 이상 연속적으로 있는 경우에만 성능검사 통과

약품을 사용해야한다
막 별로 투입 시 하나의 특성으로 변경

약품 투입 횟수를 최소로 하여 성능검사를 통과할 수 있는 방법을 찾아라

문제점
1. 몇번이나 바꿔야하는가?, 횟수를 체크하면서 바꾸고 안바꾸고 전부다 체크? 수열의 length처럼

아이디어
A.
    일단 완전탐색해보기

A.
    1. 문제가 되는 단면의 index를 찾기
    2. 그리고 해당 index에 값을 바꿔주기 그리고 체크?

'''

from copy import deepcopy


def solution():
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    visited = [0] * D


    def check_board(local_board):
        cnt = 0
        for d in range(D):
            flag = 0
            w_cnt = 0
            for w in range(W):
                if flag == local_board[d][w]: # 현재 체크하는 것과 같다면
                    w_cnt += 1
                    if w_cnt == K:
                        cnt += 1
                        break
                else:
                    flag = local_board[d][w]
                    w_cnt = 1
        if cnt == W:
            return True
        else:
            return False


    def dfs(length, count, start, temp_board):
        if count < length:
            for d in range(start, D):
                if not visited[d]:
                    visited[d] = 1
                    origin_board = temp_board[d]
                    temp_board[d] = [0] * W
                    if dfs(length, count + 1, d, temp_board):
                        return True

                    visited[d] = 0
                    temp_board[d] = origin_board

        elif count == length:
            if check_board(temp_board):
                return True
        return False


    for length in range(D):
        tmp_board = deepcopy(board)
        if dfs(length, 0, 0, tmp_board):
            return length

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')