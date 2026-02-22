from collections import Counter
import re


def solution(s):
    numbers = re.findall(r'\d+', s)
    numbers = list(map(int, numbers))

    freq_dict = Counter(numbers)

    return [key for key, _ in freq_dict.most_common()]
