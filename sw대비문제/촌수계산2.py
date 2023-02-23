node = int(input())
a, b = map(int, input().split())
num = int(input())
graph = [[]*node for _ in range(node+1)]
for _ in range(num):
    n, m = map(int,input().split())
    graph[n].append(m)
    graph[m].append(m)
print(graph) # [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]
BFS = [0] * (node+1)


