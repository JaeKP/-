# 문제 정보: SolvingClub _2차 배열

T = int(input())

for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]
    start = [0] * M                    # 정사각형의 영역에 대한 데이터를 저장할 리스트
    total = 0                          # 영역의 총합을 위한 변수

    for i in range(M):
        start[i] = list(map(int, input().split()))
        row = start[i][0]              # 행
        column = start[i][1]           # 열
        side = start[i][2]             # 변의 길이

        # 행우선 순회
        for r in range(row, row+side):
            for c in range(column, column+side):
                if  0 <= r < N and 0 <= c < N:   # 조건 1) 2차원 배열 범위 안에 있어야 함.
                    total += arr[r][c]           # 영역의 값을 총합에 더함.
                    arr[r][c] = 0                # 중복 집계를 방지하기 위해 값을 초기화

    print(f'#{t} {total}')

