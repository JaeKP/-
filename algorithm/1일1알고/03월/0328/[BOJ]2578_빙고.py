# 문제 url: https://www.acmicpc.net/problem/2578

def call_num():
    global cnt
    for i in range(5):
        for j in range(5):
            num = number[i][j]
            cnt += 1
            row, column = map_num[num]
            check[0][row] -= 1          # column이 i인 세로 빙고 값 -=1 (0이 되면 빙고다)
            check[1][column] -= 1          # row가 j 인 가로 빙고 값 -= 1 (0이 되면 빙고다)
            # 오른쪽 하단 방향의 대각선인지 확인
            if row == column:
                check[2][0] -= 1
            # 왼쪽 상단 방향의 대각선인지 확인
            if row + column == 4:
                check[2][1] -= 1
            # 숫자를 외친 후, 빙고가 몇 개 있는지 확인한다.
            if check_line():
                return

# 빙고의 개수를 체크하는 함수
def check_line():
    bingo = 0
    for i in range(3):
        for j in range(5):
            if check[i][j] == 0:  # 0이면 빙고이다.
                bingo += 1
    if bingo >= 3:
        return 1
    else:
        return 0


arr = [list(map(int, input().split()))for _ in range(5)]
number = [list(map(int, input().split()))for _ in range(5)]
check = [[5]*5 for _ in range(5)]  # 빙고를 체크하기 위한 리스트 ([0][0]~[0][4]: 세로 빙고, [1][0]~[1][4]: 가로빙고, [2][0]~[2][1]: 대각선빙고)
map_num = [0]*26  # 숫자의 좌표를 저장하는 리스트
cnt = 0           # 사회자가 부른 숫자의 수

for i in range(5):
    for j in range(5):
        map_num[arr[i][j]] = (i, j)


call_num()
print(cnt)
