import sys
import sys
sys.stdin = open('A1_input.txt', 'r')
# 방향: 0=북, 1=동, 2=남, 3=서  (행(y)은 아래로 증가)
DY = [-1, 0, 1, 0]
DX = [0, 1, 0, -1]

def turns_to_reach(N, sx, sy, sd, tx, ty):
    """
    현재 (sx, sy), 방향 sd에서 (tx, ty)까지
    '전진으로 맨해튼 거리가 줄면 전진, 아니면 오른쪽 회전 후 전진' 그리디로
    필요한 회전 횟수를 센다. (칸당 최대 1회 회전 규칙 자동 만족)
    반환: (회전횟수, 도착 방향)
    """
    x, y, d = sx, sy, sd
    turns = 0

    # 안전장치(무한루프 방지): 최악에도 충분히 큰 스텝 상한
    step_cap = N * N * 20

    steps = 0
    while not (x == tx and y == ty):
        steps += 1
        if steps > step_cap:
            # 이 문제 제약 하에서 여기 오면 안 됨
            # 혹시라도 입력이 이상하면 예외로 끊는다.
            raise RuntimeError("Step cap exceeded; check input/logic")

        # 다음 칸
        nx, ny = x + DX[d], y + DY[d]

        # 현재 타겟까지 맨해튼 거리
        cur_dist = abs(tx - x) + abs(ty - y)

        # 1) 앞으로 나가도 되는지(격자 안) + 2) 전진 시 거리가 줄어드는지
        if 0 <= nx < N and 0 <= ny < N:
            after_dist = abs(tx - nx) + abs(ty - ny)
            if after_dist < cur_dist:
                # 전진
                x, y = nx, ny
                continue

        # 전진이 불가능(범위 밖) 하거나, 전진해도 거리가 줄지 않으면
        # 이 칸에서 '오른쪽으로' 한 번 회전하고 반드시 전진
        d = (d + 1) % 4
        turns += 1

        # 회전 후 전진 (제자리 2회전 금지 규칙 반영)
        nx, ny = x + DX[d], y + DY[d]
        # 문제 제약(사과가 테두리에 안 옴) 상 일반적으로 범위를 벗어나지 않지만,
        # 혹시 모를 상황에서도 안전하게 범위 체크.
        if 0 <= nx < N and 0 <= ny < N:
            x, y = nx, ny
        else:
            # 만약 여기서도 못 나가면 다음 루프에서 또 회전하게 됨
            # (한 칸당 1회 회전 규칙은 지킴: 이번 칸에선 회전 1번만 수행 후 이동 시도)
            pass

    return turns, d


def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    for tc in range(1, T + 1):
        N = int(input().strip())
        grid = [list(map(int, input().split())) for _ in range(N)]

        # 사과 좌표 수집: 값>0, 번호 순으로 정렬
        apples = []
        for r in range(N):
            for c in range(N):
                if grid[r][c] > 0:
                    apples.append((grid[r][c], r, c))  # (번호, y, x)
        apples.sort()

        # 시작: (0,0)에서 오른쪽으로 전진 상태 (문제 서술)
        x, y, d = 0, 0, 1  # 1=동
        total_turns = 0

        for _, ay, ax in apples:
            turns, d = turns_to_reach(N, x, y, d, ax, ay)
            total_turns += turns
            x, y = ax, ay  # 사과 위치로 이동 완료

        print(f"#{tc} {total_turns}")


if __name__ == "__main__":
    # 로컬 테스트 시 주석 해제
    # sys.stdin = open("A1_input.txt", "r")
    solve()
