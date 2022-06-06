T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for n in range(N):
        s_r, s_c, e_r, e_c, color = map(int, input().split())

        # 사용자에게 입력받은 좌표를 이용하여 색칠하기
        for i in range(s_r, e_r+1):      # 세로: s_r ~ e_r
            for j in range(s_c, e_c+1):  # 가로: s_c ~ e_c
                if color == 1:           # 빨간색이면
                    arr[i][j] += 1       # 값: 1

                else:                    # 파란색이면
                    arr[i][j] += 2       # 값: 2

    cnt = 0
    for i in range(10):                  # 2차원 배열 순회
        for j in range(10):
            if arr[i][j] == 3:           # 값이 3이면 (1+2)
                cnt += 1                 # 보라색이기때문에 카운트한다.
    print(f'#{t} {cnt}')





