from collections import defaultdict
def solution():
    n = int(input())
    dic = {
        2: 0,
        3: 0,
        5: 0,
        7: 0,
        11: 0,
    }

    for k in sorted(dic.keys(), reverse=True):
        while (n % k) == 0:
            dic[k] = dic[k] + 1
            n //= k
    return(' '.join(map(str, (dic[k] for k in sorted(dic.keys())))))


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')