n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
prefix1 = [[0] * (n+2) for _ in range(n+2)]
prefix2 = [[0] * (n+2) for _ in range(n+2)]

for i in range(1, n):
    for j in range(1, n):
        val = matrix[i][j]
        prefix1[i][j] = prefix1[i-1][j-1] + val
        prefix2[i][j] = prefix2[i-1][j+1] + val

beauti = -1
for k in range(2, n+1):
    for i in range(1, n-k+2):
        for j in range(k, n-k+2):
            r1, c1 = i, j
            r2, c2 = i + k-1, j + k-1
            first = prefix1[r2][c2] - prefix1[r1-1][c1-1]
            second = prefix2[r2][c1] - prefix2[r1-1][c2+1]
            beauti = max(beauti, first - second)
print(beauti)
