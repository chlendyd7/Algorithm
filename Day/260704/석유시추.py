'''
    단 하나만 뚫을 수 있다
    가장 많은 석유량을 return 하도록 solution 함수를 완성해 주세요
    
    1을 만나면 해당 석유 크기 파악 및 y값 파악
    전체를 넣고, 이미 본 값은 pass
    
    land가 이미 있음
'''
dirs = [(1,0), (0,1), (-1,0), (0,-1)]
from collections import deque, defaultdict
def solution(land):
    def simulation(x,y):
        q = deque([(x,y)])
        len_check = 0
        now_check = [(x, y)]
        while q:
            x, y = q.popleft()

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    if (nx, ny) not in now_check and land[nx][ny] == 1:
                        len_check += 1
                        q.append((nx, ny))
                        now_check.append((nx, ny))
        all_check.update(now_check)
        lst.append(now_check)
    
    
    # 여기부터
    records = defaultdict(list)
    all_check = set()
    lst = []
    n, m = len(land), len(land[0])
    for x in range(n):
        for y in range(m):
            if land[x][y] and (x,y) not in all_check: # 석유 값이 있으면
                simulation(x,y)
    
    for c1 in lst:
        l = len(c1)
        check = set()
        for c2 in c1:
            check.add(c2[1])

        for y in check:
            records[y].append(l)
    
    mx = 0
    for record in records.values():
        now = 0
        for r in record:
            now += r
        mx = max(now, mx)

    return mx


from collections import deque, defaultdict

def solution(land):
    n, m = len(land), len(land[0])
    
    # 각 열(Column)마다 얻을 수 있는 석유량의 합을 저장
    # {열번호: 총 석유량}
    column_oil = defaultdict(int)
    
    # 이미 방문한 곳을 0으로 바꾸어 방문 처리
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                # BFS 시작
                q = deque([(i, j)])
                land[i][j] = 0
                
                size = 0
                cols = set() # 이 덩어리가 어떤 열들을 포함하는지 기록
                
                while q:
                    x, y = q.popleft()
                    size += 1
                    cols.add(y)
                    
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                            land[nx][ny] = 0
                            q.append((nx, ny))
                
                # 이 덩어리가 포함된 모든 열에 덩어리 크기를 더해줌
                for col in cols:
                    column_oil[col] += size
                    
    # 모든 열 중에서 가장 큰 값 반환
    if not column_oil:
        return 0
    return max(column_oil.values())
