import sys
input = sys.stdin.readline  # 속도를 위해 입력 함수만 재정의

n = int(input())
# 말씀하신 정석적인 board 선언 방식
board = [list(map(int, input().split())) for _ in range(n)]

# 누적 합 배열 (인덱스 계산 편의를 위해 n+2 크기)
pref1 = [[0] * (n + 2) for _ in range(n + 2)] # 주대각선 (\)
pref2 = [[0] * (n + 2) for _ in range(n + 2)] # 부대각선 (/)

# 1. 누적 합 미리 구하기
for i in range(1, n + 1):
    for j in range(1, n + 1):
        val = board[i-1][j-1]
        pref1[i][j] = pref1[i-1][j-1] + val
        pref2[i][j] = pref2[i-1][j+1] + val

max_beauty = -float('inf')

# 2. 모든 크기(k)의 정사각형 탐색
for k in range(2, n + 1):
    for i in range(k, n + 1): #이 루프에서 i는 정사각형의 맨 아래 행(Row) 번호를 의미합니다.
        for j in range(1, n - k + 2): #이 루프에서 j는 정사각형의 맨 왼쪽 열(Column) 번호를 의미합니다.
            # 시작점과 끝점 계산
            r1, c1 = i - k + 1, j
            r2, c2 = i, j + k - 1
            
            # 주대각선(\) 합: 끝점 - 시작점 이전
            main_diag = pref1[r2][c2] - pref1[r1-1][c1-1]
            # 부대각선(/) 합: 왼쪽 아래 끝점 - 오른쪽 위 시작점 이전
            anti_diag = pref2[r2][c1] - pref2[r1-1][c2+1]
            
            max_beauty = max(max_beauty, main_diag - anti_diag)

print(max_beauty)
