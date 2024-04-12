# 하나로 정렬, 나머지 비교
n = int(input())
ls= []
for _ in range(n):
    a, b = map(int, input().split())
    ls.append((a,  b))

ls.sort(reverse=True)
et = 0
cnt = 0
for s, e in ls:
    if e>et:
        cnt+=1
        et=e
print(cnt)