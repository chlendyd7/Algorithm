def solution(board, moves):
    stack = []  # 바구니 역할을 하는 스택
    answer = 0  # 터진 인형의 개수

    for move in moves:
        column = move - 1  # moves는 1-based 인덱스이므로 0-based로 변환
        for i in range(len(board)):
            if board[i][column] != 0:  # 해당 열에서 가장 위의 인형 찾기
                stack.append(board[i][column])  # 바구니에 인형 추가
                board[i][column] = 0  # 인형을 뽑았으므로 비워줌
                break  # 다음 move로 이동

        # 스택의 마지막 두 개가 같다면 터뜨리기
        while len(stack) >= 2 and stack[-1] == stack[-2]:
            stack.pop()  # 마지막 아이템 제거
            stack.pop()  # 마지막에서 두 번째 아이템 제거
            answer += 2  # 터진 인형 개수 추가

    return answer

# 테스트
print(solution([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
