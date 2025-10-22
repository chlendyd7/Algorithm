import sys
sys.stdin=open("input.txt", "r")
def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

k, n=map(int, input().split())
Line=[]
res=0
largest=0
for i in range(k):
    tmp=int(input())
    Line.append(tmp)
    largest=max(largest, tmp) # 왜 필요? 가장긴 랜선이 오른쪽 끝 값이기 때문
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    if Count(mid)>=n: #최적의 값 찾아 줌
        res=mid
        lt=mid+1
    else:
        rt=mid-1
print(res)








