'''
    기준 점 잘 잡기
'''
ways = [0] * 10001
for i in range(10001):
    ways[i] = i

n, d = map(int,input().split())
highway = []
for _ in range(n):
    start, end, dis = map(int,input().split())
    if dis < end - start:
        highway.append((start, end, dis))

now = 0
for i in range(1, d+1):
    for way in highway:
        if start == now:
            ways[i] = min(ways[end], way[2])
        else:
            ways[i] = min(ways[i], ways[i-1] + 1)
print(ways[d])
