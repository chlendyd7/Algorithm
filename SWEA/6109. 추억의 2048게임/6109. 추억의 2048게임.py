'''
🧩 접근 방법

단일 행/열 이동 로직 구현

0을 제외한 숫자들을 순서대로 모으고

인접한 같은 숫자를 만나면 합쳐주고

다시 0으로 채워서 길이를 맞춤.

방향별 처리 방법

left: 행 단위로 그대로 처리.

right: 행을 뒤집어서 left 로직 적용 후 다시 뒤집기.

up: 열 단위로 추출해서 left 로직 적용.

down: 열을 뒤집어서 left 로직 적용 후 다시 뒤집기.
'''
def solution():
    data = input().split()
    N, cmd = int(data[0]), data[1]
    board = [list(map(int, input().split())) for _ in range(N)]
    tmp_board = [[] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if board[r][c]:
                tmp_board[r].append(board[r][c])

    print(tmp_board)

    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')