def solution(k, ranges):
    answer = []
    hail = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
    end = len(hail) - 1
    for ran in ranges:
        a = ran[0]
        b = ran[1]
        if b <= 0:
            b = end + b
        if a > b:
            answer.append(-1)
            continue
        else:
            area = 0
            for i in range(a, b):
                high = max(hail[i], hail[i+1])
                low = min(hail[i], hail[i+1])
                area += low + ((high - low) / 2)
            answer.append(area)
    return answer
