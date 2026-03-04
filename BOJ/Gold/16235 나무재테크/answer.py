import sys
from collections import deque

# 빠른 입력을 위해 사용
input = sys.stdin.readline

def solve():
    # 1. 입력 및 초기화
    N, M, K = map(int, input().split())
    
    # 겨울에 추가될 양분 정보
    A = [list(map(int, input().split())) for _ in range(N)]
    
    # 현재 땅의 양분 상태 (초기값은 모두 5)
    board = [[5] * N for _ in range(N)]
    
    # 나무 정보 (2차원 배열 안에 deque를 두어 나이순 관리)
    trees = [[deque() for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        r, c, age = map(int, input().split())
        trees[r-1][c-1].append(age)

    # 처음에 입력받은 나무들은 나이순으로 정렬되어 있지 않을 수 있으므로 한 번 정렬
    for r in range(N):
        for c in range(N):
            if trees[r][c]:
                # deque를 정렬한 뒤 다시 deque로 만듦
                trees[r][c] = deque(sorted(trees[r][c]))

    directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

    # 2. K년 동안 시뮬레이션 반복
    for _ in range(K):
        # --- 봄 & 여름 ---
        # 봄에 죽은 나무를 바로 여름 양분으로 계산하기 위해 한 루프에서 처리
        for r in range(N):
            for c in range(N):
                if not trees[r][c]:
                    continue
                
                alive_trees = deque()
                dead_nutrient = 0
                
                # 봄: 나이가 어린 나무(앞쪽)부터 양분 섭취
                while trees[r][c]:
                    age = trees[r][c].popleft()
                    if board[r][c] >= age:
                        board[r][c] -= age
                        alive_trees.append(age + 1)
                    else:
                        # 여름: 양분 부족으로 죽은 나무는 즉시 양분으로 예약
                        dead_nutrient += (age // 2)
                
                trees[r][c] = alive_trees
                board[r][c] += dead_nutrient

        # --- 가을 & 겨울 ---
        for r in range(N):
            for c in range(N):
                # 가을: 나무 번식
                for age in trees[r][c]:
                    if age % 5 == 0:
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if 0 <= nr < N and 0 <= nc < N:
                                # ★핵심: 새로 태어난 나이 1 나무를 '앞'에 넣음
                                # 이 한 줄 덕분에 다음 해 봄에도 자동 정렬 상태 유지!
                                trees[nr][nc].appendleft(1)
                
                # 겨울: 기계가 양분 보충
                board[r][c] += A[r][c]

    # 3. 결과 출력: 살아남은 나무의 총 개수
    answer = 0
    for r in range(N):
        for c in range(N):
            answer += len(trees[r][c])
    print(answer)

solve()
