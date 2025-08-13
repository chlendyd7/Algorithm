'''
    NxN 크기 도시 빈칸 치킨집 집
    치킨거리 = 집과 가장 가까운 치킨집 사이의 거리
    치킨 거리는 모든 집의 치킨 거리의 합
    |r1 - rc| + |c1 - c2|

    M개만 고르고 나머지 폐업
    어떻게 고르면 도시의 치킨 거리가 가장 적게 될지 구하기


'''

N,M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
chick_house = []
houses = []
result = 1e9

for i in range(N):
    for j in range(N):
        if lst[i][j] == 1:
            houses.append((i,j))
        elif lst[i][j] == 2:
            chick_house.append((i,j))

def find_chicken_dis(selected):
    global result
    mn = 0
    for h_r, h_c in houses:
        house_min = 1e9
        for c_r, c_c in selected:
            house_min = min(house_min, abs(h_r - c_r) + abs(h_c - c_c))
        mn += house_min
    result = min(result, mn)

def dfs(start, selected):
    if len(selected) == M:
        find_chicken_dis(selected)
        return

    for i in range(start, len(chick_house)):
        selected.append(chick_house[i])
        dfs(i + 1, selected)
        selected.pop()

dfs(0, [])
print(result)
