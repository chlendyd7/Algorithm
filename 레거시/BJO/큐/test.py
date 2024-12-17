from collections import deque
n,k = map(int,input().split())
ls = [i for i in range(1, n+1)]

ls = deque(ls)
print(ls[0])


print(ls)
