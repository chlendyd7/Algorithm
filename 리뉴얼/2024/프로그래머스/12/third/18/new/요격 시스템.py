    # Python 풀이
def solution(targets):
    answer = 0
    targets.sort(key=lambda x: x[1])  # 진출 기준으로 sort
    print(targets)
    check = -1 # 가장 왼쪽에서부터 탐색 해갈 것.
    for idx in range(len(targets)):
        if check <= targets[idx][0]:  # 진입 기준
            check = targets[idx][1]
            answer += 1
    return answer
    