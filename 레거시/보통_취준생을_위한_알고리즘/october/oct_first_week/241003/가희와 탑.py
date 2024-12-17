import sys


n,a,b = map(int,input().split())
answer = []
for i in range(1, a):
    answer.append(i)
answer.append(max(a,b))
for i in range(b-1, 0, -1):
    answer.append(i)

if n < len(answer):
    print(-1)
    sys.exit()

print(answer[0], end=' ')
for j in range(n - len(answer)):
    print(1, end=' ')
for k in range(1, len(answer)):
    print(answer[k], end=' ')
