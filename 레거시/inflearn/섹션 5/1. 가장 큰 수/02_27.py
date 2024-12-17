from collections import deque
n, m = map(int,input().split())
# int는 list화 하여 인덱싱 불가능
n = list(map(int, str(n)))
stack = []

for x in n:
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)

if m>0:
    stack=stack[:-m] # -m개를 제외한 나머지를 반환
res="".join(map(str, stack))
print(res)