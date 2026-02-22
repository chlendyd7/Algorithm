from bisect import bisect_left, bisect_right
from collections import defaultdict


def solution(words, queries):
    word_dict = defaultdict(list)
    reversed_word_dict = defaultdict(list)
    
    for word in words:
        length = len(word)
        word_dict[length].append(word)
        reversed_word_dict[length].append(word[::-1])
    
    for length in word_dict:
        word_dict[length].sort()
        reversed_word_dict[length].sort()
    
    def count_by_range(word_list, left, right):
        return bisect_right(word_list, right) - bisect_left(word_list, left)

    result = []
    for query in queries:
        length = len(query)
        if length not in word_dict:
            result.append(0)
            continue
    
        if query[0] == '?':
            query = query[::-1]
        left = query.replace('?', 'a')
        right = query.replace('?', 'z')
        result.append(count_by_range(word_dict[length], left, right))
    
    return result