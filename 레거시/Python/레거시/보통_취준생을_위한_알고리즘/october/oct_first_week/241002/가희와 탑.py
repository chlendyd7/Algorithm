n,a,b = map(int,input().split())
answer = []

for i in range(1, a):
    answer.append(i)
answer.append(max(a,b))
for j in range(b-1, 0, -1):
    answer.append(j)

if len(answer) > n:
    print(-1)
else:
    print(answer[0], end=' ')
    for k in range(n - len(answer)):
        print(1, end=' ')
    for l in range(1, len(answer)):
        print(answer[l], end=' ')
