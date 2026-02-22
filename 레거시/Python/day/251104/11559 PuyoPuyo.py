from collections import deque

direction = [(1,0), (0,1), (-1,0), (0, -1)]
board = [list(input()) for _ in range(12)]
def dfs(r, c, color, visited):
    q = deque([(r,c)])
    pop_list = []
    visited[r][c] = True
    while q:
        r, c = q.popleft()
        pop_list.append((r,c))

        for dx, dy in direction:
            nx, ny = r + dx, c + dy
            if 0 <= nx < 12 and 0 <= ny < 6 \
                and not visited[nx][ny] and board[nx][ny] == color:
                q.append((nx, ny))
                visited[nx][ny] = True

    return pop_list


def explode():
    visited = [[False] * 6 for _ in range(12)]
    pop_list = []
    for r in range(12):
        for c in range(6):
            if board[r][c] != '.' and not visited[r][c]:
                color = board[r][c]
                tmp_list = dfs(r, c, color, visited)
                if len(tmp_list) >= 4:
                    pop_list.extend(tmp_list)
    if not pop_list:
        return False
    
    for x, y in pop_list:
        board[x][y] = '.'
    return True


def apply_gravity():
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
           

chain = 0
while True:
    if not explode():
        break
    apply_gravity()
    chain += 1

print(chain)