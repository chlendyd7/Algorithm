import itertools
from collections import deque

def calcul(after_operation, op):
    b = after_operation.pop()
    a = after_operation.pop()
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b

def solution(expression: str):
    stk = []
    answer_list = []
    # 모든 우선순위를 조사
    for rank in itertools.permutations(["*", "+", "-"], 3):
        num = ""

        after_operation = []

        que = deque(expression)

        while len(que) != 0:
            s = que.popleft()
            # 숫자라면 num에 추가 하고 다음 문자 확인
            if s not in rank:
                num += s
                continue

            # 연산자라면 숫자로 만들어주고 후위 에 넣어준다.
            after_operation.append(int(num))
            num = ""

            # stk 이 비어 있지 않고 지금 나온게 더 낮거나 같다면
            while len(stk) != 0 and rank.index(stk[-1]) <= rank.index(s):
                after_operation.append(calcul(after_operation, stk.pop()))

            # stk 이 비어 있거나
            # 우선 순위가 지금 나온게 더 높다면 그냥 넣어준다.
            stk.append(s)

        # 마지막 숫자 넣기
        after_operation.append(int(num))

        # 모든 연산 하기
        while len(stk) != 0:
            after_operation.append(calcul(after_operation, stk.pop()))

        # 최종 결과의 절댓값을 answer_list에 넣기    
        answer_list.append(abs(after_operation[0]))

    # 모든값을 정렬후  
    answer_list.sort()
    # 최댓값을 return
    return answer_list[-1]