'''
- 메모리 초기화
- 해당 값이 메모리 끝까지 덮어씌어짐
- 원래 상태로 돌아가는데 최소 몇번이나 고쳐야 하는지 계산
- 그리디인가?
- 완탐?

'''

def solution():
    check = False
    bits = list(map(int, input()))
    cnt = 0
    for b in bits:
        if b != check:
            cnt += 1
            check = not check

    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')