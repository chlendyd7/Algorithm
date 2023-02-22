n, m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
cnt= 0
for i in ls:
    cnt += 1
    if m==i:
        break

print(cnt)