def solution(n, results):
    # 1. 그래프 초기화
    graph = [[False] * (n + 1) for _ in range(n + 1)]
    
    # 2. 승리 관계를 그래프에 기록
    for win, lose in results:
        graph[win][lose] = True

    # 3. 플로이드-워셜 알고리즘으로 간접 승리 관계 계산
    for k in range(1, n + 1):  # 경유점
        for i in range(1, n + 1):  # 출발점
            for j in range(1, n + 1):  # 도착점
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True

    # 4. 순위를 알 수 있는 선수 계산
    answer = 0
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if graph[i][j] or graph[j][i]:  # 승리하거나 패배한 경우
                count += 1
        if count == n - 1:  # 다른 모든 선수와 관계가 있다면 순위 확정 가능
            answer += 1

    return answer
