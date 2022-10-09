N,M = map(int, input().split())
a = list(map(int, input().split()))
cnt = 0
tot = a[0]
lt =0
rt = 1

while True:
    if tot < M:
        if rt <N:
            tot +=a[rt]
            rt+=1
        else:
            break
    elif tot==M:
        cnt +=1
        tot -=a[lt]
        lt +=1
    else:
        tot -=a[lt]
        lt +=1
print(cnt)