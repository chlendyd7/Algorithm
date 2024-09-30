T = int(input())
dy = [1] * 10001
for i in range(2, 10001):
    dy[i] += dy[i-2]
for i in range(3, 10001):
    dy[i] += dy[i-3]

for _ in range(T):
    print(dy[int(input())])