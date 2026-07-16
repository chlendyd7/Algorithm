'''
    주기적으로 외벽 점검
'''

def solution(n, weak, dist):
    answer = 0
    return answer




'''
12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
'''

from itertools import permutations

def solution(n, weak, dist):
    # 원형 벽을 선형으로 변환
    # weak 지점들 사이의 거리 계산
    weak_distances = []
    for i in range(len(weak)):
        next_i = (i + 1) % len(weak)
        if next_i == 0:  # 마지막에서 처음으로
            distance = n - weak[i] + weak[0]
        else:
            distance = weak[next_i] - weak[i]
        weak_distances.append(distance)
    
    dist.sort(reverse=True)  # 거리 긴 친구부터 시도
    
    # 친구 명수 최소부터 최대까지 시도
    for num_friends in range(1, len(dist) + 1):
        # 이 명수의 친구들 조합 모두 시도
        for friend_combo in permutations(dist, num_friends):
            # 원형이므로 시작점을 다르게 설정해서 시도
            for start_idx in range(len(weak)):
                # weak_distances를 start_idx부터 시작하도록 재배열
                rotated = weak_distances[start_idx:] + weak_distances[:start_idx]
                
                # 이 친구 조합과 시작점으로 모든 약한 지점 커버 가능?
                covered = True
                idx = 0
                for friend_dist in friend_combo:
                    cumsum = 0
                    while idx < len(rotated) and cumsum + rotated[idx] <= friend_dist:
                        cumsum += rotated[idx]
                        idx += 1
                    
                    if idx == len(rotated):  # 모든 지점 커버됨
                        break
                
                if idx == len(rotated):  # 성공
                    return num_friends
    
    return -1



# 파이썬
from itertools import permutations
def solution(n, weak, dist):
    L = len(weak)
    cand = []
    weak_point = weak + [w+n for w in weak]  # 선형으로
    print(weak_point)
    for i, start in enumerate(weak):
        for friends in permutations(dist):  # 순열 이용
            print(friends)
            count = 1
            position = start
            # 친구 조합 배치
            for friend in friends:
                position += friend
                # 끝 포인트까지 도달 못했을 때
                if position < weak_point[i+L-1]:
                    count += 1  # 친구 더 투입
                    # 현재 위치보다 멀리 있는 취약지점 중 가장 가까운 위치로
                    position = [w for w in weak_point[i+1:i+L]
                                if w > position][0]
                else:  # 끝 포인트까지 도달
                    cand.append(count)
                    break

    return min(cand) if cand else -1



from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    linear = weak + [w + n for w in weak]  # 원형 → 직선
    dist.sort(reverse=True)

    for count in range(1, len(dist) + 1):
        for perm in permutations(dist, count):
            for start in range(length):  # 시작 weak 포인트
                idx = start
                for d in perm:
                    reach = linear[idx] + d
                    while idx < start + length and linear[idx] <= reach:
                        idx += 1
                    if idx >= start + length:
                        return count
    return -1

def solution(n, weak, dist:list):
    length = len(weak)
    linear = weak + [w + n for w in weak]
    dist.sort(reverse=True)
    
    for count in range(1, len(dist) + 1):
        for perm in permutations(dist, count):
            for start in range(length):
                idx = start
                for d in perm:
                    reach = linear[idx] + d
                    while idx < start + length and linear[idx] <= reach:
                        idx += 1
                    if idx >= start + length:
                        return count
'''
12	[1, 5, 6, 10]	[1, 2, 3, 4]	2
12	[1, 3, 4, 9, 10]	[3, 5, 7]	1
'''