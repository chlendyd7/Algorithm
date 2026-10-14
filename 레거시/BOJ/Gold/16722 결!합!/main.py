from itertools import combinations

# 1. 그림 정보 입력
pictures = [None] * 10
for i in range(1, 10):
    pictures[i] = input().split()

# 2. '합' 조건 체크 함수
def check(nums):
    p1, p2, p3 = pictures[nums[0]], pictures[nums[1]], pictures[nums[2]]
    for i in range(3):
        temp = {p1[i], p2[i], p3[i]}
        if len(temp) == 2:
            return False
    return True

# 3. 모든 가능한 '합' 조합 미리 계산
all_sets = set()
for comb in combinations(range(1, 10), 3):
    if check(comb):
        all_sets.add(tuple(sorted(comb)))

# 4. 게임 시뮬레이션
n = int(input())
result = 0
check_sets = set()
gyeol_flag = False  # '결'을 이미 성공했는지 체크하는 변수 추가

for _ in range(n):
    cmd = input().split()

    if cmd[0] == 'H': # 합
        v1, v2, v3 = int(cmd[1]), int(cmd[2]), int(cmd[3])
        comb = tuple(sorted([v1, v2, v3]))
        
        # 정답셋에 있고, 내가 아직 찾지 않은 조합인 경우
        if comb in all_sets and comb not in check_sets:
            result += 1
            check_sets.add(comb)
        else:
            result -= 1
            
    else: # 결
        # 모든 합을 찾았고, '결'을 처음 성공하는 경우
        if len(check_sets) == len(all_sets) and not gyeol_flag:
            result += 3
            gyeol_flag = True # '결' 성공 상태로 변경
        else:
            # 이미 '결'을 했거나, 아직 찾을 합이 남았는데 '결'을 외친 경우
            result -= 1 # 보통 결 실패는 -1점입니다. 문제에 따라 -3이면 수정하세요.

print(result)