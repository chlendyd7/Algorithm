k, n = map(int,input().split())
Line = []
res = 0

def Count(len):
    cnt=0
    for x in Line:
        cnt+=(x//len)
    return cnt

for i in range(k):
    tmp = int(input())
    Line.append(tmp)
    
largest=max(Line)
lt=1
rt=largest
while lt<=rt:
    mid=(lt+rt)//2
    