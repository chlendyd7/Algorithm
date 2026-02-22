def solve():
    T = int(input())
    for t in range(1, T + 1):
        N = int(input())
        scores = list(map(int, input().split()))

        possible = {0}
        for p in scores:
            new_scores = set()
            for s in possible:
                new_scores.add(s + p)
            possible |= new_scores   # 합집합

        print(f"#{t} {len(possible)}")
