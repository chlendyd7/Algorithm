import sys, math
from heapq import heappush, heappop

input = sys.stdin.readline

def main():
	answer = 0
	N = int(input().rstrip())
	A = [int(i) for i in input().rstrip().split()]
	B = [int(i) for i in input().rstrip().split()]
	table = [(A[i], B[i]) for i in range(N)]
	table = sorted(table, key=lambda x: (x[1], x[0]))
	print(table)
	prev = -1
	max_A_value = -1
	for i in range(N):
		a, b = table[i]
		if prev > a:
			time = math.ceil((prev - a) / 30)
			a = a + 30 * time
			answer = answer + time
		if b > a:
			time = math.ceil((b - a) / 30)
			a = a + 30 * time
			answer = answer + time
			print(time, i)
		max_A_value = max(max_A_value, a)
		if i + 1 < N and b != table[i + 1][1]:
			prev = max_A_value
    
	return answer
"""
5
24 2 3 29 2
25 35 30 30 30
"""
print(main())