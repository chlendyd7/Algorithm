n,m = map(int,input().split())
Line=[]
for _ in range(n):
    tmp=int(input())
    Line.append(tmp)

Line.sort()
rt = Line[n-1]
lt=1
mid = (lt+rt)//2
