n = int(input())
for _ in range(n):
    k = int(input())
    map = {}
    answer = 1
    for _ in range(k):
        cloth = input().split()
        if not cloth[1] in map:
            map[cloth[1]] = 1
        else:
            map[cloth[1]] += 1

    for k in map.keys():
        answer = answer * (map[k]+1)
    print(answer-1)