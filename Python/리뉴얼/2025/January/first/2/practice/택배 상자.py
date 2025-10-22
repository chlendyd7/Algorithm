def solution(order):
    stack = []
    idx = 0
    num = 0
    
    while idx < len(order):
        if order[idx] > num:
            num += 1
            stack.append(num)
        elif order[idx] == stack[-1]:
            stack.pop()
            idx += 1
        else:
            return idx
