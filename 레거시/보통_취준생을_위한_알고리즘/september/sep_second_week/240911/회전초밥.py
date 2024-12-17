#방법3. 백준 15961번 슬라이딩 윈도우 기법
from collections import defaultdict
n,d,k,c = map(int, input().split())
arr = [ int(input()) for _ in range(n)]
arr = arr + arr[:k-1] 
max_sushi = 0
left , right = 0, 0
window = defaultdict(int)
window[c] +=1

while right < k:  #처음 k개로 초기값 만들기 
    window[arr[right]] +=1
    right+=1

for _ in range(n-1):
    max_sushi = max(max_sushi, len(window))    
    window[arr[right]] +=1
    window[arr[left]] -=1
    if window[arr[left]==0]: window.pop(arr[left])
    right+=1
    left+=1
print(max_sushi)