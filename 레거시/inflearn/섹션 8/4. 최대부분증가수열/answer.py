import sys
# sys.stdin = open("input.txt", 'r')
n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0) # 5가 list의 1번 index에서 시작하게 하기 위해서
dy=[0]*(n+1) # 다이나믹 1번부터 하려고 n+1
dy[1]=1 # 5만 있기에 직관적으로 처음 값은 5인것을 안다, 3부터 출발
res=0
for i in range(2, n+1):
    max=0 # 최대값 찾기
    for j in range(i-1, 0, -1): # i-1부터 1번까지 돌아야함
        if arr[j]<arr[i] and dy[j]>max: # 만들고자 하는 앞의 항, dy[j]는 arr[j]의 마지막 항의 증가 최대 길이
            max=dy[j] # dy의 최대 길이
    dy[i]=max+1 # 새로운 arr이 더 크니까 +1해줌
    if dy[i]>res: # 최대값 
        res=dy[i]
print(res)