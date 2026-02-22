# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=4&contestProbId=AWngfZVa9XwDFAQU&categoryId=AWngfZVa9XwDFAQU&categoryType=CODE&problemTitle=&orderBy=INQUERY_COUNT&selectCodeLang=ALL&select-1=4&pageSize=10&pageIndex=2

'''
    1. 해당 로직은 무한 루프에 빠짐
    if people in check_set:
        continue

    그래프문제
    사는 사람의 수 N
    알고있는 사람의 관계 수 M
    그래프 문제
'''
def solution():
    N, M = map(int, input().split())
    adj_matrix = [[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        node1, node2 = map(int, input().split())
        adj_matrix[node1][node2] = 1
        adj_matrix[node2][node1] = 1

    check_set = set()
    cnt = 0
    people = 1
    while len(check_set) != N:
        #아래의 if문 무한 루프에 빠짐
        if people in check_set: 
            continue
        check_set.add(people)
        
        #인접 노드들도 탐색해줘야 하는데 그러지 않고 1-step만 보고 멈춤
        for i in range(1, N+1):
            if adj_matrix[people][i]:
                check_set.add(i)

        people += 1
        cnt += 1
    return cnt


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')
