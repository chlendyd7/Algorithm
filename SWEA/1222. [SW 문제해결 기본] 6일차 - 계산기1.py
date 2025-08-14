def solution():
    priors = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '(': 3,
    }
    cal_stack = []
    result = ''
    for c in string:
        if c in priors:
            if cal_stack:
                if priors[cal_stack[-1]] == priors[c]:
                    result += cal_stack.pop()
            cal_stack.append(c)
        elif c == ')':
            while cal_stack[-1] != '(':
                result += cal_stack.pop()
        else:
            result += c
    if cal_stack:
        result += cal_stack.pop()
    return eval_postfix(result)

def eval_postfix(string):
    stack = []
    for token in string:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a+b)
            elif token == '-':
                stack.append(a-b)
            elif token == '*':
                stack.append(a*b)
            elif token == '/':
                stack.append(a*b)
    return stack[0]

for t in range(1, 11):
    N = int(input())
    string = input()
    print(f'#{t} {solution()}')