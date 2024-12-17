import sys
#sys.stdin = open("input.txt", 'r')
n=int(input())
dy=[0]*(n+1)
dy[1]=1
dy[2]=2 # 직관적으로 알 수 있는건 초기화 길이 2로 자르는 것은 1+1 or 2
for i in range(3, n+1):
    dy[i]=dy[i-1]+dy[i-2]

res=0
for i in range(n+1):
    res=dy[i]
print(res)

    

