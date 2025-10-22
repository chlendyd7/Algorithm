'''
    - k 번째 학생의 번호 학점
    - T, N 학생 수, K 학생 번호
'''
GRADE = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
def solution():
    N,K = map(int, input().split())
    result = []
    for _ in range(N):
        mid, final, task = map(int, input().split())
        result.append((mid * 0.35) + (final * 0.45) + (task * 0.2))
    
    k_score = result[K-1]
    result.sort(reverse=True)
    rank = result.index(k_score)
    return GRADE[rank // (N // 10)]


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
