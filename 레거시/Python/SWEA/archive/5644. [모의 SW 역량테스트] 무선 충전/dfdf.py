import sys
sys.stdin = open('input.txt', 'r')

DX = [0, -1, 0, 1, 0]
DY = [0, 0, 1, 0, -1]

def get_reachable_bcs(x, y, bc_list):
    reachable = []
    for idx, (bc_x, bc_y, coverage, power) in enumerate(bc_list):
        if abs(x - bc_y) + abs(y - bc_x) <= coverage:
            reachable.append((idx, power))
    return reachable

def calc_max_charge(a_bcs, b_bcs, bc_list):
    """
    A와 B가 선택할 수 있는 BC 리스트를 받아
    최대 충전량을 계산한다.
    """
    max_charge = 0
    # -1은 "선택 안함"을 의미
    a_choices = [-1] + [idx for idx, _ in a_bcs]
    b_choices = [-1] + [idx for idx, _ in b_bcs]

    for a_idx in a_choices:
        for b_idx in b_choices:
            if a_idx == -1 and b_idx == -1:
                charge = 0
            elif a_idx == b_idx and a_idx != -1:
                # 같은 BC 공유 → 절반씩 분배
                charge = bc_list[a_idx][3]
            else:
                charge = 0
                if a_idx != -1:
                    charge += bc_list[a_idx][3]
                if b_idx != -1:
                    charge += bc_list[b_idx][3]
            max_charge = max(max_charge, charge)
    return max_charge

def solve():
    T = int(input())
    for tc in range(1, T + 1):
        # 입력 처리
        M, A = map(int, input().split())
        moves_a = [0] + list(map(int, input().split()))  # A의 이동 경로 (0초 포함)
        moves_b = [0] + list(map(int, input().split()))  # B의 이동 경로 (0초 포함)

        bc_list = [tuple(map(int, input().split())) for _ in range(A)]

        # 초기 위치
        pos_a = [1, 1]
        pos_b = [10, 10]

        total_charge = 0

        # 매 초마다 이동 후 충전 계산
        for step in range(M + 1):
            # 1. A, B 이동
            pos_a[0] += DX[moves_a[step]]
            pos_a[1] += DY[moves_a[step]]
            pos_b[0] += DX[moves_b[step]]
            pos_b[1] += DY[moves_b[step]]

            # 2. 현재 위치에서 접속 가능한 BC 리스트
            a_bcs = get_reachable_bcs(pos_a[0], pos_a[1], bc_list)
            b_bcs = get_reachable_bcs(pos_b[0], pos_b[1], bc_list)

            # 3. 가능한 모든 조합 탐색 후 최대 충전량
            total_charge += calc_max_charge(a_bcs, b_bcs, bc_list)

        print(f'#{tc} {total_charge}')

# 실행
if __name__ == "__main__":
    solve()
