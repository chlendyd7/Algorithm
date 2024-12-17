# 자기보다 큰 숫자가 앞에 있으면 전진 해야한다.
n, m = map(int,input().split())
num = list(map(int,str(n)))
stack = []
for x in num:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)


if m!=0:
    stack=stack[:-m]
res = ''.join(map(str,stack))
print(res)