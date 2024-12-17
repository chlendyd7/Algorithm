
def Check(capacity):
    cnt=1
    sum=0
    for x in ls:
        if sum+x>capacity: # 누적된 시간들 이 곡도 저장 할 수 있나 유무 판단
            cnt+=1
            sum=x
        else: # 저장 할 수 있다
            sum+=x
    return cnt




n, m = map(int,input().split())
ls = list(map(int,input().split()))
lt = 1
rt = sum(ls)
while lt<=rt:
    mid=(lt+rt)//2
    if Check(mid)<=m:
        res=mid
        rt=mid-1
    else:
        lt=mid+1
print(res)

##논리에서 오류 dvd 용량은 가장 긴 노래보다 높아야함
# max 함수를 사용해서 노래중에 가장 긴거 보다 높아야함