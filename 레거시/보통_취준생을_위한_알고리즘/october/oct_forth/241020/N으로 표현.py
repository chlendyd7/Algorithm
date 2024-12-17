def solution(n, number):
    # DP 배열 초기화
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(n) * i))
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a//b)
    
    for i in range(1,9):
        if number in dp[i]:
            return i
    return -1

n = 5
number = 12
print(solution(n, number))  # 출력: 4
