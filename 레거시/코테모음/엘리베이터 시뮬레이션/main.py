def elevator():
    curr_floor = 1
    target_floor = 1
    direction = 0 # 정지0, 상행1, 하행-1
    requests = {10, 5, 2}

    while requests or curr_floor != target_floor:
        if curr_floor in requests:
            requests.remove(curr_floor)
            if curr_floor == target_floor and requests:
                if direction == 1:
                    target_floor = max(requests)
                elif direction == -1:
                    target_floor = min(requests)
        
        if curr_floor < target_floor:
            curr_floor += 1
            direction = 1
        elif curr_floor > target_floor:
            curr_floor -= 1
            direction -= 1
        else:
            if requests:
                up_reqs = [f for f in requests if f > curr_floor]
                if up_reqs:
                    target_floor = max(up_reqs)
                    direction = 1
                else:
                    target_floor = min(requests)
                    direction -= 1
            else:
                direction = 0
