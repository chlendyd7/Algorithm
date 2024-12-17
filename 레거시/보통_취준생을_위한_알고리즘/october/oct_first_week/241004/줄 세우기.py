def solution(childs):
    dp = []
    for c in childs:
        if not dp or dp[-1] < c:
            dp.append(c)
        else:
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < c:
                    left = mid + 1
                else:
                    right = mid - 1
            dp[left] = c
    return len(dp)




n = int(input())
childs = [int(input()) for _ in range(n)]
answer = 0
print(n - solution(childs))