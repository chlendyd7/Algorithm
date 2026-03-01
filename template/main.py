import sys
import os

# 로컬에서 테스트할 때만 주석 해제
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.stdin = open(os.path.join(current_dir, 'input.txt'), 'r')
sys.stdout = open(os.path.join(current_dir, 'output.txt'), 'w')

input = sys.stdin.readline
