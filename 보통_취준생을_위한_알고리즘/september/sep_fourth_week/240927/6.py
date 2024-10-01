def solution(n, m, x, y, r, c, k):
    answer = ''
    dist = abs(x-r) + abs(y-c)
    k -= dist
    if k<0 or k%2 != 0:
        return "impossible"
    
    direction = {'d':0, 'l':0, 'r':0, 'u':0}
    if x > r:
        direction['u'] += x-r
    else:
        direction['d'] += r-x
    if y > c:
        direction['l'] += y-c
    else:
        direction['r'] += c-y
    
    answer += 'd'*direction['d']
    d = min(int(k/2), n-(x+direction['d']))
    answer += 'd'*d
    direction['u'] += d
    k -= 2
