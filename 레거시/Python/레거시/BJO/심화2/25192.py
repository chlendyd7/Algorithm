# 인사성 밝은 곰곰이
# 중복을 피하면 될 것 같아 set을 사용
import sys
input = sys.stdin.readline

n = int(input())
ls = set()
cnt = 0

for i in range(n):
    a = input().rstrip()
    if a == "ENTER":
        cnt += len(ls)
        ls.clear()
        continue
    ls.add(a)
    

cnt += len(ls)
print(cnt)