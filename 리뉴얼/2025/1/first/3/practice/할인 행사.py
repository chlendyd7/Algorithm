from collections import Counter


def solution(want, number, discount):
    want_dict = {
        want[i] : number[i]
        for i in range(len(number))
    }

    answer = 0
    for i in range(len(discount) - 9):
        current_window = discount[i:i+10]
        current_count = Counter(current_window)

        if all(current_count[product] >= want_dict[product] for product in want_dict):
            answer += 1

    return answer