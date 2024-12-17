# https://www.acmicpc.net/problem/1931

n = int(input())
answer = 0
endtime = 0
ls = []
for _ in range(n):
    start, end = map(int,input().split())
    ls.append((start, end))


ls.sort(key=lambda x: (x[1], x[0]))
for i in range(len(ls)):
    if endtime <= ls[i][0]:
        endtime = ls[i][1]
        answer += 1
print(answer)