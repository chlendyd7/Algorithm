n = int(input())
c_list=[0]*(n+1)
cnt = 0
for i in range(2, n+1):
    if c_list[i]==0:
        cnt +=1
        for j in range(i, n+1, i):
            c_list[j]=1
print(cnt)
