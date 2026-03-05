import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")


'''
    N개의 세로선 M개의 가로선, 세로선과 가로선 놓을 수 있음
    세로선에 가로선을 놓을 수 있는 위치 갯수는 H
    가로선은 세로선 연결 but 가로선 연속하면 안된다
    
    가로선을 추가
    i번 세로선의 결과가 i번이 나와야 한다
    그렇게 하기 위해서 추가해야 하는 가로선의 최솟값을 구하는 프로그램
    
    N, M, H
    가로선 정보 A, B(M개) 가장 위 1, 1 좌표
    정답이 3보다 크면 -1, 불가능한 경우 -1
    
'''
N, M, H = map(int, input().split())
answer = [i for i in range(N)]
print(answer)
board = [[0] * N for _ in range(H)]
for _ in range(M):
    r, c = map(int, input().split())
    board[r-1][c-1] = 1
    board[r-1][c] = 1

print(board)

# 시뮬 완성
def simulation(board):    
    # 일단 스타트하는데 가로 만나면
    result = []
    for start_cal in range(N):
        r = 0
        c = start_cal
        while r < H:
            # 가로선을 만나면
            if board[r][c] == 1:
                if c+1 < N and board[r][c+1] == 1:
                    c = c+1
                elif c-1 >= 0 and board[r][c-1] == 1:
                    c = c-1
                else:
                    print(board)
                    print(r, c, "잘못짬")
            r+=1
        result.append(c)
    print(result)
    return result == answer

mx = 4
def dfs(board, cnt):
    global mx
    if cnt > 3:
        return
    if mx < cnt:
        return

    if simulation(board):
        mx = min(mx, cnt)
        return
    else:
        for r in range(H):
            for c in range(N-1):
                if c == 0:
                    if board[r][c] == 0 and board[r][c+1] == 0:
                        board[r][c] = 1
                        board[r][c+1] = 1
                        dfs(board, cnt+1)
                        board[r][c] = 0
                        board[r][c-1] = 0
                else:
                    if board[r][c] == 0 and board[r][c+1] == 0 and board[r][c-1] == 0:
                        board[r][c] = 1
                        board[r][c+1] = 1
                        dfs(board, cnt+1)
                        board[r][c] = 0
                        board[r][c-1] = 0

dfs(board, 0)
print(mx)
    