import sys
input = sys.stdin.readline
number = [0]*10001
n=int(input())
for _ in range(n):
    number[int(input().strip())] +=1

for i in range(1, 10001):
    for _ in range(number[i]):
        print(i)
