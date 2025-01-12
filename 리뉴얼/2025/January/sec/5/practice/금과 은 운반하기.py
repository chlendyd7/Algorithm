def solution(a,b,g,s,w,t):
    total_gold = sum(g)
    total_silver = sum(s)
    total_weight = sum(a) + sum(b)
    
    left, right = 0, (10**9) * (10**5) * 4
    
    while left < right:
        mid = (left + right) // 2
        gold_delivered, silver_delivered, total_delivered = 0, 0, 0
        
        for i in range(len(t)):
            round_trip_time = t[i] * 2
            trips = mid // round_trip_time
            if mid % round_trip_time >= t[i]:
                trips += 1
            
            max_gold = min(trips * w[i], g[i])
            max_silver = min(trips * w[i], s[i])
            max_total = min(trips, w[i], g[i] + s[i])
            
            gold_delivered += max_gold
            silver_delivered += max_silver
            total_delivered += max_total
            
            if gold_delivered >= total_gold and \
                silver_delivered >= total_silver and \
                total_delivered >= total_weight:
                right = mid
            else:
                left = mid + 1
    
    return left
