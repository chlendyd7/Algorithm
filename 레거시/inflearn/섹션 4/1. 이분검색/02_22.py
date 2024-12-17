n, m = map(int,input().split())
ls = list(map(int,input().split()))
ls.sort()
lt=0
rt=n-1 # index 번호?
while lt <= rt:
    mid=(lt+rt)//2
    if ls[mid]==m:
        print(mid+1)
        break
    elif ls[mid]>m:
        rt=mid-1
    else:
        lt=mid+1