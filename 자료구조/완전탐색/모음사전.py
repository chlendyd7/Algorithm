





def solution(word):
    alp = ["A", "E", "I", "O", "U"]
    answer = 0
    multiplier = [781,156,31,6,1]
    
    for i in range(len(word)):
        answer += alp.index(word[i])*multiplier[i]
    
    return answer + len(word)

'''
"AAA"의 경우를 계산해보겠습니다.

첫 번째 문자 'A'의 가중치: vowels.index('A') * multiplier[0] → 0 * 781 = 0
두 번째 문자 'A'의 가중치: vowels.index('A') * multiplier[1] → 0 * 156 = 0
세 번째 문자 'A'의 가중치: vowels.index('A') * multiplier[2] → 0 * 31 = 0
따라서 "AAA"의 경우 answer는 0 + 0 + 0 = 0이 됩니다.
'''

'''
word가 "AAAEE"라고 가정하겠습니다.

첫 번째 문자 'A'의 가중치: vowels.index('A') * multiplier[0] → 0 * 781 = 0
두 번째 문자 'A'의 가중치: vowels.index('A') * multiplier[1] → 0 * 156 = 0
세 번째 문자 'A'의 가중치: vowels.index('A') * multiplier[2] → 0 * 31 = 0
네 번째 문자 'E'의 가중치: vowels.index('E') * multiplier[3] → 1 * 6 = 6
다섯 번째 문자 'E'의 가중치: vowels.index('E') * multiplier[4] → 1 * 1 = 1
'''

