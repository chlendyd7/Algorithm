'''
입력 파일의 첫째 줄에는 입력될 벽돌의 수가 주어진다. 입력으로 주어지는 벽돌의 수는 최대
100개이다. 둘째 줄부터는 각 줄에 한 개의 벽돌에 관한 정보인 벽돌 밑면의 넓이, 벽돌의 높
이 그리고 무게가 차례대로 양의 정수로 주어진다. 각 벽돌은 입력되는 순서대로 1부터연속적
인 번호를 가진다.
    5
    25 3 4
    4 4 6
    9 2 3
    16 2 5
    1 5 2
'''
n=int(input())
arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))
arr.insert(0,[0,0,0])
arr=sorted(arr, key=lambda x:x[0], reverse=True)
dy=[0]*(n+1)
dy[0]=arr[0][1]
res=0

for i in range(n+1):
    max_h=0
    for j in range(i-1,-1,-1):
        if arr[i][2]<arr[j][2] and dy[j]>max_h:
            max_h=dy[j]
    dy[i]=max_h+arr[i][1]
    if res<dy[i]:
        res=dy[i]

print(res)