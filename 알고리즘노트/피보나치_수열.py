n=int(input())
dynamic_cnt=0
dynamic=[0]*(n+1)
def fibonacci(n):
    global dynamic_cnt
    dynamic[1]=1
    dynamic[2]=2
    for i in range(3,n+1):
        dynamic_cnt+=1
        dynamic[i]=dynamic[i-1]+dynamic[i-2]
    return dynamic[n]
