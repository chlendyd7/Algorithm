def rotate_key(key):
    M = len(key)
    return [[key[M-1-j][i] for j in range(M)] for i in range(M)]

def check(expanded_lock, key, start_x, start_y, N, M):
    for i in range(M):
        for j in range(M):
            expanded_lock[start_x + i][start_y + j] += key[i][j]
    
    # 원래 자물쇠 범위 확인
    for i in range(N):
        for j in range(N):
            if expanded_lock[N+i][N+j] != 1:
                return False
    
    return True

def solution(key, lock):
    N = len(lock)
    M = len(key)
    # 자물쇠 확장
    expanded_lock = [[0] * (N + 2*M) for _ in range(N + 2*M)]
    for i in range(N):
        for j in range(N):
            expanded_lock[M+i][M+j] = lock[i][j]
    
    for _ in range(4):  # 열쇠 회전
        key = rotate_key(key)
        for x in range(1, N+M):
            for y in range(1, N+M):
                # 열쇠 대입
                if check(expanded_lock, key, x, y, N, M):
                    return True
                # 열쇠 제거
                for i in range(M):
                    for j in range(M):
                        expanded_lock[x + i][y + j] -= key[i][j]
    
    return False
