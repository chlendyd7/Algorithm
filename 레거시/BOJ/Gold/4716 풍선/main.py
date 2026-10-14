import pprint
import sys
import os
file_path = os.path.join(os.path.dirname(__file__), 'input.txt')

# 파일이 존재하는지 확인 후 stdin을 교체합니다.
if os.path.exists(file_path):
    sys.stdin = open(file_path, 'r')
else:
    print("경고: input.txt 파일을 찾을 수 없습니다.")

'''
    풍선은 A B에 보관 참가한 팀의 수 N 앉아있는 자리 다름
    각 팀 풍선의 수 방 A, B 거리 주어짐
    모든 풍선을 달아주는데 필요한 이동거리 최솟값
    1 <= N <=1000
    0 <= A, B <= 10000
    팀에게 달아줘야 하는 풍선의 수 K, Da, Db
    N, A, B 보관 되있는 풍선의 수

    단순 그리디 정렬 시 => 10, 10의 경우에서 논리 x
    차이 정렬은? a, b
    
    15, 35
    10 20 10  10, -10  => 5 cnt += 50, cnt += 1 
    10 10 30  -20, 20 => 10 .. 5    cnt += 100
    10 40 10  30, -30   => cnt += 100
'''

def solve():
    while True:
        line = sys.stdin.readline().split()
        if not line or line == ['0', '0', '0']:
            break

        N, A, B = map(int, line)
        teams = []
        for _ in range(N):
            K, Da, Db = map(int, sys.stdin.readline().split())
            teams.append([abs(Da-Db), K, Da, Db])
        
        teams.sort(key=lambda x: x[0], reverse=True)
        ans = 0
        for diff, K, Da, Db in teams:
            if Da <= Db:
                take_A = min(K, A)
                ans += take_A * Da
                A -= take_A
                K -= take_A

                if K > 0:
                    ans += K * Db
                    B -= K
            else:
                take_B = min(K, B)
                ans += take_B * Db
                B -= take_B
                K -= take_B

                if K > 0:
                    ans += K * Da
                    A -= K
        print(ans)
solve()
