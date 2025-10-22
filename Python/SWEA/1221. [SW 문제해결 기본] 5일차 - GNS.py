def solution():
    _ = input()
    WORD_LIST = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    words = list(input().split())
    cnt_lst = [0] * 10

    for word in words:
        cnt_lst[WORD_LIST.index(word)] += 1
    
    result = []
    for i in range(10):
        result.extend((WORD_LIST[i] + ' ') * cnt_lst[i])
    return ''.join(result)




T = int(input())
for t in range(1, T+1):
    print(f'#{t}')
    print(solution())
