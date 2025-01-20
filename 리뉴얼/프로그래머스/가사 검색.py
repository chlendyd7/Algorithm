from bisect import bisect_left, bisect_right

def solution(words, queries):
    # 단어를 길이별로 저장
    word_dict = {}
    reversed_word_dict = {}

    for word in words:
        length = len(word)
        if length not in word_dict:
            word_dict[length] = []
            reversed_word_dict[length] = []
        word_dict[length].append(word)
        reversed_word_dict[length].append(word[::-1])

    # 각 길이별 리스트 정렬
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

        if query[0] != "?":  # 접두사 검색
            left = query.replace("?", "a")
            right = query.replace("?", "z")
            result.append(count_by_range(word_dict[length], left, right))
        else:  # 접미사 검색
            reversed_query = query[::-1]
            left = reversed_query.replace("?", "a")
            right = reversed_query.replace("?", "z")
            result.append(count_by_range(reversed_word_dict[length], left, right))

    return result
