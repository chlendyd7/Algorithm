'''
1. 두 개의 숫자판을 선택, 정해진 횟수 만큼 **자리를** 교환 할 수 있음
2. 오른쪽 끝에서부터 1원 왼쪽으로 갈 수록 10배수 커짐
3. 그냥 자리 수 대로 상금 획득
4. 가장 ㅡㅋㄴ 금액
'''
# import sys
# sys.stdin = open('input.txt', 'r')
def solution():
    number, count = input().split()
    count = int(count)
    number = list(number)
    length = len(number)

    visited = set()
    max_result = 0
    
    def dfs(depth):
        nonlocal max_result
        key = (''.join(number), depth)
        if key in visited:
            return
        visited.add(key)

        if depth == count:
            max_result = max(max_result, int(''.join(number)))
            return

        for i in range(length):
            for j in range(i+1, length):
                number[i], number[j] = number[j], number[i]
                dfs(depth + 1)
                number[i], number[j] = number[j], number[i]

    dfs(0)
    return max_result
        


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
