def solution(a, b, cards):
    ca, cb = cards[a], cards[b]
    if ca == cb:
        return a
    elif(ca == 1 and cb == 3) or (ca == 2 and cb == 1) or (ca == 3 and cb == 2):
        return a
    else:
        return b

def tournament(start, end, cards):
    if start == end:
        return start
    mid = (start + end) // 2
    left = tournament(start, mid, cards)
    right = tournament(mid + 1, end, cards)
    return solution(left, right, cards)

T = int(input())
for t in range(1, T+1):
    n = int(input())
