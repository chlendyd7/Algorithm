from copy import deepcopy

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

def rotate(x, y, lst, rt) :
    length = len(lst)
    for k in range(5) :
        ax, ay = x + dx[k], y + dy[k]
        if -1 < ax < length and -1 < ay < length :
            lst[ay][ax] = ( lst[ay][ax] + rt ) % 4

def solution(clockHands):
    answer = float('inf')
    length = len(clockHands)
    
    for i in range(4 ** length) :
        tmp = 0
        tmp_clock = deepcopy(clockHands)
        for j in range(length) :
            rt = i % 4 ** ( j + 1 ) // 4 ** j
            if rt == 0 :
# 출처: https://magentino.tistory.com/55 [마젠티노's:티스토리]
