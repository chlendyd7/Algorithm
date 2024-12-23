def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []  # 값 저장 스택
    idx_stack = []  # 인덱스 저장 스택
    
    for i in range(len(numbers)):
        while stack and stack[-1] < numbers[i]:  # 현재 값이 스택의 마지막 값보다 크다면
            stack.pop()  # 스택에서 값을 제거
            idx = idx_stack.pop()  # 인덱스도 제거
            answer[idx] = numbers[i]  # 해당 인덱스에 현재 값을 기록
        stack.append(numbers[i])  # 현재 값을 스택에 추가
        idx_stack.append(i)  # 인덱스도 추가
    
    return answer

def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    idx_stack = []
    i = 0
    while i < len(answer):
        now = numbers[i]
        if not stack:
            stack.append(numbers[i])
            idx_stack.append(i)
        for j in len(stack):
            if stack[j] < now:
                answer[idx_stack[j]] = now
        i += 1

    return answer

# 3, 5, 9
# 4, 3, 2, 1, 0