import sys

# 재귀 한도 늘리기 (병합 정렬은 재귀 깊이가 깊어질 수 있음)
sys.setrecursionlimit(10**6)

def merge_sort(start, end):
    global swap_count
    
    # 원소가 하나면 리턴
    if start == end:
        return [arr[start]]
    
    mid = (start + end) // 2
    # 왼쪽과 오른쪽을 각각 정렬
    left_part = merge_sort(start, mid)
    right_part = merge_sort(mid + 1, end)
    
    merged = []
    l, r = 0, 0
    
    # 두 그룹을 합치면서 swap 횟수 카운트
    while l < len(left_part) and r < len(right_part):
        if left_part[l] <= right_part[r]:
            merged.append(left_part[l])
            l += 1
        else:
            # 오른쪽 그룹의 원소가 왼쪽보다 작아서 먼저 들어가는 경우!
            # 왼쪽 그룹에 남아있는 모든 원소의 개수만큼 swap이 발생한 것과 같음
            merged.append(right_part[r])
            swap_count += (len(left_part) - l)
            r += 1
            
    # 남은 원소들 처리
    merged.extend(left_part[l:])
    merged.extend(right_part[r:])
    
    return merged

def solve():
    global arr, swap_count
    input = sys.stdin.readline
    
    try:
        n_str = input().strip()
        if not n_str: return
        n = int(n_str)
        arr = list(map(int, input().split()))
    except EOFError:
        return
        
    swap_count = 0
    merge_sort(0, n - 1)
    print(swap_count)

solve()