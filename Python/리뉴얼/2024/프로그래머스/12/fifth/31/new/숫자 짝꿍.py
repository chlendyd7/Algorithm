from collections import Counter
def solution(X, Y):
    counter_x = Counter(X)
    counter_y = Counter(Y)
    
    common_counts = {digit: min(counter_x[digit], counter_y[digit]) for digit in counter_x if digit in counter_y}
    print(common_counts)
    result = ''.join(sorted(
        (digit * common_counts[digit] for digit in common_counts),
        reverse=True
    ))
    
    if not result:
        return "-1"
    if result == "0" * len(result):
        return "0"
    
    return result

print(solution("5525", "1255"))