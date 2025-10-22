n = int(input())
dis = list(map(int,input().split()))
avg = int(sum(dis)/n+0.5)
min = float('inf')
for idx, x in enumerate(dis):
    tmp= abs(avg - x)
    if tmp<min:
        min = tmp
        score = x
        num = idx+1
    if tmp==min:
        if score < x:
            score = x
            num = idx+1 

print(avg, num)