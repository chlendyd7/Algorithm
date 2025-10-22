def rcp(a, b, lst):
    ca, cb = lst[a], lst[b]
    if ca == cb:
        return a
    elif (ca == 1 and cb == 3) or (ca == 2 and cb == 1) or (ca == 3 and cb == 2):
        return a
    else:
        return b

def dfs(left, right, lst):
    if left == right:
        return left

    mid = (left + right) // 2
    left = dfs(left, mid, lst)
    right = dfs(mid + 1, right, lst)
    
    result = rcp(left, right, lst)
    return result


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    winner = dfs(0, N-1, cards)
    print(f'#{t} {winner + 1}')
