import sys
# sys.stdin = open("input.txt", 'r')
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0) # list가 1번 index에서 시작하게 하기 위해서
dy=[0]*(n+1) # 다이나믹
dy[1]=1 # 직관적으로 처음 값은 1인것을 안다
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if arr[j]<arr[i] and dy[j]>max:
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res: # 최대값 
        res=dy[i]
print(res)a