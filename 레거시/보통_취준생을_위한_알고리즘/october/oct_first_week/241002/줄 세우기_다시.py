def lis(sequence):
    dp = []

    for num in sequence:
        if not dp or dp[-1] < num:
            dp.append(num)
        else:
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            dp[left] = num
    
    return len(dp)

n = int(input())
student = [int(input()) for _ in range(n)]

longest_length = lis(student)
min_move = n - longest_length

print(min_move)
