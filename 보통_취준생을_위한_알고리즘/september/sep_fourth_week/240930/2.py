def solution(cap, n, deliveries, pickups):
    total_distance = 0
    delivery_stack = [[i+1, deliveries[i]] for i in range(n) if deliveries[i] > 0]
    pickup_stack = [[i+1, pickups[i]] for i in range(n) if pickups[i] > 0]
    
    def calculate_max_distacne(stack):
        total_boxes = 0
        max_distance = 0
        while stack:
            house, box = stack.pop()
            if house > max_distance:
                max_distance = house
            
            if total_boxes + box > cap:
                remain_box = total_boxes + box - cap
                stack.append([house, remain_box])
                
                return max_distance
        
        total_boxes += box
        return total_boxes
    
    while delivery_stack or pickup_stack:
        max_deliver_stack = calculate_max_distacne(delivery_stack)
        max_pickup_distance = calculate_max_distacne(pickup_stack)
        total_distance += max(max_deliver_stack, max_pickup_distance) * 2

    return total_distance
