'''
- 인도네시아 내의 모든 섬을 해저터널로 연결하려 함
- 직접적으로 연결된 경우도 있지만 간접적으로 연결 된 경우도 있다

# 조건
- 환경 부담금 정책이 있음
환경 부담 세율(E)와 각 해저터널 길이(L)의 제곱(E *L^2)만큼 지불


# 입력
첫 줄은 전테 테스트 케이스
섬의 개수 N이 주어짐
각 섬들의 정수인 X좌표, 세 번째 줄에는 각 섬들의 정수인 Y좌표가 주어짐
마지막에 E가 주어짐

# 접근 방법
graph를 만들고 visited를 체크해서 모든 섬을 방문하기
세율을 어떻게 접근 해야할까

MST(최소 스패닝 트리)

'''
def solution():
    N = int(input().strip())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input().strip())

    visited = [False] * N
    min_edge = [float('inf')] * N
    min_edge[0] = 0

    total_cost = 0

    for _ in range(N):
        u = -1
        min_val = 1e9
        for i in range(N):
            if not visited[i] and min_edge[i] < min_val:
                min_val = min_edge[i]
                u = i
    
    visited[u] = True
    total_cost += min_val

    for v in range(N)
T = int(input().strip())
for t in range(1, T + 1):
    print(f'#{t} {solution()}')