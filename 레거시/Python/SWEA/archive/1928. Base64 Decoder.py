'''
1. 표1을 보고 입력받은 문자들을 각각 대응하는 숫자로 변경한다.
2. 각 숫자들을 6자리 이진수로 표현하고, 이 이진수들을 한 줄로 쭉 이어 붙인다.
3. 한 줄로 쭉 이어붙인 이진수들을 8자리씩 끊어서 십진수로 바꾼다.
4. 각각의 십진수를 아스키 코드로 변환한다.
'''

base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def solution():
    string = input()
    binary_str = ""
    for c in string:
        binary_str += format(base64_table.index(c), '06b')
    chunks = [binary_str[i: i+8] for i in range(0, len(binary_str), 8)]
    decimal_list = [int(chunk, 2) for chunk in chunks]
    
    result = ""
    for c in decimal_list:
        result += chr(c)
    
    return result
    
T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')