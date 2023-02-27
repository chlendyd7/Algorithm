
def Count(mid):
    cnt = 0
    for i in ls:
        cnt+=(i//mid)
    return cnt
        

n,m = map(int,input().split())
ls=[]
largest=0
res=0
for i in range(n):
    tmp = int(input())
    ls.append(tmp)
    largest = max(largest, tmp)
lt =1
rt = largest
while lt <= rt:    
    mid = (lt+rt)//2
    if Count(mid)>=m:
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
