import sys

def common_prefix_length(word1, word2):
    length = min(len(word1), len(word2))
    for i in range(length):
        if word1[i] != word2[i]:
            return i
    return length

# 입력 받기
n = int(input())
words = [input().strip() for _ in range(n)]

# 사전 순 정렬을 위해 (단어, 인덱스) 형태로 저장
sorted_words = sorted((word, idx) for idx, word in enumerate(words))

# 접두사 최대 길이 및 해당하는 단어 인덱스 저장
max_prefix_len = 0
result = (0, 1)  # 초기 값 설정

for i in range(n - 1):
    word1, idx1 = sorted_words[i]
    word2, idx2 = sorted_words[i + 1]
    
    # 현재 단어 쌍의 접두사 길이 계산
    prefix_len = common_prefix_length(word1, word2)
    
    # 접두사가 더 길면 갱신
    if prefix_len > max_prefix_len:
        max_prefix_len = prefix_len
        result = (idx1, idx2)
    # 접두사 길이가 같을 때, 입력 순서가 더 작은 단어 쌍으로 갱신
    elif prefix_len == max_prefix_len:
        if min(idx1, idx2) < min(result):
            result = (idx1, idx2)

# 결과 출력 (입력 순서대로 출력하기 위해 인덱스 정렬)
idx1, idx2 = sorted(result)
print(words[idx1])
print(words[idx2])
