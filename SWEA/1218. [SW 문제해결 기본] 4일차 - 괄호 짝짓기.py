def solution():
    _ = int(input())
    lst = list(input())
    stack = []
    for l in lst:
        if l == ')':
            if stack[-1] == '(':
                stack.pop()
            else:
                return 0
        elif l == ']':
            if stack[-1] == '[':
                stack.pop()
            else:
                return 0
        elif l == '}':
            if stack[-1] == '{':
                stack.pop()
            else:
                return 0
        elif l == '>':
            if stack[-1] == '<':
                stack.pop()
            else:
                return 0
        else:
            stack.append(l)

    return 1


for t in range(1, 11):
    print(f'#{t} {solution()}')
    

def solution():
    _ = input()
    s = input().strip()

    pairs = {')':'(', ']':'[', '}':'{', '>':'<'}
    stack = []

    for ch in s:
        if ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return 0
            stack.pop()
        else:
            stack.append(ch)
    
    return int(not stack)
