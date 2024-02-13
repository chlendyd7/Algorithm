def solution(numbers):
    # 숫자를 문자열로 변환하고 정렬 기준을 설정하여 정렬
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    
    # 0으로만 구성된 경우 예외 처리
    return str(int(''.join(numbers)))
'''
    문자열 비교연산의 경우엔 첫번째 인덱스인 666[0]인 6과 101010[0]인 1과 222[0]인 2를 ascii숫자로 바꿔서 비교합니다. 
    물론 같으면, 다음 인덱스도 비교합니다. 비교한 결과 [6, 2, 10]의 순으로 정렬됩니다.
'''