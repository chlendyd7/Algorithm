def check(stack):
    tmp = []
    for st in stack:
        if st == '(':
            tmp.append('(')
        if st == ')':
            if tmp: tmp.pop()
            else: return False
    return True

g_cnt = 0 # g
a_cnt = 0 # (
b_cnt = 0 # )

n = int(input())
inputs = input()
n_len = len(inputs)
for str in inputs:
    if str == 'G':
        g_cnt+=1
    elif str == '(':
        a_cnt+= 1
    else:
        b_cnt += 1


tmp_stack = []
cnt = 0
for st in inputs:
    g_locatin = []
    if st == 'G':
        if cnt < (n_len // 2) - a_cnt:
            tmp_stack.append('(')
            cnt += 1
        else:
            tmp_stack.append(')')
    else:
        tmp_stack.append(st)

if check(tmp_stack):
    print(''.join(tmp_stack))

    

