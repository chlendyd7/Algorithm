board = [list(input()) for _ in range(12)]


def check():
    visited = [[False] * 6 for _ in range(12)]
    pop_list = []

    for r in range(12):
        for c in range(6):
            if board[r][c] != '.':
                temp_list = check_pop(r, c, board[r][c], visited)
                if len(temp_list) > 4:
                    pop_list.extend(temp_list)

    if not pop_list:
        return False
    for x, y in pop_list:
        board[x][y] = '.'
    return True


def gravity():
    for c in range(6):
        stack = []
        for r in range(11, -1, -1):
            if board[r][c] != '.':
                stack.append(board[r][c])
        for r in range(11, -1, -1):
            if stack:
                board[r][c] = stack.pop(0)
            else:
                board[r][c] = '.'


cnt = 0
while True:
    if not check():
        break
    gravity()
    cnt += 1

print(cnt)
