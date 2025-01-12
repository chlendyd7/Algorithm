from collections import deque
from itertools import permutations


dx = [-1, 1, 0, 0]
dy = [0,0,-1,0]

def in_range(x, y):
    return 0<= 4 and 0<= y < 4

def bfs(board, start, end):
    q = deque([*start, 0])
    visited = set()
    visited.add(start)

    while q:
        x, y, dist = q.popleft()
        if(x, y) == end:
            return dist

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and (nx, ny) not in visited:
                visited.add((nx,ny))
                q.append((nx,ny, dist + 1))

            cx, cy = x, y
            while in_range(cx + dx[i], cy + dy[i]) and board[cx + dx[i]][cy + dy[i]] == 0:
                cx += dx[i]
                cy += dy[i]
            if (cx, cy) not in visited:
                visited.add((cx, cy))
                q.append((cx, cy, dist + 1))
    return float('inf')
def remove_cards(board, card1, card2):
    board[card1[0]][card1[1]] = 0
    board[card2[0]][card2[1]] = 0

def solution(board, r, c):
    card_positions = {}
    for i in range(4):
        for j in range(4):
            if board[i][j] > 0:
                if board[i][j] not in card_positions:
                    card_positions[board[i][j]] = []
                card_positions[board[i][j]].append((i,j))

    cards = list(card_positions.keys())

    min_moves = float('inf')
    for card_order in permutations(cards):
        total_moves = 0
        curr_pos = (r, c)
        board_copy = [row[:] for row in board]

        for card in card_order:
            card1, card2 = card_positions[card]

            dist1 = bfs(board_copy, curr_pos, card1) + bfs(board_copy, card1, card2) + 2
            dist2 = bfs(board_copy, curr_pos, card2) + bfs(board_copy, card2, card1) + 2

            total_moves += min(dist1, dist2)
            if dist1 <= dist2:
                curr_pos = card2
            else:
                curr_pos = card1
            
            remove_cards(board_copy, card1, card2)
        
        min_moves = min(min_moves, total_moves)
    
    return min_moves