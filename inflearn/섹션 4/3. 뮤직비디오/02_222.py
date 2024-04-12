def check(len):
    cnt = 1
    sum = 0
    for x in ls:
        if sum+x>len:
            cnt+=1
            sum=x
        else:
            sum+=x
    return cnt




n, m = map(int,input().split())
ls = list(map(int,input().split()))
largest = max(ls)
lt=1
rt = sum(ls)
cnt = 0
while lt<=rt:
    mid = (lt+rt)//2
    if check(mid)<=m:
        res=mid
        rt = mid-1
    else:
        lt=mid+1
print(res)