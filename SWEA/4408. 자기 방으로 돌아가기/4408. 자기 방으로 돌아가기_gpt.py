'''
    https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWNcJ2sapZMDFAV8&categoryId=AWNcJ2sapZMDFAV8&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=3
    지나는 복도의 구간이 겹치면 두 학생은 동시에 들어갈 수 없다.
    이동하는데 거리에 관계없이 단위 시간이 걸림
    최소 몇 단위만에 모든 학생들이 들어 갈 수 있나요?

    중복 없음
    현재 방번호 돌아가야 할 방번호
    
    아이디어
    1. visited를 통해 해당 부분 check 공통되면 + 1
        시간 복잡도: 높음
    2. a1 <= a2 < b1:
        최대 복잡도를 놓침

'''
def solution():
    N = int(input())
    corridor = [0] * 201   # 복도 구간 (1~200)

    for _ in range(N):
        a, b = map(int, input().split())
        # 구간 매핑 (1,2 -> 1 / 3,4 -> 2 / ...)
        a = (a + 1) // 2
        b = (b + 1) // 2
        if a > b:
            a, b = b, a
        for i in range(a, b+1):
            corridor[i] += 1

    return max(corridor)


T = int(input())
for t in range(1, T+1):
    print(f"#{t} {solution()}")
