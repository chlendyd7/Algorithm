def solution(n, results):
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    answer = 0

    # 경기 결과를 그래프에 반영
    for w, l in results:
        graph[w][l] = True

    # 플로이드-워셜 알고리즘으로 승리 관계를 업데이트
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    # 각 선수에 대해 승패가 명확한 선수 수를 카운트
    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:  # i가 j를 이기거나 j가 i를 이김
                cnt += 1
        if cnt == n - 1:  # 자신 제외한 모든 선수와의 승패가 명확
            answer += 1

    return answer
