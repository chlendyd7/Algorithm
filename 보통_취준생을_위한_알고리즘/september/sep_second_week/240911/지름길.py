n, d = map(int,input().split())
highway = []
for i in range(n):
    start, end, length = map(int,input().split())
    if length < end - start and end <= d:
        highway.append((start, end, length))
visited = [0] * (d + 1)
for j in range(1, d+1):
    visited[j] = j

for start, end, length in highway:
    for i in range(1, d+1):
        if end == i:
            visited[i] = min(visited[i], visited[start] + length)
        else:
            visited[i] = min(visited[i], visited[i-1] + 1)
print(visited[d])
