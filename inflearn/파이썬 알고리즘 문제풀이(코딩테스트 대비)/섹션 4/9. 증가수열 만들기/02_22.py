# 증가수열 길이 측정하는거 1
# 마지막에 가져간것 비교
# 없으면 break
from collections import deque


n= int(input())
ls = list(map(int,input().split()))
cnt = 1
final = min(ls[0], ls[-1])
ls = deque(ls)
check = ""
while ls:
    if ls[0] < ls[-1]:
        if ls[0] > final:
            final = ls[0]
            cnt +=1
            ls.popleft()
            check += "L"
    elif ls[0] > ls[-1]:
        if ls[-1] > final:
            final = ls[-1]
            cnt +=1
            ls.pop()
            check += "R"
    else:
        break

print(cnt)
print(check)

