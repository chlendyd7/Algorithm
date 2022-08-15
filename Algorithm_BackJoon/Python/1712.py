a, b ,c = input().split()
i = 1
cnt=0
while (c*i)<(a+b*i):
    cnt +=1
    i +=1
print(cnt)