'''
    주기적으로 외벽 점검
'''

from itertools import permutations


def solution(n, weak, dist:list):
    length = len(weak)
    weak += [w + n for w in weak]
    dist.sort(reverse=True)
    for count in range(1, len(dist)+1):
        for workers in permutations(dist, count):
            for start in range(length): # start
                idx = start
                for work in workers:
                    reach = weak[idx] + work
                    # 이번 바퀴를 정확하게 보기 위해 idx < start + length
                    while idx < start + length and weak[idx] <= reach:
                        idx += 1

                    if idx >= start + length:
                        return count
                    
    return -1

for t in permutations([4,3,2,1],2):
    print(t)

'''
12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
'''
