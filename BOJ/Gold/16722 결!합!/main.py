from itertools import combinations

pictures = [None] * 10
for i in range(1, 10):
    s, c, b = input().split()
    pictures[i] = s,c,b

n = int(input())
check_s = set()

def check(nums):
    p1, p2, p3 = pictures[nums[0]], pictures[nums[1]], pictures[nums[2]]

    for i in range(3):
        attr = {p1[i], p2[i], p3[i]}
        if len(attr) == 2:
            return False
        return True

all_hap_combi = set()
for comb in combinations(range(1, 10), 3):
    if check(comb):
        all_hap_combi.add(tuple(sorted(comb)))

        

result = 0
end = False
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'H':
        v1, v2, v3 = int(cmd[1]), int(cmd[2]), int(cmd[3])
        comb = tuple(sorted([v1,v2,v3]))
        
        if comb not in check_s and check(comb):
            result += 1
            check_s.add(comb)
        else:
            result -= 1
    elif cmd[0] == 'G':
        if len(all_hap_combi) == len(check_s) and not end:
            result += 3
            end= True
        else:
            result -= 1

print(result)