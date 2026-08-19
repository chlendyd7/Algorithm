# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=5&problemLevel=6&problemLevel=7&problemLevel=8&contestProbId=AV15OZ4qAPICFAYD&categoryId=AV15OZ4qAPICFAYD&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=8&pageSize=30&pageIndex=1
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    parent_x = find(parent, x)
    parent_y = find(parent, y)

    if parent_x > parent_y:
        parent[parent_y] = parent_x
    else:
        parent[parent_x] = parent_y


def solution():
    V, E = map(int, input().split())
    graph = []
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph.append((w, s, e))

    graph.sort()
    parent = [i for i in range(V+1)]
    total_weight = 0


    for w, s, e in graph:
        if parent[s] != parent[e]:
            union(parent, s, e)
            total_weight += w

    return total_weight 


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
