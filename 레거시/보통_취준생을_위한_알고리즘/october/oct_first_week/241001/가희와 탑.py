n, a, b = map(int,input().split())

answer = []
max_building = max(a,b)

for i in range(1, a):
    answer.append(i)
answer. append(max_building)

for i in range(b-1, 0, -1):
    answer.append(i)

if len(answer) > n:
    print(-1)
else:
    print(answer,[0], end=' ')
    x = n - len(answer)
    
    for i in range(x):
        print(1, end =' ')
    
    for i in range(1, len(answer)):
        print(answer[i], end=' ')
