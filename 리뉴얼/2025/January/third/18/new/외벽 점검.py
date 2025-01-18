def solution(n, weak, dist):

    W, F = len(weak), len(dist)
    repair_lst = [()]
    count = 0
    dist.sort(reverse=True)

    for can_move in dist:
        repairs = []
        count += 1

        for i, wp in enumerate(weak):
            start = wp
            ends = weak[i:] + [n+w for w in weak[:i]]
            can = [end % n for end in ends if end - start <= can_move]
            repairs.append(set(can))
        
        camd = set()
        for r in repairs:
            for x in repair_lst:
                new = r | set(x)
                if len(new) == W:
                    return count
                camd.add(tuple(new))
        repair_lst = camd
    
    return -1