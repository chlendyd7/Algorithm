n = int(input())  # 동전의 종류 개수
coins = list(map(int, input().split()))  # 동전의 종류
m = int(input())  # 거슬러 줄 금액

# dp[i] : i원을 거슬러주는데 필요한 최소 동전 개수
dp = [10001] * (m + 1)  # 최대 동전 개수는 500원을 1원짜리로 500번 거슬러줘야 하므로 500 * 100 + 1 = 10001로 초기화
dp[0] = 0  # 0원 거슬러줄 때는 동전을 사용할 필요가 없으므로 0으로 초기화

for coin in coins:  # 모든 동전에 대해 반복
    for j in range(coin, m + 1):  # 동전의 가치부터 m원까지 반복
        dp[j] = min(dp[j], dp[j - coin] + 1)  # 현재 j원에 대해 동전을 사용하는 경우와 사용하지 않는 경우 중 작은 값을 선택

print(dp[m])  # m원을 거슬러주는데 필요한 최소 동전 개수 출력


# # import sys
# sys.stdin = open("input.txt", 'r')    
# if __name__=="__main__":
#     n=int(input())
#     coin=list(map(int, input().split()))
#     m=int(input())
#     dy=[1000]*(m+1);
#     dy[0]=0
#     for i in range(n):
#         for j in range(coin[i], m+1):
#             dy[j]=min(dy[j], dy[j-coin[i]]+1)
#     print(dy[m])