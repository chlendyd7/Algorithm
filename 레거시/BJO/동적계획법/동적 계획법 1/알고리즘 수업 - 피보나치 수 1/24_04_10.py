def fin(n):
    global recursion_cnt
    if n==1 or n==2:
        recursion_cnt+=1
        return 1
    else:
        return fin(n-1) + fin(n-2)

def fibonacci(n):
    global dynamic_cnt
    dynamic[1]=1
    dynamic[2]=2
    for i in range(3,n+1):
        dynamic_cnt+=1
        dynamic[i]=dynamic[i-1]+dynamic[i-2]
    return dynamic[n]



recursion_cnt=0
dynamic_cnt=0

n=int(input())
dynamic=[0]*(n+1)

fin(n)
fibonacci(n)
print(recursion_cnt, dynamic_cnt)



