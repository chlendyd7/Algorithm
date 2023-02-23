https://fre2-dom.tistory.com/309
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = str(sys.stdin.readline())

cnt = 0
i = 0
flag =0
# 시간 복잡도 : O(M) => I0I 단위로 최대 m번씩 탐색
while i < m - 1:
    # 현재 문자열이 IOI 일 경우
    if s[i - 1] == "I" and s[i] == "O" and s[i + 1] == "I":
        flag += 1
        
        # IOI 문자열 개수가 n 개라면  
        if flag == n: 
            flag -= 1 # 문자열 개수 -1
            cnt += 1 # 카운트
            
        i += 2 # 현재 문자열이 IOI 이기 때문에 다다음 문자부터 확인하기 위해 i + 2를 해준다.  
        continue
    
    i += 1 # 현재 문자열이 IOI 가 아니라면 다음 문자부터 확인 
    flag = 0 # IOI 문자열 개수는 0으로 초기화
    
print(cnt)

import sys

# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# s = str(sys.stdin.readline())

# p = "IOI"
# for _ in range(1, n):
#     p += "OI"

# cnt = 0

# # 시간 복잡도 : O(NM) => n개를 m번씩 탐색
# for i in range(m):
#     if s[i:len(p) + i] == p:
#         cnt += 1

# print(cnt)