'''
    두 팀은 경기가 시작하기 전까지 타순(타자가 타석에 서는 순서)을 정해야 하고, 
    경기 중에는 타순을 변경할 수 없다. 9번 타자까지 공을 쳤는데 3아웃이 발생하지 않은 상태면 이닝은 끝나지 않고, 
    1번 타자가 다시 타석에 선다. 타순은 이닝이 변경되어도 순서를 유지해야 한다. 
    예를 들어, 2이닝에 6번 타자가 마지막 타자였다면, 3이닝은 7번 타자부터 타석에 선다.
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
        b1, b2, b3 = 0,0,0
        
        while out < 3:
            result = inning[order[current_play]]
            if result == 0:
                out += 1
            elif result == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif result == 2:
                score += (b2+b3)
                b1, b2, b3 = 0, 1, b1
            elif result == 3: # 3루타
                score += (b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 1
            elif result == 4:
                score += (b1 + b2 + b3 + 1)
                b1, b2, b3 = 0,0,0
            
            
            current_play = (current_play + 1) % 9
    max_score = max(max_score, score)
print(max_score)
