def move_direction(first_list, direction_positive, direction_negative):
    positive = []
    negative = []
    
    # 방향에 따라 리스트 분류
    for i in range(1, n+1):
        if first_list[i-1][1][0] > i:
            positive.append(i)
        elif first_list[i-1][1][0] < i:
            negative.append(i)
    
    # 양의 방향 (오름차순)
    for pos in positive:
        for j in range(pos, first_list[pos-1][1][0]):
            result.append((first_list[pos-1][0], direction_positive))
    
    # 음의 방향 (내림차순)
    negative = sorted(negative, reverse=True)
    for neg in negative:
        for j in range(first_list[neg-1][1][0], neg):
            result.append((first_list[neg-1][0], direction_negative))

if __name__ == '__main__':
    n = int(input())
    r_first = []
    c_first = []
    result = []
    
    # 입력받아 r_first, c_first 리스트에 저장
    for i in range(1, n+1):
        r, c = map(int, input().split())
        r_first.append((i, (r, c)))
        c_first.append((i, (c, r)))
    
    # r_first, c_first를 각 방향 기준으로 정렬
    r_first.sort(key=lambda x: x[1])
    c_first.sort(key=lambda x: x[1])
    
    # 상하 이동과 좌우 이동을 처리
    move_direction(r_first, 'U', 'D')
    move_direction(c_first, 'L', 'R')
    
    # 결과 출력
    print(len(result))
    for res in result:
        print(res[0], res[1], sep=' ')
