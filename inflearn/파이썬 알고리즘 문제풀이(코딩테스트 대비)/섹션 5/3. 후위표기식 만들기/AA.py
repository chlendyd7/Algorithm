a = input()
stack = []
res = ''
for x in a:
    if x.isdecimal(): # 0~9 까지의 숫자인지 판별
        res += x
    else:
        if x == '(': # (는 괄호는 stack에 바로 넣음
            stack.append(x)
        elif x == '*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res += stack.pop()
            stack.append(x)
        elif x =='+' or x=='-':
            while stack and stack[-1] != '(': # 여는 괄호 전까지만
                res += stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)        