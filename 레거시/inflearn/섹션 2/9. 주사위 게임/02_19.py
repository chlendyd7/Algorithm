n = int(input())
m=0

for i in range(n):
    a,b,c = map(int,input().split())
    sum=0
    if a==b==c:
        sum = 10000+a*1000
    elif a==b or b==c:
        sum = 1000+b*100
    elif a==c:
        sum = 1000+a*100
    else:
        sum = max(a,b,c)*100
    
    if sum>m:
        m=sum

print(m)

#sort를 사용하기도 하구나