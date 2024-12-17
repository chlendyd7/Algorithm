n,m = map(int,input().split())
Line=[]

def Count(len):
    cnt = 1
    endpoint = Line[0]
    for i in range(1, n):
        if Line[i]-endpoint >= len:
            cnt +=1
            endpoint = Line[i]
    return cnt

for _ in range(n):
    tmp=int(input())
    Line.append(tmp)

Line.sort()
rt = Line[n-1]
lt=1

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= m: #배치 할 수 있는 마리 수
        res=mid
        lt=mid+1
    else:
        rt=mid-1

print(res)
