n,m = map(int,input().split())
ls = list(map(int,input().split()))
tot = ls[0]
lt = 0
rt = 1
count = 0
while True:
    if tot < m:
        if rt < n:
            tot += ls[rt]
            rt +=1
        else:
            break
    elif tot == m:
        count+=1
        tot -= ls[lt]
        lt +=1
    
    else:
        tot -= ls[lt]
        lt +=1
print(count)
        