a = input()
res=0
num = len(a)
for i in a:
    if i.isdecimal():
        res = res*10 + int(i)
print(res)
cnt = 0
for j in range(1, res+1):
    if res%j ==0:
        cnt+=1
print(cnt)
