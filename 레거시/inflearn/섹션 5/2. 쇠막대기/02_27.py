# cnt = 0
# pip = 0
# n = input()
# ls = []
# for i in range(len(n)):
#     if n[i] == '(':
#         pip+=1
#     if n[i] == ')':
#         if n[i-1] == '(':
#             pip-=1
#             cnt += pip
#         else:
#             cnt+=1
#             pip-=1
# print(cnt)

# stack[]으로 구현해보기
cnt = 0
pip = []
n = input()
for i in range(len(n)):
    if n[i] == '(':
        pip.append(n[i])
    else:
        pip.pop()
        if n[i-1] == ')':
            cnt +=1
        else:
            cnt += len(pip)

print(cnt)