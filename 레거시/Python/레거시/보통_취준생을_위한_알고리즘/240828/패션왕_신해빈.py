n = int(input())
for _ in range(n):
    map = {}
    cloths_num = int(input())
    answer = 1
    for _ in range(cloths_num):
        a, b = input().split()
        if not b in map:
            map[b] = 1
        else:
            map[b] += 1
    
    for k in map.keys():
        answer = answer * (map[k]+1)
    print(answer-1)