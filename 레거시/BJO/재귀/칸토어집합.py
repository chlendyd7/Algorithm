




def cantor(a,n):
    if n==1:
        return
    for i in range(a+n//3, a+(n//3)*2):
        result[i]=' '
    cantor(a, n//3),
    cantor(a+n//3*2, n//3)

import sys
while True:
    try :
        N = int(sys.stdin.readline())
        result = ['-']*(3**N) # 최초 리스트 집합
        cantor(0,3**N) # 자르기
        print(''.join(result))
    except:
        break