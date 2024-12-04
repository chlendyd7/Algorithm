import sys

def main():
    input = sys.stdin
    while True:
        # 한 줄 읽기
        line = input.readline().strip()
        if line == "0":
            break
        
        # 첫 번째 값은 n, 나머지는 heights
        values = list(map(int, line.split()))
        n = values[0]
        heights = values[1:]
        
        # 스택과 최대 넓이 변수 초기화
        stack = []
        max_area = 0
        
        for i in range(n):
            idx = i
            while stack and stack[-1][0] >= heights[i]:
                height, start_idx = stack.pop()
                max_area = max(max_area, height * (i - start_idx))
                idx = start_idx
            stack.append((heights[i], idx))
        
        # 남은 스택 처리
        while stack:
            height, start_idx = stack.pop()
            max_area = max(max_area, height * (n - start_idx))
        
        # 결과 출력
        print(max_area)

if __name__ == "__main__":
    main()
