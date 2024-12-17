import heapq as hq

a=[]
n = int(input())
for _ in range(n):
    n=int(input())
    
    if n==0:
        if len(a) == 0:
            print(0)
        else:
            print(-hq.heappop(a))
            
    else:
        hq.heappush(a, -n)
