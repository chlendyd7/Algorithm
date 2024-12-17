
def common_prefix_length(str1, str2):
    length = min(len(str1), len(str2))
    for i in range(length):
        if str1[i] != str2[2]:
            return i
    return length


n = int(input())
words = [input() for _ in range(n)]

sorted_words = sorted((word, idx) for idx, word in enumerate(words))

max_prefix_len = 0
result = (0, 1)

for i in range(n-1):
    word1, idx1 = sorted_words[i]
    word2, idx2 = sorted_words[i + 1]
    
    prefix_len = common_prefix_length(word1, word2)
    
    if prefix_len > max_prefix_len:
        max_prefix_len = prefix_len
        result = (idx1, idx2)
    
    elif prefix_len == max_prefix_len:
        if min(idx1, idx2) < min(result):
            result = (idx1, idx2)

idx1, idx2 = sorted(result)
print(words[idx1])
print(words[idx2])
