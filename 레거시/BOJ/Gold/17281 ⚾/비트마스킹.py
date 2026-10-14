'''
    두 팀은 경기가 시작하기 전까지 타순(타자가 타석에 서는 순서)을 정해야 하고, 
    경기 중에는 타순을 변경할 수 없다. 9번 타자까지 공을 쳤는데 3아웃이 발생하지 않은 상태면 이닝은 끝나지 않고, 
    1번 타자가 다시 타석에 선다. 타순은 이닝이 변경되어도 순서를 유지해야 한다. 
    예를 들어, 2이닝에 6번 타자가 마지막 타자였다면, 3이닝은 7번 타자부터 타석에 선다.
    
    & (AND) 연산은 양쪽 다 1인 자리만 1로 남깁니다.
    따라서 base & 7을 하면 **0, 1, 2번 비트(1~3루)**는 그대로 남고, **3번 비트 이상(홈인 한 주자)**은 모두 0이 되어 사라집니다.
    
'''

from itertools import permutations


n = int(input())
max_score = 0
innings = [list(map(int, input().split())) for _ in range(n)]

for p in permutations(range(1,9)):
    p = list(p)
    order = p[:3] + [0] + p[3:]
    score = 0
    current_play = 0
    
    for inning in innings:
        out = 0
        base = 0
        
        while out < 3:
            result = inning[order[current_play]]
            if result == 0:
                out += 1
            else:
                # 안타(1)면 1칸 밀고 1루 추가, 2루타(2)면 2칸 밀고 2루(2) 추가...
                base = (base << result) | (1 << (result - 1))
                score += bin(base >> 3).count('1')
                base &= 7
            current_play = (current_play + 1) % 9

            # if result == 0:
            #     out += 1
            # elif result == 1:
            #     base = (base<<1) | 1
            # elif result == 2:
            #     base = (base<<2) | 2
            # elif result == 3: # 3루타
            #     base = (base << 3) | 4
            # elif result == 4:
            #     base = (base << 4) | 8

    max_score = max(max_score, score)
    base &= 7

print(max_score)
