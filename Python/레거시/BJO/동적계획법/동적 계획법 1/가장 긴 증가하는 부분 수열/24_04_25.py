n=int(input())
a_list = list(map(int,input().split()))
a_list.insert(0,0)
dy=[0]*1001

for i in range(1,n+1):
    for j in range(i):
        if a_list[j] < a_list[i]:
            dy[i] = max(dy[i], dy[j]+1)


print(max(dy))
