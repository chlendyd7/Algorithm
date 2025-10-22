from collections import defaultdict


def solution():
    lst = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    won = { l : 0 for l in lst }
    money = int(input())
    for k in sorted(won.keys(), reverse=True):
        while money >= k:
            won[k] += 1
            money -= k
        # won[k] = money // k
        # money %= k
    return ' '.join(map(str, (k for k in won.values())))


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')

