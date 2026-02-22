'''
    문자열의 순서를 유지해야 하니까
    앞에 있는게 빠지면 안됨, 즉 deque로 앞에 있는 것 위주로
    해당 idx를 체크하면서 가장 빠른걸
    근데 이게 개별 deque가 아닌데 어떻게 하지 popleft()를 해야하는데
'''

n = int(input())
lst = [list(input()) for _ in range(n)]
answer = []
while lst:
    min_char = 'a'
    check_idx = 0
    for i in range(len(lst)):  # 현재 `lst`의 길이만큼 반복합니다.
        if lst[i] and lst[i][0] <= min_char:
            min_char = lst[i][0]
            check_idx = i
    
    answer.append(lst[check_idx].pop(0))  # `check_idx` 리스트의 첫 번째 문자 제거 및 저장
    if not lst[check_idx]:  # 해당 리스트가 비어 있으면
        lst.pop(check_idx)  # `lst`에서 해당 리스트를 제거합니다.

print(''.join(answer))
