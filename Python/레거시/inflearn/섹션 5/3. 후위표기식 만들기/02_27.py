# 첫 번째 생각 숫자면 stack에 바로 넣는다 (이면 바로 넣는다)
# 그다음 순서대로 넣는다
m = input()
stack = []
res = ''

for x in m:
    if x.isdecimal():
        res += x
    else:
        if x=='(':
            stack.append(x)
        elif x == '*' or x=='/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack:
    res += stack.pop()
print(res)