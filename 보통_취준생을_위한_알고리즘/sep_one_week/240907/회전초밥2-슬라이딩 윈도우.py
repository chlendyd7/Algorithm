from collections import defaultdict

n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

arr += arr[:k-1]

window = defaultdict(int)
window[c] += 1

left, right = 0, 0
while right < k:
    window[arr[right]] += 1
    right += 1

max_sushi = len(window)

# 슬라이딩 윈도우로 초밥 종류 계산
for _ in range(n):
    max_sushi = max(max_sushi, len(window))  # 최대 가짓수 갱신
    
    # 윈도우 오른쪽에 새 초밥 추가
    window[arr[right]] += 1
    
    # 윈도우 왼쪽에서 초밥 제거
    window[arr[left]] -= 1
    if window[arr[left]] == 0:  # 초밥 가짓수가 0이 되면 제거
        del window[arr[left]]
    
    right += 1
    left += 1

# 결과 출력
print(max_sushi)
