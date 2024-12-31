def solution(cards):
    visited = [False] * len(cards)
    group_sizes = []
    
    for i in range(len(cards)):
        if not visited[i]:
            current = i
            size = 0
            while not visited[current]:
                visited[current] = True
                current = cards[current] - 1  # 다음 박스로 이동
                size += 1
            group_sizes.append(size)
    
    if len(group_sizes) < 2:
        return 0  # 두 그룹을 만들 수 없으면 0 반환
    
    group_sizes.sort(reverse=True)  # 크기 내림차순 정렬
    return group_sizes[0] * group_sizes[1]  # 가장 큰 두 그룹의 곱
