'''
- N개의 숫자로 구성된 숫자열
- M 개의 숫자로 구성된 숫자열

- 긴쪽의 양끝을 벗어나면 안됨
- 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라
- 완전탐색?
'''
def solution(big, small):
    mx, mn = len(big), len(small)
    result = 0
    for i in range(mx - mn + 1):
        tmp = 0
        for j in range(mn):
            tmp += big[j+i] * small[j]
        result = max(tmp, result)
    
    return result

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    n_list = list(map(int, input().split()))
    m_list = list(map(int, input().split()))
    if N > M:
        result = solution(n_list, m_list)
    else:
        result = solution(m_list, n_list)
    
    print(f'#{t} {result}')


def max_dot_product(longer, shorter):
    max_sum = float('-inf')
    for i in range(len(longer) - len(shorter) + 1):
        total = sum(longer[i + j] * shorter[j] for j in range(len(shorter)))
        max_sum = max(max_sum, total)
    return max_sum

def max_dot_product(a, b):
    # 항상 a가 긴 배열
    if len(a) < len(b):
        a, b = b, a
    return max(
        sum(a[i + j] * b[j] for j in range(len(b)))
        for i in range(len(a) - len(b) + 1)
    )

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    if N >= M:
        result = max_dot_product(A, B)
    else:
        result = max_dot_product(B, A)
    
    print(f"#{t} {result}")
    
