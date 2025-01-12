def solution(n, k, cmd):
    stack = []  # 삭제된 행을 기록
    cursor = k  # 현재 커서 위치
    can_work = [True] * n  # 각 행의 상태 (True: 존재, False: 삭제)
    table = {i: [i - 1, i + 1] for i in range(n)}  # 각 행의 이전, 다음 행을 기록

    for c in cmd:
        if c[0] == 'U':
            cnt = int(c.split(' ')[1])
            while cnt > 0:
                cursor = table[cursor][0]  # 이전 행으로 이동
                cnt -= 1

        elif c[0] == 'D':
            cnt = int(c.split(' ')[1])
            while cnt > 0:
                cursor = table[cursor][1]  # 다음 행으로 이동
                cnt -= 1

        elif c[0] == 'C':
            stack.append((cursor, table[cursor]))  # 현재 행과 연결 정보를 기록
            can_work[cursor] = False  # 삭제 처리

            # 이전과 다음 행을 연결
            prev, next = table[cursor]
            if prev != -1:
                table[prev][1] = next
            if next != n:
                table[next][0] = prev

            # 커서 이동
            cursor = next if next != n else prev

        elif c[0] == 'Z':
            restored, (prev, next) = stack.pop()  # 복구할 행과 연결 정보
            can_work[restored] = True  # 복구 처리

            # 이전과 다음 행 복구
            if prev != -1:
                table[prev][1] = restored
            if next != n:
                table[next][0] = restored

    return ''.join('O' if x else 'X' for x in can_work)
