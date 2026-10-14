n = int(input())

events = []
for i in range(n):
    c1,r1,c2,r2 = map(int, input().split())
    upper = r2/c1
    lower = r1/c2
    
    events.append((lower, 1))
    events.append((upper, -1))

    events.sort(key=lambda x: (x[0], -x[1]))
    
    max_count = 0
    current_count = 0
    for _, type in events:
        current_count += type
        max_count = max(max_count, current_count)
    print(max_count)
