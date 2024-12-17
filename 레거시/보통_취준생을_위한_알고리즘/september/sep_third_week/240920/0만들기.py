def dfs(idx, rst):
    if idx == N:
        answer = eval(rst.replace(' ', ''))
        if answer == 0:
            ans_lst.append(rst)
        return
    else:
        n_idx = idx + 1
        dfs(n_idx, rst + ' ' + str(n_idx))
        dfs(n_idx, rst+'+'+str(n_idx))
        dfs(n_idx, rst+'-'+str(n_idx))


T = int(input())
for _ in range(T):
    N = int(input())
    ans_lst = []
    dfs(1, '1')
    for a in ans_lst:
        print(a)
    print()
