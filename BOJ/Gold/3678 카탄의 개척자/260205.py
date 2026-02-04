dx = [-1, 1, 2, 1, -1, -2]
dy = [2,2,0,-2,-2,0]


def place_title(x, y, idx):
    used_nearby = set()
    for i in range(6):
        nx, ny = x + dx[i], y + dy[i]
        if (nx, ny) in board:
            used_nearby.add(board[(nx, ny)])

    best_res = -1
    min_val = 10001
    for res in range(1, 6):
        if res in used_nearby:
            continue
        if counts[res] < min_val:
            min_val = counts[res]
            best_res = res
    
    ans[idx] = best_res
    board[(x,y)] = best_res
    counts[best_res] += 1

ans = [0] * 10001
board = {}
counts = [0] * 6

cur_x, cur_y = 0, 0
ans[1] = 1
board[(0,0)] = 1
counts[1] = 1
title_idx = 2
for layer in range(1, 70):
    if title_idx > 10000: break
    
    cur_x += dx[0]
    cur_y += dy[0]
    place_title(cur_x, cur_y, title_idx)
    title_idx += 1
    
    for direction in range(6):
        steps = (layer - 1) if direction == 0 else layer
        move_dir = (direction + 1) % 6
        
        for _ in range(steps):
            if title_idx > 10000:
                break
            cur_x += dx[move_dir]
            cur_y += dy[move_dir]
            place_title(cur_x, cur_y, title_idx)
            title_idx += 1
n = int(input())
for i in range(n):
    print(ans[int(input())])
