def solution(k, room_number):
    parent = {}
    
    def find(x):
        if x not in parent:
            parent[x] = x + 1
            return x
        parent[x] = find(parent[x])
    
    answer = []
    for room in room_number:
        next_room = find(room)
        answer.append(next_room)
    return answer