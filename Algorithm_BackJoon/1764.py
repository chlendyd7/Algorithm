import sys
input = sys.stdin.readline

n,m = map(int,input().split())
Nohear = set()
for i in range(n):
    Nohear.add(input().strip())
Nosee = set()
for j in range(m):
    Nosee.add(input().strip())

arr = sorted(list(Nohear & Nosee)) 
# list 는 & 연산이 안됨
# &를 통해서 중복되는 값을 찾아내서 새로운 list에 담아주었다.
# 사전순으로 출력해라는 조건이기에 sorted
print(len(arr))
for i in arr:
    print(i)
