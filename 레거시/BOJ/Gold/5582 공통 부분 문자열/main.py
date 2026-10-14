'''
Docstring for BOJ.Gold.5582 공통 부분 문자열.main

'''
words1 = list(input())
words2 = list(input())
n1, n2 = len(words1), len(words2)

dp = [[0] * (n2+1) for _ in range(n1+1)]

max_len = 0
for i in range(1, n1+1):
    for j in range(1, n2+1):
        if words1[i-1] == words2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            max_len = max(max_len, dp[i][j])
        else:
            dp[i][j] = 0

print(max_len)

