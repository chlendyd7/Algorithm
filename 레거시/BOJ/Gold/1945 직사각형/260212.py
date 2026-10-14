n = int(input())
events = []
for _ in range(n):
    r1,c1,r2,c2 = map(int, input().split())
    events.append((r1/c2, 1))
    events.append((r2/c1, -1))

events.sort(key=lambda x: (x[0], x[-1]))
max_cnt = 0
current_cnt = 0
for _, type in events:
    current_cnt += type
    max_cnt = max(max_cnt, current_cnt)

print(max_cnt)
