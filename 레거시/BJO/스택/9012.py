#괄호
import sys; input = sys.stdin.readline

def is_stack(s:str) -> str: #리턴 값
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return "NO"
    return "YES" if not stack else "NO"

T = int(input())
for _ in range(T):
    s = input().rstrip()
    print(is_stack(s))
