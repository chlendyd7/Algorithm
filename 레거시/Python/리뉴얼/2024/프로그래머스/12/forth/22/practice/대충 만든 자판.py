from collections import defaultdict


def solution(keymap, targets):
    answer = []
    MAX_INT = 101
    dic = defaultdict(lambda: MAX_INT)

    for kk in keymap:
        for i in range(len(kk)):
            dic[kk[i]] = min(dic[kk[i]], i + 1)

    for target in targets:
        cnt = 0
        for t in target:
            if t in dic:
                cnt += dic[t]
            else:
                cnt = - 1
                break
        answer.append(cnt)
    return answer

keymap = ["ABACD", "BCEFD"]
targets = ["ABCD","AABB"]
solution(keymap, targets)