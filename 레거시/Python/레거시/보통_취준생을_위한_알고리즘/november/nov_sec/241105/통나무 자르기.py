import sys
input = sys.stdin.readline

l, k, c = map(int, input().split())
position = sorted(list(set([0, *list(map(int, input().split())), l])))
# 나무토막들
print(position)
pieces = [position[i] - position[i-1] for i in range(1, len(position))]
print(pieces)
start = 1
end = l

while start <= end:
    mid = (start + end) // 2
	# 애초에 자를 수 없으면 크기를 키움
    if max(pieces) > mid:
        start = mid + 1
    else:
        total = 0
        cnt = 0
        # 토막들의 뒤부터 확인
        for p in pieces[::-1]:
            total += p
            if total > mid:
                total = p
                cnt += 1
        if cnt > c:
            start = mid + 1
        else:
        	# 적절한 크기
            ans_result = mid
            # 최대횟수를 모두 사용하면 total,
            # 그렇지 않다면 맨 앞토막의 끝
            ans_front = total if cnt == c else pieces[0]
            end = mid - 1

print(ans_result, ans_front)
