def can_measure(beads, weights):
    possible = set([0])
    
    for weight in weights:
        new_possible = set()
        for p in possible:
            new_possible.add(p + weight)
            new_possible.add(abs(p - weight))
        possible.update(new_possible)

    results = []
    for bead in beads:
        if bead in possible:
            results.append('Y')
        else:
            results.append('N')
    return results



num_weight = int(input())
weights = list(map(int,input().split()))
num_bead = int(input())
beads = list(map(int, input().split()))

result = can_measure(beads, weights)
print(' '.join(result))
