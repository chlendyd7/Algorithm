import re


def solution(s):
    cnt_while = 0
    cnt_0 = 0
    while s != '1':
        cnt_while += 1
        num = s.count('1')
        cnt_0 += len(s) - num
    answer = [cnt_while, cnt_0]
    return answer