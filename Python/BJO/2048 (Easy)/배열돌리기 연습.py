# 3 3
# 1 2 3
# 4 5 6
# 7 8 9

N,M = 3, 3
lst = [[1,2,3], [4,5,6], [7,8,9]]
tmp_lst = [[0] * N for _ in range(M)]

# 시계방향 회전
for i in range(N):
    for j in range(M):
        tmp_lst[j][N-1-i] = lst[i][j]

print(tmp_lst)

for i in range(N):
    for j in range(M):
        tmp_lst[M-1-j][i] = lst[i][j]

print(tmp_lst)