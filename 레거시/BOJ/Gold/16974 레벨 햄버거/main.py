'''
Docstring for BOJ.Gold.16974 레벨 햄버거.main
버거는 패티만
L은 번, L-1버거, 패티 L-1 버거,번
번 패티 패티 패티 번
번 번 패티패티패티 번 패티 번 패티 번 패티패티패티번 번

'''

N, X = map(int, input().split())
total_size = [0] * (N+1)
patty_cnt = [0] * (N+1)


