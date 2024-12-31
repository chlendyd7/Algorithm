def solution(ingredient):
    hambugi = [1,2,3,1]
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == hambugi:
            answer += 1
            for _ in range(4):
                stack.pop()
    return answer