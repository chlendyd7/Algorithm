import os
import sys


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 현재 실행 중인 파일의 절대 경로
sys.stdin = open(os.path.join(BASE_DIR, 'input.txt'), 'r')


def solution():
    return


T = int(input())
for t in range(1, T+1):
    print(f'#{t} {solution()}')