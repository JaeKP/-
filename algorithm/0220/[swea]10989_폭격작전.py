# 문제 정보: SolvingClub _2차 배열

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    bomb = [0] * M
    total = 0                                                 # 피해입는 적군의 총수

    for i in range(M):
        bomb[i] = list(map(int, input().split()))
        for j in range(bomb[i][2] + 1):                       # bomb[i][2] = 폭탄의 범위
            for r, c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:   # 델타 (폭탄이 터지는 십자 방향)

                # bomb[i][0]: 폭탄의 열  bomb[i][1]: 폭탄의 행
                if 0 <=(bomb[i][0]) + (r*j) < N and 0 <= (bomb[i][1]) + (c*j) < N :    # 폭탄의 범위는 2차 배열 범위 안에 있어야 함.
                    total += arr[(bomb[i][0]) + (r*j)][(bomb[i][1]) + (c*j)]           # 폭탄의 범위에 있는 적군의 수를 total에 추가
                    arr[(bomb[i][0]) + (r*j)][(bomb[i][1]) + (c*j)] = 0                # 중복 집계를 막기 위해 0으로 초기화

    print(f'#{t} {total}')