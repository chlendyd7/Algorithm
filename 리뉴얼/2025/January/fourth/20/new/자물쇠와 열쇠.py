'''
자물쇠 영역을 벗어난 부분에 있는 열쇠의 홈과 돌기는 자물쇠를 여는 데 영향을 주지 않지만,
자물쇠 영역 내에서는 열쇠의 돌기 부분과 자물쇠의 홈 부분이 정확히 일치해야 하며 열쇠의 돌기와 자물쇠의 돌기가 만나서는 안됩니다. 또한 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있습니다.
홈은 0 돌기는 1
 '''
def rotate(key):
    M = len(key)
    rotated_key = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            rotated_key[j][M - 1 - i] = key[i][j]
    return rotated_key

def check(expanded_lock, key, start_x, start_y, N, M):
    for i in range(M):
        for j in range(M):
            expanded_lock[start_x + i][start_y + j] += key[i][j]
    
    for i in range(N):
        for j in range(N):
            if expanded_lock[N+i][N+j] != 1:
                return False

    return True
def solution(key, lock):
    
    N = len(lock)
    M = len(key)
    expanded_lock = [[0] * (N + 2 * M) for _ in range(N + 2*M)]
    for i in range(N):
        for j in range(N):
            expanded_lock[M+i][M+j] = lock[i][j]
    
    for _ in range(4):
        key = rotate(key)
        for x in range(1, N+M):
            for y in range(1, N+M):
                if check(expanded_lock, key, x, y, N, M):
                    return True
                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] -= key[i][j]
    return False
