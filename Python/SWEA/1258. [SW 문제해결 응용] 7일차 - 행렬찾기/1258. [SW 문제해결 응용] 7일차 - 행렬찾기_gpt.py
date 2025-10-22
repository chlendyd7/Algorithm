'''
🚩 문제 핵심

부분 행렬은 0이 없는 사각형으로 이루어져 있음.

부분 행렬들 사이에는 반드시 0이 존재 → 겹칠 일 없음.

대각선은 고려하지 않음 → 행과 열만 확장하면 됨.

출력 조건

행*열 크기 기준 오름차순

같으면 행 수 기준 오름차순

즉, 0이 아닌 시작점(i,j)을 찾으면 거기서 오른쪽과 아래로 얼마나 확장되는지 측정하면 됨.

🚩 올바른 접근

전체 행렬을 탐색하면서 matrix[i][j] != 0인 시작점 찾기

행 길이: i에서 아래로 0이 아닌 연속 행 계산

열 길이: j에서 오른쪽으로 0이 아닌 연속 열 계산

부분 행렬을 발견했으면, 탐색한 영역을 0으로 표시(또는 방문 체크) → 중복 탐지 방지

모든 부분 행렬을 찾아 (행, 열) 리스트에 저장

정렬:

sorted(matrices, key=lambda x: (x[0]*x[1], x[0]))
'''
def solution():
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] != 0:
                # 행 길이
                r = i
                while r < N and matrix[r][j] != 0:
                    r += 1
                # 열 길이
                c = j
                while c < N and matrix[i][c] != 0:
                    c += 1
                # 크기 저장
                result.append((r-i, c-j))
                # 방문 처리
                for x in range(i, r):
                    for y in range(j, c):
                        matrix[x][y] = 0

    # 정렬
    result.sort(key=lambda x: (x[0]*x[1], x[0]))
    output = [str(len(result))]
    for r, c in result:
        output.append(str(r))
        output.append(str(c))

    return ' '.join(output)


T = int(input())
for t in range(1, T+1):
    print(f"#{t} {solution()}")