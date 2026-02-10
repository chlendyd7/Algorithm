'''
BOJ.Gold.1184 귀농.main의 Docstring
1. 핵심 아이디어: "꼭짓점"을 기준으로 생각하기두 사람이 땅을 나누는 기준은 항상 어떤 격자의 교차점입니다. 임의의 꼭짓점 $(i, j)$를 기준으로 땅을 네 구역으로 나눌 수 있습니다.구역 1 (좌상): $(0,0)$ ~ $(i,j)$ 사이의 부분 사각형구역 2 (우상): $(0,j+1)$ ~ $(i, N-1)$ 사이의 부분 사각형구역 3 (좌하): $(i+1, 0)$ ~ $(N-1, j)$ 사이의 부분 사각형구역 4 (우하): $(i+1, j+1)$ ~ $(N-1, N-1)$ 사이의 부분 사각형이때 문제의 조건인 "꼭짓점을 맞대고 있는 경우"는 다음 두 가지 조합입니다.좌상(1) 구역의 사각형 하나와 우하(4) 구역의 사각형 하나가 만날 때우상(2) 구역의 사각형 하나와 좌하(3) 구역의 사각형 하나가 만날 때2. 접근 단계1단계: 2차원 누적 합 구하기어떤 사각형의 합을 $O(1)$로 빠르게 구하기 위해 미리 누적 합 테이블을 만듭니다.
$$S[i][j] = \text{board}[i][j] + S[i-1][j] + S[i][j-1] - S[i-1][j-1]$$2단계: 모든 꼭짓점 순회 (중심점 설정)$(0, 0)$부터 $(N-2, N-2)$까지 모든 교차점을 기준점으로 잡습니다.3단계: 각 구역의 사각형 합 계산 및 비교기준점 $(i, j)$에 대하여:좌상 방향으로 만들 수 있는 모든 사각형의 합을 구해 리스트(또는 Map)에 저장합니다.우하 방향으로 만들 수 있는 모든 사각형의 합을 구하며, 좌상 리스트에 같은 값이 있는지 확인하여 카운트합니다.우상 vs 좌하 조합에 대해서도 동일하게 반복합니다.
'''
from collections import defaultdict


def get_sum(r1, c1, r2, c2):
    return pref[r2+1][c2+1] - pref[r1][c2+1] - pref[r2+1][c1] + pref[r1][c1]
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
pref = [[0] *(n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        pref[i][j] = board[i-1][j-1] + pref[i-1][j] + pref[i][j-1] - pref[i-1][j-1]

ans = 0
for r in range(n-1):
    for c in range(n-1):
        sums = defaultdict(int)
        for i in range(r+1):
            for j in range(c+1):
                sums[get_sum(i,j,r,c)] += 1

    for i in range(r+1, n):
        for j in range(c+1, n):
            val = get_sum(r+1, c+1, i, j)
            if val in sums:
                ans += sums[val]

    sums = defaultdict(int)
    for i in range(r+1):
        for j in range(c+1, n):
            sums[get_sum(i,c+1, r,j)] += 1
    
    for i in range(r+1, n):
        for j in range(c+1):
            val = get_sum(r+1, j, i, c)
            if val in sums:
                ans += sums[val]

print(ans)