# https://school.programmers.co.kr/learn/courses/30/lessons/60062
'''
    주기적으로 외벽 점검

    사람 다 뽑아뒀고 [4,3]
    어디부터 시작할래
    weak[0] ~ weak[1]? => start
    시작 idx가 얼마까지 인지 체크
    weak = [1, 5, 6, 10, 13, 17, 18, 22]
    idx 3, 4, 

    check = 4, w=4, cnt=3, idx=0
    weak[3] + 4 > weak[3]
    idx += 1, idx = 1

    idx < check, 10 + 4 != weak[5] 17
    cnt => 4




'''
from itertools import permutations

def solution(n, weak, dist):
    check = len(weak)
    dist.sort(reverse=True)
    weak += [w+n for w in weak]

    for count in range(1, check+1):
        for workers in permutations(dist, count):
            for start in range(check):
                idx = 0
                cnt = start
                for w in workers:
                    while idx < check and weak[cnt] + w >= weak[cnt + idx]:
                        idx += 1
                    cnt += idx
                if idx >= check:
                    return count

    return -1

print(solution(12,[1, 5, 6, 10],[1, 2, 3, 4]))



'''
12,[1, 5, 6, 10],[1, 2, 3, 4]	2
12,[1, 3, 4, 9, 10],[3, 5, 7]	1
'''
