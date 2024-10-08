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
