T = int(input())

for tc in range(1, T+1):

    n, m, k = map(int, input().split())
    scouter = [list(input()) for _ in range(n)]
    answer_r, answer_c = 0, 0
    for r in range(n-m+1):
        for c in range(n-m+1):

            cur_count = 0
            for check_r in range(r, r+m):
                for check_c in range(c, c+m):
                    if scouter[check_r][check_c] == '*':
                        cur_count += 1
            if cur_count != k:
                if r == n-m and c == n-m and answer_r == 0 and answer_c == 0:
                    answer_r, answer_c = -1, -1
                    print(f"#{tc} {answer_r} {answer_c}")
                    break
            else:
                answer_r, answer_c = r, c
                print(f"#{tc} {answer_r} {answer_c}")
                break