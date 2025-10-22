'''
    최대의 갯수만 보면 됩니다.
    기존의 최대의 갯수보다 내가 큰지 확인합니다.
    확인 후 기존의 최대 갯수가 적힌 dy 인덱스에 자신을 넣어줍니다
    그러면서 동시에 가장 큰 최대의 index를 기록 합니다.
'''

n=int(input())
arr=list(map(int,input().split()))
dy=[0]*(n+1)
arr.insert(0,0)
res=0
for i in range(1,n+1):
    cnt=0
    for j in range(i,0,-1):
        if arr[i]>arr[j] and dy[j]>cnt:
            cnt=dy[j]
    dy[i]=cnt+1
    res=max(res,dy[i])
print(res)