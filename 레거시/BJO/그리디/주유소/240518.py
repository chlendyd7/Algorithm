import sys
input = sys.stdin.readline
n = int(input())
dist = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
maxx = price[0]
for i in range(n-1):
    if price[i] < maxx:
        maxx = price[i]
    result += dist[i]*maxx

print(result)
