n = int(input())
a = [list(map(int,input().split())) for _ in range(n)]
mx = 0
cnt = 0

for j in range(n):
    sum1 = sum2 = 0
    for z in range(n):
        sum1 +=a[z][j]
        sum2 +=a[j][z]
    if sum1>mx:
        mx = sum1
    if sum2>mx:
        mx = sum2
sum1=sum2=0
for j in range(n):
    sum1 +=a[j][j]
    sum2 +=a[j][n-j-1] #역순
if sum1 > mx:
    mx = sum1
if sum2 > mx:
    mx = sum2
print(mx)