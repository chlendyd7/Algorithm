'''
# 1. 완전탐색
B를 C보다 작을 때 까지 하나씩 먹자
A를 B보다 작을 때까지 하나씩 먹자
시간 복잡도: 3000가지 x 3000 x 3

# 2. 규칙을 세우자

'''
import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(T+1):
    A,B,C = map(int, input().split())
    