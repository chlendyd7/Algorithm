T = int(input())

def hex_char_to_int(ch):
    if '0' <= ch <= '9':
        return ord(ch) - ord('0')
    else:
        return ord(ch) - ord('A') + 10

def to_4bit_bin(num):
    bits = []
    for i in [8,4,2,1]:
        bit = num // i
        bits.append(str(bit))
        num = num % i
    return ''.join(bits)

for tc in range(1, T+1):
    N, hex_str = input().split()
    result = ''
    for ch in hex_str:
        num = hex_char_to_int(ch)
        result += to_4bit_bin(num)
    print(f'#{tc} {result}')
