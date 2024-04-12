n = int(input())
ls = [list(map(int,input().split())) for _ in range(n)]
m = int(input())
for _ in range(m):
    row, rotate, num = map(int,input().split())
    row -=1
    if rotate == 0:
        for j in range(num):
            ls[row].append(ls[row].pop(0))
    elif rotate == 1:
        for _ in range(num):
            ls[row].insert(0, ls[row].pop())


cnt = 0 
lt = 0
rt = n-1
for i in range(n):
    for j in range(lt, rt+1):
        cnt += ls[i][j]
    if i < n//2:
        lt +=1
        rt -=1
    else:
        lt -=1
        rt +=1
print(cnt)