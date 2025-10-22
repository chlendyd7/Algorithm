from pprint import pprint


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pprint(arr)

arr_t = list(map(list, zip(*arr)))
pprint(arr_t)


new = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        new[i][j] = arr[N-1-i][j]

pprint(new)