from collections import deque

n, m = map(int, input().split())
king = input()

graph = dict()
indegree = dict()
family = dict()
all_people = set()
all_people.add(king)

for _ in range(n):
    child, p1, p2 = input().split(' ')
    all_people.update([child, p1, p2])
    
    for p in [p1, p2]:
        if p not in graph: graph[p] = []
        graph[p].append(child)
    family[child] = [p1,p2]
    indegree[child] = indegree.get(child, 0) + 2

scores = {name: 0.0 for name in all_people}
scores[king] = 1.0

queue = deque()
for person in all_people:
    if person not in indegree:
        queue.append(person)

while queue:
    curr = queue.popleft()
    
    if curr in graph:
        for child in graph[curr]:
            indegree[child] -= 1
            if indegree[child] == 0:
                p1, p2 = family[child]
                scores[child] = (scores[p1] + scores[p2]) / 2.0
                queue.append(child)

best_candidate = ""
max_bllod_score = -1.0

for _ in range(m):
    candidate = input()
    current_score = scores.get(candidate, 0.0)
    if current_score > max_bllod_score:
        max_bllod_score = current_score
        best_candidate = candidate
print(best_candidate)
