from collections import Counter


def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)

    common_counts = {d: min(counter_x[d], counter_y[d]) for d in counter_x if d in counter_y}
    result = ''.join(sorted(
        (d * common_counts[d] for d in common_counts),
        reverse=True
    ))

    if not result:
        return "-1"
    if result == '0' * len(result):
        return "0"
    
    return result
