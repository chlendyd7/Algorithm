import sys
#sys.stdin = open("input.txt", "rt")
n, k=map(int, input().split())
a = list(map(int, input().split()))
b = set()
for i in range(n):#n 전까지, 중복방지
    for j in range(i+1, n):
        for m in range(j+1, n):#제일 뒤편부터 돌아야함
            b.add(a[i] + a[j]+ a[m])
b = list(b)#sort 기능이 set에는 없음
b.sort(reverse=True)
print(b[k-1])