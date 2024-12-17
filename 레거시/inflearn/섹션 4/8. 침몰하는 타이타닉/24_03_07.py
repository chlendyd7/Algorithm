# 2명이하
# 가장 큰 사람부터 태우기
# 가장 큰 사람, 가장 작은 사람 안되면 걍 하나 더하기

n,m = map(int,input().split())
ls = list(map(int,input().split()))

ls.sort()
cnt = 0
while ls:
    if len(ls) == 1:
        cnt +=1
        break
    if ls[0]+ls[-1] > m:
        ls.pop()
        cnt+=1
    else:
        ls.pop(0)
        ls.pop()
        cnt+=1

print(cnt)