import sys
n = int(input())
ls = []
for _ in range(n):
    ls.append(int(sys.stdin.readline()))

ls.sort()
for i in ls:
    print(i)