n=int(input())
ls = list(map(int,input().split()))


lt=0
rt = n-1
cnt = 0
last = 0
res=""
tmp = []
while lt<=rt:
    if ls[lt]>last:
        tmp.append((ls[lt], 'L'))
    if ls[rt]>last:
        tmp.append((ls[rt], 'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res+=tmp[0][1]
        if tmp[0][1] == 'L':
            lt+=1
        else:
            rt-=1
        last=tmp[0][0]
        tmp.clear()

print(len(res))
print(res)

''''
    last: 2,    3       
    ls: [4513]  [451]
    
    
'''