delta = [0, (-1, 0), (1, 0), (0, -1), (0, 1)]  # 1: 상, 2:하, 3:좌, 4: 우
opp = [0, 2, 1, 4, 3]
def move(array):
    for i in range(len(array)):
        di, dj = delta[array[i][3]]
        ni = array[i][0] + di
        nj = array[i][1] + dj
        array[i][0] = ni
        array[i][1] = nj

def sort_check(array):
    array.sort(key = lambda x: (x[0], x[1], x[2]), reverse=True)  # 좌표, 미생물의 수에 따라 내림차순 정렬한다. 
    cnt = 0
    while cnt < len(array):
        row = array[cnt][0]; column = array[cnt][1]; num = array[cnt][2]; direction = array[cnt][3]
        # 약품 칸에 도착했는지 확인하고 약품칸에 도착하면 미생물의 개수와 방향을 수정한다.
        if row == N-1 or row == 0 or column == N-1 or column == 0:
            array[cnt][2] = num // 2
            array[cnt][3] = opp[direction]
            cnt += 1
            continue
        # 같은 좌표에 다른 미생물이 있는지 확인하고 미생물의 수를 합친다.
        if cnt >= 1 and array[cnt-1][0] == row and array[cnt-1][1] == column:
            array[cnt-1][2] += num
            array.pop(cnt)
        else:
            cnt += 1

def counting(array):
    global c
    for micro in array:
        c += micro[2]
    return c

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())  # N은 셀의 개수, M은 격리 시간, K는 미생물 군집의 개수이다.
    arr = [list(map(int, input().split())) for _ in range(K)]

    # 실험 시작! M시간이 경과하면 종료한다.
    ttime = 0
    while ttime < M:
        move(arr)
        sort_check(arr)
        ttime += 1

    # 남은 미생물의 수를 카운팅한다.
    c = 0
    print(f'#{t} {counting(arr)}')