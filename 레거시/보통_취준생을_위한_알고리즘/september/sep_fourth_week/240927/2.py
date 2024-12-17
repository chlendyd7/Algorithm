def solution(cap, n, deliveries, pickups):
    total_distance = 0
    delivery_stack = [[i+1, deliveries[i]] for i in range(n) if deliveries[i] > 0]
    pickup_stack = [[i+1, pickups[i]] for i in range(n) if pickups[i] > 0]

    def calculate_max_distance(stack):
        total_boxes = 0
        max_distance = 0

        while stack:
            house, boxes = stack.pop()
            if house > max_distance:
                max_distance = house
            
            if total_boxes + boxes > cap:
                remaining_boxes = total_boxes + boxes - cap
                stack.append([house, remaining_boxes])
                return max_distance

        return max_distance
    
    while delivery_stack or pickup_stack:
        max_delivery_distance = calculate_max_distance(delivery_stack)
        max_pickup_distacne = calculate_max_distance(pickup_stack)
        total_distance += max(max_delivery_distance, max_pickup_distacne) * 2
    
    return total_distance
