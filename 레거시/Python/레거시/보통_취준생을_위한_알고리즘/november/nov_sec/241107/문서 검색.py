str1 = input()
str2 = input()
str1_len = len(str1)
str2_len = len(str2)
cnt = 0

i = 0
while i < str1_len:
    if  str1[i:i+str2_len] == str2:
        i += str2_len
        cnt += 1
    else:
        i+=1
print(cnt)

# import sys
# S = sys.stdin.readline().strip()
# x = sys.stdin.readline().strip()
# i = 0
# cnt = 0
# while i < len(S):
#     if S[i:i+len(x)] == x:
#         i += len(x)
#         cnt += 1
#     else :
#         i += 1
# print(cnt)
# 출처: https://edder773.tistory.com/199 [개발하는 차리의 학습 일기:티스토리]