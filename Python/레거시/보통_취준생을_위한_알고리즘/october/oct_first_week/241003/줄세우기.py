n = int(input())
childs = [int(input()) for _ in range(n)]


dp = []
for i in range(n):
    if not dp or dp[-1] < childs[i]:
        dp.append(childs[i])
    else:
        left, right = 0, len(dp) - 1
        while left <= right:
            mid = (left + right) // 2
            if dp[mid] < childs[i]:
                left = mid + 1
            else:
                right = mid - 1
        dp[left] = childs[childs[i]]
