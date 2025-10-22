string = list(input())
a_cnt = string.count('a')
string += string[0:a_cnt - 1]
min_val = float('inf')
for i in range(len(string) - (a_cnt -1)):
    min_val = min(min_val, string[i:i+a_cnt].count('b'))

print(min_val)

s = input() # 문자열 입력
a = s.count('a') # 입력된 str에서의 a의 개수

s += s[0:a-1] # 원형 문자열 처리
min_val = float('inf') # 최솟값
for i in range(len(s)-(a-1)):
    min_val = min(min_val, s[i:i+a].count('b'))
print(min_val)
