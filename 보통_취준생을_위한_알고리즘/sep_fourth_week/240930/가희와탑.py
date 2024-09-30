n, a, b = map(int,input().split())
top = max(a, b)
answer = []
for i in range(1, top+1):
    answer.append(i)
for j in range(1, top+1):
    if len(answer) < n:
        answer.append(j)
print(*answer)
