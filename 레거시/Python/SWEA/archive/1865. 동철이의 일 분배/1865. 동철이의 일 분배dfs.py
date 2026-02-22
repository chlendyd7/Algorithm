'''
    최대값 찾기
    N명 N개의 일
    그리디 아님
'''
def solution():
    N = int(input())
    min_val = 1
    visited = [0] * N
    for _ in range(N):
        data = list(map(int, input().split()))
        best_value = 0
        for i in range(N):
            if visited[i]:
                continue
            if data[i] > best_value:
                best_value = data[i]
                idx = i
        visited[idx] = 1
        print(best_value)
        min_val *= best_value / 100
    print(f'{min_val*100:.6f}')
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')