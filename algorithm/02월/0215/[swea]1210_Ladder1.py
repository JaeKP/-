for t in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 도착 좌표 찾기
    end_r = 99
    end_c = 0
    for j in range(100):
        if arr[end_r][j] == 2:  # 값이 2인 곳이 도착해야할 좌표이다.
            end_c = j

    # 반복문으로 상, 좌, 우를 확인하고 이동한다. (-1,0), (0, 1), (0, -1)
    while end_r > 0:                                       # row가 0이면 중지(출발지점)
        for i, j in [(0, 1), (0, -1), (-1, 0)]:
            if 0 <= end_r+i < 100 and 0 <= end_c+j < 100:  # 2차원 배열을 벗어나는 것을 방지
                if arr[end_r+i][end_c+j] == 1:             # 사다리가 있는지 확인
                    arr[end_r + i][end_c + j] = 0          # 사다리가 있다면 이동 후 되돌아 가는 것을 방지 하기 위해 값을 0으로 변경
                    end_r += i                             # 이동!
                    end_c += j                             # 이동!

    print(f'#{T} {end_c}')
