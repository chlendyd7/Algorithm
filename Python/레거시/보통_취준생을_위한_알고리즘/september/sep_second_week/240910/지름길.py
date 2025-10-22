n, d = map(int,input().split())
high_way = []
for i in range(n):
    start, end, length = map(int,input().split())
    high_way.append([start, end, length])
high_way.sort()
dy = [0] * (d + 1)

for j in range(1, d+1):
    dy[j] = j

for start, end, length in high_way:
    for i in range(1, d+1):
        if end == i:
            dy[i] = min(dy[i], dy[start] + length)
        else:
            dy[i] = min(dy[i], dy[i-1] + 1)
print(dy[d])