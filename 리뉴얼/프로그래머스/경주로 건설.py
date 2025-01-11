from collections import deque
from heapq import heappop, heappush
from sys import maxsize

def solution(board):
    N = len(board)
    q = deque()
    cost_board = [[[maxsize] * N for _ in range(N)] for _ in range(4)]
    for i in range(4):
        cost_board[i][0][0] = 0

    heap = [(0, 0, 0, 0), (0, 0, 0, 2)]
    while heap:
        cost, x, y, d = heappop(heap)

        for dx, dy, dd in ((1,0,0), (-1,0,1), (0,1,2), (0,-1,3)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
                new_cost = cost + (100 if d == dd else 600)
                
                if cost_board[dd][ny][nx] > new_cost:
                    cost_board[dd][ny][nx] = new_cost
                    heappush(heap, (new_cost, nx, ny, dd))
    
    return min([cost_board[i][N-1][N-1] for i in range(4)])
