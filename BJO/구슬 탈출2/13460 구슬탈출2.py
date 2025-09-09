'''
    빨간 구슬과 파란 구슬을 넣은 뒤 빨간 구슬을 구멍을 통해 빼냄
    N, M 크기 구멍은 하나만 있음
    파란 구슬이 구멍에 들어가면 안됨
    
    왼쪽 기울이기, 오른쪽 기울이기, 위쪽 기울이기, 아랜쪽 기울이기
    동시에 구멍 x, 같은 칸x, 모두 한 칸을 차지
    기울이기 동작을 그만 하는것은 더 이상 구슬이 움직이지 않을 때
    최소 몇 번 만에 빨간 구슬을 구멍을 통해 빼낼 수 있는지 구하시오

    N, M 크기
    .은 빈칸 #은 장애물 o는 구멍 R은 빨간 구슬 B는 파란 구슬
    크기는 10x10 100
    10번 이하로 움직이기 안되면 -1
'''

N, M = map(int, input().split())
red = blue = hole = (0,0)
board = []
for i in range(N):
    row = list(input())
    for j in range(M):
        if row[j] == 'R':
            red = (i,j)
        if row[j] == 'B':
            blue = (i,j)
        if row[j] == 'O':
            hole = (i,j)
    board.append(row)

def dfs(cnt, board):
    
# def dfs(board):
    

