T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max = [0, 0, 0]                                             # row, column, 최댓값을 할당할 변수
    for i in range(N):
        for j in range(N):
            total = 0                                          # 순회를 시작할 때마다 리셋
            row = i
            column = j
            for ni, nj in [(0, 1), (-1, 0), (0, -1), (1, 0)]:  # 이웃원소의 인덱스
                if 0 <= (i + ni) < N and 0 <= (j + nj) < N:    # 이웃 원소의 인덱스 범위를 제한
                    total += arr[i+ni][j+nj]
            if max[2] < total:                                 # 기존의 max 값 보다 크면
                max[2] = total                                 # 최댓값 교체
                max[0] = row                                   # row  교체
                max[1] = column                                # colume 교체

    print(f'#{t} {max[0]} {max[1]} {max[2]}')
