s = list(input())

zero_to_remove = s.count('0') // 2
one_to_remove = s.count('1') // 2

# 앞에서부터 '1' 제거 (사전순으로 앞서기 위해 큰 숫자인 1을 앞에서 제거)
count = 0
for i in range(len(s)):
    if s[i] == '1':
        s[i] = '' # 삭제 표시
        count += 1
    if count == one_to_remove:
        break

# 뒤에서부터 '0' 제거 (작은 숫자인 0을 뒤에서 제거하여 앞쪽에 남김)
count = 0
for i in range(len(s) - 1, -1, -1):
    if s[i] == '0':
        s[i] = '' # 삭제 표시
        count += 1
    if count == zero_to_remove:
        break

print(''.join(s))