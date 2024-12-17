def lis(sequence):
    # LIS를 저장하기 위한 리스트
    dp = []
    
    for num in sequence:
        # 현재 숫자가 dp의 마지막 원소보다 크면 추가
        if not dp or dp[-1] < num:
            dp.append(num)
        else:
            # 현재 숫자가 dp의 마지막 원소보다 작거나 같으면
            # dp에서 이진 탐색을 통해 위치를 찾고 대체
            left, right = 0, len(dp) - 1
            while left <= right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid - 1
            dp[left] = num  # dp에서 대체
    print(dp)
    return len(dp)  # 최장 증가 부분 수열의 길이 반환


# 입력 부분
N = int(input())
students = [int(input()) for _ in range(N)]

# 현재 순서의 학생들에서 LIS의 길이를 구함
longest_inc_subseq_length = lis(students)

# 최소 이동 횟수 계산
min_moves = N - longest_inc_subseq_length

# 결과 출력
print(min_moves)
