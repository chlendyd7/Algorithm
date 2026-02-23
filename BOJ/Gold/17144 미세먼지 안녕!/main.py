'''
    미세먼지 확산, 인접한 네 방향 공청기 있으면 확산 x Arc/5
    arc - Arc/5 * 확산 방향 갯수
    
    공청기
    윗쪽은 반 시계방향
    아래쪽은 시계방향
    바람이 불면 한칸 이동
    
    공청기 -1
    확산하는 로직 1
    공청기 동작하는 로직 1
    
'''
dr = [-1,1,0,0]
dc = [0,0,1,-1]
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]


def mise(board):
    next_board = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                for
