N = int(input())
R = 10**N
dp = [0] * R
for i in range(1, R):
    num = str(i)
    check = True
    for j in range(1, i//10):
        if abs(int(num[j-1]) - int(num[j])) != 1 or abs(int(num[j]) - int(num[j+1])) != 1:
                check=False
                break
    if check:
        dp[i] = dp[i-1]+1
    else:
        dp[i] = dp[i-1]

print(dp[R-1])

