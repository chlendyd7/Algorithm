import math


n,l = map(int, input().split())
ports = [list(map(int, input().split())) for _ in range(n)]
ports.sort()

current_end = 0
cnt = 0
for s, e in ports:
    if current_end >= e:
        continue

    s = max(s, current_end)
    # tmp = (e -s + l - 1) // l
    tmp = math.ceil((e - s) / l)
    current_end = s + tmp * l
    cnt += tmp

print(cnt)