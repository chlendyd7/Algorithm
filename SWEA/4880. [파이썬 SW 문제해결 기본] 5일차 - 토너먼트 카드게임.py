'''
- N 장씩 나눠가짐
- 전체 그룹을 두 그룹으로 나눔
- 그룹의 승자끼리 카들르 비교해서 이긴 사람이 최종 승자
- 그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눔
'''
def rsp(a, b, cards):
    ca, cb = cards[a], cards[b]
    if ca == cb:
        return a
    elif (ca == 1 and cb == 3) or (ca == 2 and cb == 1) or (ca == 3 and cb == 2):
        return a
    else:
        return b

def tournament(start, end, cards):
    if start == end:
        return start
    mid = (start + end) // 2
    left = tournament(start, mid, cards)
    right = tournament(mid + 1, end, cards)
    return rsp(left, right, cards)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    cards = list(map(int, input().split()))
    winner = tournament(0, N-1, cards)
    print(f'#{t} {winner + 1}')
