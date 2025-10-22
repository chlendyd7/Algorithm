def find(x, parent):
    if parent[x] != x:
        parent[x] = find(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    if parent[x] != parent[y]:
        parent[y] = parent[x]
    return parent[x]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    x_location = list(map(int, input().split()))
    y_location = list(map(int, input().split()))
    E = float(input())

    islands = []
    for i in range(N):
        islands.append((x_location[i], y_location[i]))

