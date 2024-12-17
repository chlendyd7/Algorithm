import sys
input = sys.stdin.readline
n = int(input())
peoples = list(map(int, input().split()))
peoples.sort()
result = 0
now_time = 0
for people in peoples:
    result += people + now_time
    now_time += people
print(result)
