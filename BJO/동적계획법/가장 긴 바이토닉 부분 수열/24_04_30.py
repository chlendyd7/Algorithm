n=int(input())
ls=list(map(int,input().split()))
plus_dy=[1]*1001
min_dy=[1]*1001
reverse_ls= ls[::-1]
for i in range(n):
    for j in range(i):
        if ls[i]>ls[j]:
            plus_dy[i] = max(plus_dy[i], plus_dy[j]+1)
        if reverse_ls[i]>reverse_ls[j]:
            min_dy[i] = max(min_dy[i], min_dy[j]+1)

result_dy=[0]*1001
for k in range(n):
    result_dy[k] = plus_dy[k] + min_dy[n-k-1]-1

print(max(result_dy))
