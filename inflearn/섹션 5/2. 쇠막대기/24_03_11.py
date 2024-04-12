'''
    ▣ 입력예제 1
    ()(((()())(())()))(())
    ▣ 출력예제 1
    17
'''

s=input()
stack=[]
cnt=0
for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')':
        stack.pop()
        if s[i-1] == '(':
            cnt += len(stack)
        else:
            cnt+=1

print(cnt)