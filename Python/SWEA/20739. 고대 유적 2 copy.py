def find_max_line(arr):
    print(arr)
    max_len = 0
    for line in arr:
        cnt = 0
        for val in line + [0]:  # 마지막에 0 추가해서 경계 처리
            if val == 1:
                cnt += 1
                max_len = max(max_len, cnt)
            else:
                cnt = 0
    return max_len

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행과 열 모두 확인
    max_row = find_max_line(arr)
    # 열은 전치 행렬로 변환
    convert = zip(*arr)
    print('max_col:')
    max_col = find_max_line(list(c) for c in convert)
    mx = max(max_row, max_col)

    # 조건에 따라 출력
    print(f'#{tc} {0 if mx == 1 else mx}')
