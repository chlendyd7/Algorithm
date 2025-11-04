'''
    N x N
    지나갈수있는 몇개의 길이 있는지 확인

    지나가려면 길에 속한 모든 칸의 높이가 모두 같아야 함
    놓아서 지나갈 수 있는 길을 만들 수 있음
    경사로는 1 길이는 L
    낮은 칸에 놓음 L개 연속 된 경사로의 바닥이 모두 접해야 함
    높이 차는 1이어야함

    경사로 곂치기 x
    높이차이 1만, L개 연속, 범위 준수
'''
N, L = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check(line):
    visited = [False] * N

    for i in range(N-1):
        diff = line[i+1] - line[i]

        if diff == 0:
            continue

        if abs(diff) > 1:
            return False
        
        if diff == -1:
            for j in range(i+1, i+L+1):
                if j >= N or line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True

        elif diff == 1:
            for j in range(i, i-L, -1):
                if j < 0 or line[i] != line[j] or visited[j]:
                    return False
                visited[j] = True

    return True


cnt = 0
for r in range(N):
    if check(board[r]):
        cnt += 1


for j in range(N):
    col = [board[i][j] for i in range(N)]
    if check(col):
        cnt += 1

print(cnt)
