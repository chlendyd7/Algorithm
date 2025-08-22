'''
N x N 행렬
빈 용기는 0
물질에 따라 1~9

물질 용기는 사각형을 이루고 있음(내부 0 없음)
용기들 사이에는 0이 있음
대각선은 고려x

행과 열을 곱한 값, 크기가 작은 순서대로 출력
3x4 행렬은 12
크기가 같으면 행이 작은 순서대로

헤메다 놓침
'''
DIRECTION = [
    (0, 1),
    (1, 0)
]
def solution():
    N = int(input())
    container = [list(map(int, input().split())) for _ in range(N)]
    danger = []
    
    def check_size(r, c):
        r_size, c_size = 0, 0
        nr, nc = r, c
        for dr, dc in DIRECTION:
            while True:
                nr += dr
                nc += dc
                if nr == N:
                    r_size = N-1
                    break
                if nc == N:
                    c_size = N-1
                    break
                if nr < N and nc < N:
                    if not container[nr][nc]:
                        r_size = max(r_size, nr - dr)
                        c_size = max(c_size, nc - dc)
                        break
        return r_size, c_size

    for i in range(N):
        for j in range(N):
            if container[i][j] != 0:
                r_size, c_size = check_size(i,j,container)
                danger.append((r_size - i + 1, c_size - j + 1))
                i, j = r_size
    
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')