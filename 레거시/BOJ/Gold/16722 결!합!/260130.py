from itertools import combinations

pictures = [None] * 10
for i in range(1, 10):
    pictures[i] = input().split()

def check(nums):
    p1, p2, p3 = pictures[nums[0]], pictures[nums[1]], pictures[nums[2]]
    for i in range(3):
        temp = {p1[i], p2[i], p3[i]}
        if len(temp) == 2:
            return False
    return True

all_sets = set()
for comb in combinations(range(1,10), 3):
    if check(comb):
        all_sets.add(comb)

n = int(input())
result = 0
check_sets = set()
gyeol_flag = False  # '결'을 이미 성공했는지 체크하는 변수 추가
for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'H':
        v1, v2, v3 = int(cmd[1]), int(cmd[2]), int(cmd[3])
        comb = tuple(sorted([v1,v2,v3]))
        if comb not in check_sets and comb in all_sets:
            result += 1
            check_sets.add(comb)
        else:
            result -= 1
    else: #결
        if len(check_sets) == len(all_sets) and not gyeol_flag:
            result += 3
            gyeol_flag = True # '결' 성공 상태로 변경
        else:
            result -= 1
print(result)


