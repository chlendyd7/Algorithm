n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m=int(input())

for i in range(m):
    h, t, k = map(int,input().split())
    if t == 0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))#인덱스 번호를 받아 그 값을 리턴, 뒤의 리스트들은 당겨온다
    else:
        for _ in range(k):
            a[h-1].insert(0,a[h-1].pop())#인덱스번호를 쓰지 않을 시 가장 뒤의 값을 pop



#믹스에 있는 값을 꺼내서
res = 0
s=0
e = n-1
for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)