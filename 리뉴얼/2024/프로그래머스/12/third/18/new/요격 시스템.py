    # Python 풀이
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])  # 진출 기준으로 sort
    print(targets)
    check = -1 # 가장 왼쪽에서부터 탐색 해갈 것.
    for idx in range(len(targets)):
        if check <= targets[idx][0]:  # 진입 기준
            print(targets[idx][0])
            check = targets[idx][1]
            answer += 1
    return answer


targets = [[4,5],[4,8],[10,14],[11,13],[5,12],[3,7],[1,4]]
print(solution(targets))
