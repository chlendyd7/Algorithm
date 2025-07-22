'''
- N의 배수 번호인 양의 세기로 함
- 모든 숫자를 보는 것은 몇 번 양을 센 시점?
- 
'''

def solution():
    N = int(input())
    num_set = set()
    i = 1
    while True:
        num = N * i
        num_set.update(str(num))
        if len(num_set) == 10:
            return num
        i += 1


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
