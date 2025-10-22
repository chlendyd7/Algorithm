from collections import defaultdict
def solution(n, k, cmd):
    row = [True] * n
    stack = []
    cursor = k
    
    for c in cmd:
        if c[0] == 'D':
            steps = int(c.split()[1])
            while steps > 0:
                cursor += 1
                if row[cursor]:
                    steps -= 1
        elif c[0] == 'U':
            steps = int(c.split()[1])
            while steps > 0:
                cursor -= 1
                if row[cursor]:
                    steps -= 1
        elif c[0] == 'C':
            row[cursor] = False
            stack.append(cursor)
            if cursor == n-1:
                cursor -= 1
            else:
                cursor += 1
        elif c[0] == 'Z':
            last_del = stack.pop()
            row[last_del] = True
    return ''.join('O' if x else 'X' for x in row)
        if len(c)>1:
            command, idx = c.split(' ')
            idx = int(idx)
            if command == 'D':
                tmp = 0
                while tmp < idx:
                    if row[cursor+1]:
                        cursor += 1
                        tmp += 1
                    else:
                        cursor += 1
            else:
                tmp = 0
                while tmp < idx:
                    if row[cursor-1]:
                        cursor -= 1
                        tmp += 1
                    else:
                        cursor -= 1
        else:
            if c == 'C':
                row[cursor] = False
                last_del = cursor
                cursor += 1 if cursor != n else n-1
            else:
                row[last_del] = True
    answer =[]
    for i in row:
        if i:
            answer.append('O')
        else:
            answer.append('X')
    
    return ''.join(answer)

print(solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]))