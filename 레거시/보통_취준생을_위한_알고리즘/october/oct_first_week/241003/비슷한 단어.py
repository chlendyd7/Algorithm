def check_words(word1, word2):
    length = min(len(word1), len(word2))
    for i in range(length):
        if word1[i] != word2[i]:
            return i
    return length


n = int(input())
words = [input() for _ in range(n)]

sorted_words = sorted((word, idx) for idx, word in enumerate(words))
max_length = 0
answer = (1e9, 1e9)

for i in range(n-1):
    check_length = check_words(sorted_words[i][0], sorted_words[i+1][0])
    if max_length < check_length:
        max_length = check_length
        answer = (sorted_words[i][1], sorted_words[i+1][1])
    elif max_length == check_length:
        if min(sorted_words[i][1], sorted_words[i+1][1]) < min(answer):
            answer = (sorted_words[i][1], sorted_words[i+1][1])
answer = sorted(answer)

for a in answer:
    print(words[a])
   
