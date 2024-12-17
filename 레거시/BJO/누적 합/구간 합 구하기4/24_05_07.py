import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ls = list(map(int,input().split()))
prefix_sum = [0]    # init prefix_sum    

temp = 0    
for i in ls:    # accumulate arr section 
    temp += i
    prefix_sum.append(temp)

for _ in range(n):
    i, j = map(int, input().split())
    print(prefix_sum[j] - prefix_sum[i-1])
