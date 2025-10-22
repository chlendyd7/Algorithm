import sys
sys.setrecursionlimit(100000)

def solution(k, room_number):
    room = [False] * (k + 1)
    answer = []
    for num in room_number:
        if not room[num]:
            answer.append(num)
            room[num] = True
        else:
            for i in range(num + 1, k+1):
                if not room[i]:
                    answer.append(i)
                    room[i] = True
                    break
    return answer

def solution(k, room_number):
    parent = {}

    def find(x):
        # 부모를 찾아가며 다음 빈 방을 업데이트
        if x not in parent:
            parent[x] = x + 1
            return x
        parent[x] = find(parent[x])
        return parent[x]

    answer = []
    for room in room_number:
        next_room = find(room)
        answer.append(next_room)
    return answer
