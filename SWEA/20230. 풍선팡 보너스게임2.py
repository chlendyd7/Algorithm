'''
1. 풍선을 터뜨리면 같은 행과 열의 풍선이 터진다
2. 풍선의 합은 8
3. 최대 점수를 얻을 수 있다
4. 최대 점수를 출력해라
'''
def solution():
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    reversed_board_zip = zip(*board)
    reversed_board = [list(b) for b in reversed_board_zip]

    mx = 0
    for i in range(N):
        for j in range(N):
            mx = max(mx, (sum(board[i]) + sum(reversed_board[j]) - board[i][j]))

    return mx


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
