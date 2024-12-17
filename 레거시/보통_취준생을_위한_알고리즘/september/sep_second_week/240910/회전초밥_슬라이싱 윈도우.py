from collections import defaultdict

n, d, k, c = map(int,input().split())
arr = [int(input()) for _ in range(n)]

arr += arr[:k-1]

window = defaultdict(int)
window[c] += 1

left, right = 0, 0
while right < k:
    window[arr[right]] += 1
    right += 1

max_sushi = len(window)

for _ in range(n):
    max_sushi = max(max_sushi, len(window))

    window[arr[right]] += 1
    window[arr[left]] -= 1

    if window[arr[left]] == 0:
        del window[arr[left]]
    
    right += 1
    left += 1

print(max_sushi)