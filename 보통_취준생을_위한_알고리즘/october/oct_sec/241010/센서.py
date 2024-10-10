import sys


n = int(input())
k = int(input())
location = list(map(int, input().split()))
location.sort()

dist = []
if k >= len(location):
    print(0)
    sys.exit()

for i in range(1, n):
    dist.append(location[i] - location[i-1])
dist.sort(reverse=True)
for _ in range(k-1):
    dist.pop(0)
print(sum(dist))
