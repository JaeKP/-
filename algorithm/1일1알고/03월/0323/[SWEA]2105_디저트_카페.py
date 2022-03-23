# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5VwAr6APYDFAWu
# 완전탐색으로 모든 경로를 탐색하여 정답을 도출한다.

# 직사각형 형태로 움직일 delta
# 오른쪽 대각 아래, 왼쪽 대각 아래, 왼쪽 대각 위, 오른쪽 대각 위
di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]
def tour(num, row, column, d_shop, d_length):
    global max_cnt
    if len(d_length) == 3 and d_length[0] != d_length[2]:  # 가지 치기
        return
    if num > 3:  # 종료 조건
        # 직사각형이고, cnt < max_cnt이면,
        if row == i and column == j and d_length[0] == d_length[2] and len(d_shop) > max_cnt:
            max_cnt = len(d_shop)
        return

    pass_shop = []           # 지나가는 가게 목록
    for k in range(1, N):    # 변의 길이
        ni = row + di[num]*k
        nj = column + dj[num]*k
        # 범위 체크, 가게 중복 여부를 확인 한다.
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in d_shop and arr[ni][nj] not in pass_shop:
            pass_shop.append(arr[ni][nj])
            tour(num+1, ni, nj, d_shop+pass_shop, d_length+[len(pass_shop)])
        else:
            return

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    max_cnt = -1
    length = []
    for i in range(N):
        for j in range(N):
            shop = []
            tour(0, i, j, shop, length)

    print(f'#{t} {max_cnt}')
