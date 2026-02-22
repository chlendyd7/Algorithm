from collections import Counter
import re

def solution(s):
    # 1. 숫자 추출
    numbers = re.findall(r'\d+', s)  # 숫자만 추출
    print(numbers)
    numbers = list(map(int, numbers))  # 문자열을 정수로 변환
    
    # 2. 빈도 계산
    freq_dict = Counter(numbers)  # 숫자의 빈도를 계산
    
    # 3. 빈도 정렬
    # 빈도가 높은 순서대로 키를 정렬하여 리스트로 변환
    answer = [key for key, _ in freq_dict.most_common()]
    
    return answer
