def Count(len): # 답이 되냐 안되냐 측정
    cnt = 0
    for x in ls:
        cnt+=(x//len)
    return cnt




k, n = map(int,input().split())
ls = []
largest = 0
for _ in range(k):
    tmp = int(input())
    ls.append(tmp)
    largest = max(largest, tmp)
lt = 1
rt = largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)
# lt=0
# rt=n-1
# while lt<=rt