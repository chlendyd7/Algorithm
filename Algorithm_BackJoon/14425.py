import sys
input = sys.stdin.readline
n, m = map(int,input().split())
nls = []
count = 0
for _ in range(n):
    nls.append(input())

for _ in range(m):
    b = input()
    if b in nls: #b가 nls에 있는지 체크
        count += 1

print(count)
