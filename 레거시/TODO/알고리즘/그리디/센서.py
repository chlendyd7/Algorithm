N = int(input())
K = int(input())
location = list(map(int, input().split()))
location.sort()

dist = []
for i in range(1, N):
    dist.append(location[i] - location[i-1])

dist.sort(reverse=True)
for _ in range(K-1):
    dist.pop(0)

print(sum(dist))


'''
N = int(input())
K = int(input())
sensor = list(map(int, input().split()))
sensor.sort()

dist = [sensor[i] - sensor[i-1] for i in range(1, N)]
dist.sort(reverse=True)
print(sum(dist[K-1:]))
'''