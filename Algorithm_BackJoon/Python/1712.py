a, b ,c = input().split()
i = 1
cnt=0
if b >= c :
    cnt = -1
else:
    while (c*i)<(a+b*i):
        cnt +=1
        i +=1
        print(1)
print(cnt) n