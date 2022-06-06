# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13_BWKACUCFAYh&categoryId=AV13_BWKACUCFAYh&categoryType=CODE&problemTitle=1209

for t in range(10):
    T = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    max_v = 0            # 최댓값을 저장하는 변수

    # 열의 합 (행 우선 순회)
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[i][j]
        if max_v < total:
            max_v = total

    # 행의 합 (열 우선 순회)
    for j in range(100):
        total = 0
        for i in range(100):
            total += arr[i][j]
        if max_v < total:
            max_v = total

    # 좌측상단에서 시작하는 대각선의 합
    # 행과 열이 같은 원소의 합
    total = 0
    for i in range(100):
        total += arr[i][i]
    if max_v < total:
        max_v = total

    # 우측상단에서 시작하는 대각선의 합
    # 시작지점에서부터 i는 +1, j는 -1
    total = 0
    i = 0                 # 시작지점: arr[0][99]
    j = 99
    while i <= 99:        # 도착지점: arr[99][0]
        total += arr[i][j]
        i += 1            # 이동!
        j -= 1            # 이동!
    if max_v < total:
        max_v = total

    print(f'#{T} {max_v}')


