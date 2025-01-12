def solution(n, k, cmd):
    stack = []
    row = [True] * (n+1)
    cursor = 0
    for c in cmd:
        if c[0] == 'U':
            steps = int(c.split()[1])
            while steps > 0:
                cursor += 1
                if row[cursor]:
                    steps -= 1
            for i in range(cnt):
                if row[cursor]
                cursor -= cnt
        elif c[0] == 'D':
            cnt = c[2]
            cursor += cnt
            
        
    answer = ''
    return answer