import sys

input = sys.stdin.readline

a = int(input())

cnt = 0
i = 1

while i*i <= a:
    i+=1
    cnt+=1

print(cnt)