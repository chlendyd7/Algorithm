'''
    순서대로?
    deque해서 INDEX POP 해보자
    마지막에 길이로 CHECK
'''
from collections import deque

need_subject = input()
n = int(input())
for _ in range(1,n+1):
    check = deque(need_subject)
    subject = input()
    for s in subject:
        if s in check:
            if check and  s != check.popleft(): #이 부분 체크하기 없는 경우로 만들었으
                print(f'#{_} ' + "NO")
                break
    print(f'#{_} ' + "NO" if check else  f"#{_} YES")
