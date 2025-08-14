import sys
input = sys.stdin.readline

def dfs(depth, n):
    global ans
    ret = 0
    if depth == M:
        for d in dist:
            for distance, idx in d:
                if visited[idx]:
                    ret += distance
                    break
            if ans <= ret:
                return
        ans = min(ans, ret)
        return

    for i in range(n, len(chicken)):
        if not visited[i]:
            visited[i] = 1
            dfs(depth + 1, i + 1)
            visited[i] = 0


if __name__ == '__main__':
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    house = []
    chicken = []
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                house.append((i, j))
            elif city[i][j] == 2:
                chicken.append((i, j))
    
    dist = []
    for r1, c1 in house:
        dist.append([])
        for idx, c in enumerate(chicken):
            r2, c2 = c
            dist[-1].append((abs(r1-r2) + abs(c1-c2), idx))
        dist[-1].sort()

    visited = [0 for _ in range(len(chicken))]
    ans = 1e9
    dfs(0, 0)