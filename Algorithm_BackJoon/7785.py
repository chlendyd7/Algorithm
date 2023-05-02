import sys
input = sys.stdin.readline
n = int(input())
ls = {} 
#key와 value 값으로 접근하기 위함
for _ in range(n):
    name, inout = map(str, input().split())
    if inout == 'enter':
        ls[name] = 'enter' #enter이면 ls에 넣기
    else:
        del ls[name]  #아니면 del
names = sorted(ls,reverse=True)

for i in names:
    print(i)
