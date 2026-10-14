from itertools import permutations
n = int(input())
innings = [list(map(int, input().split()))for _ in range(n)]
max_result = 0
for p in permutations(range(1, 9)):
    p = list(p)
    player = p[:3] + [0] + p[3:]
    score = 0
    current_play = 0
    
    for inning in innings:
        base = 0
        out = 0
        while out < 3:
            current_result = inning[player[current_play]]
            if current_result == 0:
                out += 1
            else:
                base = (base << current_result) | (1 << (current_result - 1))
                score += bin(base >> 3).count('1')
                base &= 7
            current_play = (current_play + 1) % 9
    max_result = max(max_result, score)
print(max_result)
