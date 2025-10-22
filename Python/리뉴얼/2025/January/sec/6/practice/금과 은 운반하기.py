def solution(a, b, g, s, w, t):

    answer = (10**9) * (10**5) * 4
    left, right = 0, (10**9) * (10**5) * 4
    while left <= right:
        mid = (left + right) // 2
        gold, silver, total = 0, 0, 0

        for i in range(len(t)):
            now_gold, now_silver, now_weight, now_time = g[i], s[i], w[i], t[i]
            move_cnt = mid // (now_time * 2)

            if mid % (now_time * 2) >= now_time:
                move_cnt += 1
            
            gold += now_gold if (now_gold < move_cnt * now_weight) else move_cnt * now_weight
            silver += now_silver if (now_silver < move_cnt * now_weight) else move_cnt * now_weight
            total += now_gold + now_silver if (now_gold + now_silver < move_cnt * now_weight) else move_cnt * now_weight
        
        if gold >= a and silver >= b and total >= a + b:
            right = mid - 1
            answer = min(answer, mid)
        else:
            left = mid + 1
            


    return answer