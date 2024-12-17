def solution(m, n, puddles):
    # DP 배열 초기화
    dp = [[-1] * m for _ in range(n)]
    puddles_set = set(map(tuple, puddles))  # puddles를 set으로 변환하여 O(1) 시간복잡도로 확인
    move = [(0, 1), (1, 0)]  # 오른쪽, 아래쪽 이동

    def dfs(x, y):
        if x == n - 1 and y == m - 1:  # 도착지에 도달한 경우
            return 1

        if dp[x][y] != -1:  # 이미 계산된 경우
            return dp[x][y]
        
        dp[x][y] = 0  # 현재 위치의 경로 수를 0으로 초기화
        
        for k in range(2):
            nx = x + move[k][0]
            ny = y + move[k][1]
            
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in puddles_set:
                dp[x][y] += dfs(nx, ny)  # 재귀 호출하여 경로 수 추가

        return dp[x][y]  # 현재 위치의 경로 수 반환

    answer = dfs(0, 0)  # 시작 위치에서 DFS 호출
    return answer % 1000000007  # 문제에서 요구하는 대로 1000000007로 나눈 나머지 반환
