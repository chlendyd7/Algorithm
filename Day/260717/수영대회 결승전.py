# https://swexpertacademy.com/main/code/userProblem/userProblemDetail.do?contestProbId=AWKaG6_6AGQDFARV
'''
    섬은 1, 소용돌이 2
    소용돌이는 새ㅑㅇ성되고 22초 유지되다 1초동안 잠잠
    한번 통과한 소용돌이 위에서 머물러 있을 수 있다

    시작점, 도착점

    2<=N<=15 15여서 완탐
    
    현재 위치, 시간(%3으로 소용돌이 유무 파악)
    visited로 체크

'''
from collections import deque


def solution():
    return 0