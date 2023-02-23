# 마구간 좌표 n개
# 말의 숫자 C개
# 최대로?

# 일단 
def Check(len):
    cnt =1
    ep = ls[0]
    for i in range(1, n):
        if ls[i] - ep >= len:
            cnt +=1
            ep = ls[i]
    return cnt    




n, c = map(int,input().split())
ls = []
for i in range(n):
    tmp = int(input())
    ls.append(tmp)
ls.sort()
lt=1
rt=ls[n-1]
while lt<=rt:
    mid=(lt+rt)//2
    if Check(mid)>=c:
        res=mid
        lt = mid +1
    else:
        rt = mid -1

print(res)