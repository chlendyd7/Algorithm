def has_five_in_a_row(board, N):
    # 4방향: 오른쪽, 아래, 대각선 오른아래, 대각선 오른위
    directions = [(0, 1), (1, 0), (1, 1), (-1, 1)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'o':
                for dx, dy in directions:
                    count = 1
                    x, y = i, j
                    # 현재 방향으로 연속 체크
                    for _ in range(4):  # 이미 1개 포함했으니 4번만 더
                        x += dx
                        y += dy
                        if 0 <= x < N and 0 <= y < N and board[x][y] == 'o':
                            count += 1
                        else:
                            break
                    if count >= 5:
                        return True
    return False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [list(input().strip()) for _ in range(N)]

    if has_five_in_a_row(board, N):
        print(f'#{tc} YES')
    else:
        print(f"#{tc} NO")
