# https://www.acmicpc.net/problem/2668

n = int(input())
graph = [] * (n+1)
for i in range(1, n+1):
    graph[i].append(int(input()))

print(graph)