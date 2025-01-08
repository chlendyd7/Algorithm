def solution(n, k, cmd):
    stack = []
    cursor = k
    can_work = [True] * n
    for c in cmd:
        if c[0] == 'U':
            cnt = int(c.split()[1])
            temp = 0
            while temp < cnt:
                cursor -= 1
                if can_work[cursor]:
                    temp += 1

        elif c[0] == 'D':
            cnt = int(c.split()[1])
            temp = 0
            while temp < cnt:
                cursor += 1
                if can_work[cursor]:
                    temp += 1

        elif c[0] == 'C':
            stack.append(cursor)
            can_work[cursor] = False
            if cursor == n-1:
                cursor -= 1
            else:
                cursor += 1

        elif c[0] == 'Z':
            
            can_work[stack.pop()] = True

    return ''.join('O' if x else 'X' for x in can_work)