n, k = map(int,input().split())
dp = [0] * (n+1)
def factorial(n):
    if n<=1:
        dp[n] = 1
        return dp[n]
    else:
        dp[n] = n * factorial(n-1)
        return dp[n]

print(factorial(n) // (factorial(k) * factorial(n-k)))
