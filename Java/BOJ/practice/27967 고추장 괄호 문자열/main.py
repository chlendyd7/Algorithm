n = int(input())
inputs = input()
stack = []
result = []

for str in inputs:
    if str=='G':
        if not stack or stack[-1]==')':
            stack.append('(')
        elif stack[-1] == '(':
            stack.append(')')
    
    while stack and stack[-1] == ')':
        stack.pop()
        stack.pop()
        