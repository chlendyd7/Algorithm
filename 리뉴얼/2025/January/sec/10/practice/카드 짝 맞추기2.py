from collections import defaultdict, deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
MAX = float('inf')


def ctr_move(board, visited, sx, sy, direct) :
    while True :
        sx, sy = sx + dx[direct], sy + dy[direct]
        if -1 < sx < 4 and -1 < sy < 4 :
            if board[sy][sx] and not visited & 1 << board[sy][sx] - 1 :
                break
            continue
        sx, sy = sx - dx[direct], sy - dy[direct]
        break
    
    return sx, sy

def check_move(board, ax, ay, dist, q, tot_visited, visited, targeted, target_pos, card_dict) :
    next_visited = visited
    next_target_pos = target_pos
    if targeted and board[ay][ax] == targeted and target_pos == (ax, ay):
        next_target = 0
        next_visited = visited | (1 << (targeted - 1))
        next_target_pos = target_pos
    elif targeted :
        next_target = targeted
    elif board[ay][ax] and not visited & 1 << board[ay][ax] - 1 :
        next_target = board[ay][ax]
        next_target_pos = card_dict[(ax, ay)]
    else :
        next_target = 0
    
    if tot_visited[ay][ax][next_target][next_visited] > dist+1 :
        tot_visited[ay][ax][next_target][next_visited] = dist+1
        q.append((ax, ay, next_visited, next_target, next_target_pos, dist+1))    

def find_max_visited(board) :
    result = 0
    for i in range(4) :
        for j in range(4) :
            if board[i][j] :
                result |= 1 << board[i][j] - 1 
    return result

def make_card_dict(board) :
    tmp = defaultdict(list)
    for i in range(4) :
        for j in range(4) :
            if board[i][j] :
                tmp[board[i][j]].append((j,i))
    
    result = dict()
    for val in tmp.values() :
        result[val[0]] = val[1]
        result[val[1]] = val[0]
    
    return result

def solution(board, r, c) :
    tot_visited = [[[[MAX]*(1<<6) for _ in range(7)] for _ in range(4)] for _ in range(4)]
    tot_visited[c][r][0][0] = 0
    result = MAX
    max_visited = find_max_visited(board)
    max_check = bin(max_visited).count('1') * 2
    card_dict = make_card_dict(board)
    
    q = deque([(c, r, 0, 0, (0,0), 0)])
    if board[r][c] :
        tot_visited[r][c][board[r][c]][0] = 0
        q.append((c, r, 0, board[r][c], card_dict[(c,r)], 0))
    
    while q :
        x, y, visited, targeted, target_pos, dist  = q.popleft()
        
        if visited == max_visited:
            result = min(result, dist)
            continue
        
        for k in range(4) :
            ax, ay = x + dx[k], y + dy[k]
            if ax < 0 or ax > 3 or ay < 0 or ay > 3 :
                continue
            check_move(board, ax, ay, dist, q, tot_visited, visited, targeted, target_pos, card_dict)
            ax, ay = ctr_move(board, visited, x, y, k)
            check_move(board, ax, ay, dist, q, tot_visited, visited, targeted, target_pos, card_dict)
    
    return result + max_check
# 출처: https://magentino.tistory.com/78 [마젠티노's:티스토리]
