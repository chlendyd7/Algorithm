import sys
import copy
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_value = 0

def compress(line):
    new_line = [x for x in line if x != 0]
    merged = []
    skip = False
    
    for i in range(len(new_line)):
        if skip:
            skip = False
            continue
        
        if i + 1 < len(new_line) and new_line[i] == new_line[i+1]:
            merged.append(new_line[i] * 2)
            skip = True
        else:
            merged.append(new_line[i])
    
    merged += [0] * (N - len(merged))
    return merged


def rotate(board, times):
    new_board = copy.deepcopy(board)
    for _ in range(times):
        new_board = [list(row) for row in zip(*new_board[::-1])]

    return new_board


def move(board, direction):
    rotated_board = rotate(board, direction)
    new_board = [compress(row) for row in rotated_board]
    
    new_board = rotate(new_board, (4-direction) % 4)
    return new_board


def dfs(board, depth):
    global max_value
    
    if depth == 5:
        max_value = max(max_value, max(map(max, board)))
        return
    
    for d in range(4):
        new_board = move(board,d)
        dfs(new_board, depth + 1)