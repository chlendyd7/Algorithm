from itertools import combinations
N, M, D = map(int, input().split())
targets = []
for r in range(N):
    inputs = list(map(int, input().split()))
    for c in range(M):
        if inputs[c] == 1:
            targets.append((r,c))

from copy import deepcopy
def simulation(archurs):
    new_targets = deepcopy(targets)
    cnt = 0
    while new_targets:
        target_set = set()
        for a_c in archurs:
            target_coord = None
            dist = D+1
            left = M
            for r,c in new_targets:
                n_dist = abs(N-r) + abs(a_c - c)
                if n_dist < dist:
                    dist = n_dist
                    left = c
                    target_coord = (r,c)
                elif dist == n_dist:
                    if c < left:
                        target_coord = (r,c)

            if target_coord:
                target_set.add(target_coord)

        cnt += len(target_set)
        new_targets = [t for t in new_targets if t not in target_set]

        next_target = []
        for r, c in new_targets:
            if r + 1 < N:
                next_target.append((r+1, c))
        new_targets = next_target

    return cnt

mx = 0
for archurs in combinations(range(M), 3):
    mx = max(mx, simulation(archurs))

print(mx)

