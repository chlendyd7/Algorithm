# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7GKs06AU0DFAXB

def solution():
    n = int(input())
    col = [0] * n
    diag1 = [0] * (2 * n -1)
    diag2 = [0] * (2 * n -1)

    count = 0

    def dfs(r):
        nonlocal count
        if r == n:
            count += 1
            return
        
        for c in range(n):
            if col[c] or diag1[r-c+n-1] or diag2[r+c]:
                continue

            col[c] = 1
            diag1[r-c+n-1] = 1
            diag2[r+c] = 1
            dfs(r+1)
            col[c] = 0
            diag1[r-c+n-1] = 0
            diag2[r+c] = 0

    dfs(0)
    return count

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
