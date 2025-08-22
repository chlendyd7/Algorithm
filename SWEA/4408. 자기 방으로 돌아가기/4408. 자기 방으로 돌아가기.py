'''
    🚩 시간복잡도에 대한 오해

    너가 걱정했던 “visited 다 찍고 공통되면 체크 → 시간복잡도 높음” 부분을 뜯어보자.

    내 최종 풀이(복도 배열 마킹)는 이렇게 돼:

    학생 수 = N (최대 200)

    복도 길이 = 200

    각 학생이 차지하는 구간 [a, b] 를 corridor 배열에 +1 한다.

    이 연산은 O(N*200) = 40,000 → 충분히 빠름.

    즉, 사실상 시간복잡도 걱정할 필요 없는 문제였던 거야.

'''
def solution():
    N = int(input()) # 학생 수
    students = []
    for _ in range(N):
        a, b = map(int, input().split())
        students.append((a,b) if a < b else (b,a))
    students.sort()
    cnt = 1

    for i in range(len(students)-1):
        a1, b1 = students[i]
        for j in range(i+1, len(students)):
            a2, b2 = students[j]
            if a1 <= a2 <= b1:
                cnt += 1
                break

            if b1 < a2:
                break
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')

