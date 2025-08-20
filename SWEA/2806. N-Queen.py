def solution():
    N = int(input())
    col = [0] * N
    diag1 = [0] * (2*N - 1) # 0,0에서 N-1, N-1까지의 범위 (2N-2)
    diag2 = [0] * (2*N - 1)
    cnt = 0
    
    def backtrack(row):
        nonlocal cnt
        if row == N:
            cnt += 1
            return

        for c in range(N):
            if not col[c] and not diag1[row + c] and not diag2[row - c + (N - 1)]:
                col[c] = diag1[row + c] = diag2[row - c + (N - 1)] = 1
                backtrack(row + 1)
                col[c] = diag1[row + c] = diag2[row - c + (N - 1)] = 0

    backtrack(0)

    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
