import sys
input = sys.stdin.readline
n, m = map(int,input().split())
ls = {}

for i in range(n):
    name = input().strip()
    ls[name] = i+1

ls_reverse = dict(map(reversed, ls.items()))
#value 를 통해 key에 접근하는 방식을 구현하기 어렵다
#그래서 key와 value를 뒤집어서 다른 dict를 만들었다.
check = [input().strip() for m in range(m)]

for i in check:
    if i in ls:
        print(ls[i])
    else:
       print(ls_reverse[int(i)])
