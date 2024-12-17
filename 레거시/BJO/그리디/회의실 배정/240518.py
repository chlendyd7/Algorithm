import sys
input = sys.stdin.readline
n = int(input())
meeting = []
for i in range(n):
    start, end = map(int, input().split())
    meeting.append((start, end))

meeting.sort(key=lambda x: (x[1], x[0]))
time = 0
cnt = 0
for start, end in meeting:
    if start >= time:
        cnt += 1
        time = end
print(cnt)
