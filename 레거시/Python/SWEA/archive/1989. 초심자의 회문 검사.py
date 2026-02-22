def solution(word):
    length = len(word)
    for i in range(length//2):
        if not word[i] == word[length - i - 1]:
            return 0
    return 1

T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution(input())}')
