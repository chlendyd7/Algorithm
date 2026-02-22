def solution(storey):
    result = 0
    
    while storey > 0:
        num = storey % 10  # 1의 자리 수 추출
        next_digit = (storey // 10) % 10  # 다음 자리 수 추출

        if num > 5 or (num == 5 and next_digit >= 5):
            # 5보다 크거나, 5와 같으면서 다음 자리수가 5 이상일 때
            result += 10 - num
            storey = (storey + 10 - num) // 10
        else:
            # 5보다 작거나, 5와 같으면서 다음 자리수가 5 미만일 때
            result += num
            storey //= 10
    
    return result
