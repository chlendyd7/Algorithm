#5430 AC
from collections import deque
import sys; input=sys.stdin.readline

T = int(input())

for _ in range(T):
    hamsu = input().rstrip()
    n = int(input())
    ls = input().rstrip()[1:-1].split(',')
    que = deque(ls)

    reverse, flag = 0, 0

    if n == 0:
        que = []
    
    for j in hamsu:
        if j == 'R':
            reverse +=1
        else:
            if len(que) < 1:
                flag = 1
                print('error')
                break
            else:
                if reverse%2 == 0:
                    que.popleft()
                else:
                    que.pop()
    if flag == 0:
        if reverse %2 == 0:
                print('['+ ','.join(que) + ']')
        else:
            que.reverse()
            print('['+ ','.join(que) + ']')


    
    
    
