import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')

def test_films(films):
    for c in range(W):
        count = 0
        before = -1
        test_pass = False
        for r in range(D):
            if films[r][c] == before:
                count += 1
            else:
                count = 1
                before = films[r][c]
            if count >= K:
                test_pass = True
                break
        if not test_pass:
            return False
    return True

def dfs(films, cnt, idx):
    global answer

    if test_films(films):
        answer = min(answer, cnt)
    
    if answer <= cnt:
        return

    next_films = films[:]
    for i in range(idx, D):
        next_films[i] = A
        dfs(next_films, cnt+1, i+1)
        next_films[i] = B
        dfs(next_films, cnt+1, i+1)
        next_films[i] = films[i]


T = int(input())
A = (0,) * 20
B = (1,) * 20

for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    films = [list(map(int, input().split())) for _ in range(D)]

    answer = K
    dfs(films, 0, 0)
    print(f'#{tc} {answer}')