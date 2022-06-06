# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV597vbqAH0DFAVl

delta = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]  # 1: 상, 2:하, 3:좌, 4: 우
opp = [0, 2, 1, 4, 3]

# 미생물을 이동시키는 함수
def move(array):
    moving = []  # 미생물이 이동할 좌표와 미생물 개수, 방향을 기록 할 변수
    for i in range(N):
        for j in range(N):
            if array[i][j] and type(array[i][j][-1]) == tuple:
                di, dj = delta[array[i][j][-1][1]]
                ni = i + di
                nj = j + dj
                n, d = array[i][j].pop(-1)  # cell에서 미생물을 제거한다.
                # 미생물이 이동할 좌표와 미생물 개수, 방향을 기록한다.
                micro = [ni, nj, n, d]
                moving.append(micro)
    # 기록한 내용을 바탕으로 미생물을 cell에 놓는다.
    locate(moving)

# 미생물을 cell에 위치시키는 함수
def locate(array):
    for row, column, num, direction in array:
        cells[row][column].append((num, direction))

# 변경사항을 실행하는 함수
def change(array):
    for i in range(N):
        for j in range(N):
            # 약품 칸에 도착했는지 확인하고 약품칸에 도착하면 미생물의 개수와 방향을 수정한다.
            if len(array[i][j]) >=2 and array[i][j][0] == 'X':
                micro_number = 0 ; micro_direction = 0
                micro_number = array[i][j][-1][0]//2
                micro_direction = opp[array[i][j][-1][1]]
                array[i][j].pop()
                array[i][j].append((micro_number, micro_direction))

            # 한 칸에 여러 미생물이 있는지 확인하고 여러 개가 있다면 미생물의 수를 합친다.
            # 미생물의 방향은 가장 수가 많은 미생물의 방향이다.
            if len(array[i][j]) >= 2 and type(array[i][j][0]) == tuple:
                number = 0; direction = 0  # number: 미생물의 개수, directrion: 미생물의 방향
                max_num = 0  # 미생물의 수를 비교하기 위한 변수
                for num, direc in array[i][j]:
                    if max_num < num: # 미생물의 수가 더 많으면
                        number += num
                        direction = direc
                        max_num = num
                    else:
                        number += num
                array[i][j].clear()
                array[i][j].append((number, direction))

# cell에 있는 미생물의 개수를 카운트하는 함수
def count(array):
    global cnt
    for i in range(N):
        for j in range(N):
            if array[i][j] and type(array[i][j][-1]) == tuple:
                cnt += array[i][j][-1][0]
    return cnt


T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())  # N은 셀의 개수, M은 격리 시간, K는 미생물 군집의 개수이다.
    arr = [list(map(int, input().split()))for _ in range(K)]

    # 초기 세팅 하기
    cells = [[['X']for _ in range(N)]] + [[['X']]+[[] for _ in range(N-2)]+[['X']] for _ in range(N-2)] + [[['X']for _ in range(N)]]
    locate(arr)

    # 실험 시작! M시간이 경과하면 종료한다.
    ttime = 0
    while ttime < M:
        move(cells)
        change(cells)
        ttime += 1

    # 남은 미생물의 수를 카운팅한다.
    cnt = 0
    print(f'#{t} {count(cells)}')
