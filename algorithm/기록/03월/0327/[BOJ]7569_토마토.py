# 문제 url: https://www.acmicpc.net/problem/7569

from collections import deque

def check(array, h, row, column):
    global day
    for i in range(h):
        for j in range(row):
            for k in range(column):
                if array[i][j][k] > day:
                    day = array[i][j][k]
                if array[i][j][k] == 0: # 익지 않은 토마토가 있으면 -1을 리턴한다.
                    return -1
    return day-1                        # 첫 토마토는 제외해야 한다.


M, N, H = map(int, input().split()) # M: 가로, N: 세로, H: 높이
delta= [(0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1), (-1, 0, 0), (1, 0, 0)]
q = deque()  # 탐색을 위한 q
day = 0     # 마지막으로 토마토가 익는 날짜를 위한 변수

# 3차원 배열(?)을 생성하여 기록한다. arr[height][row][column]
arr = []
for i in range(H):
    array = [list(map(int, input().split()))for _ in range(N)]
    arr.append(array)

# 익은 토마토 찾기 (탐색 시작점)
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append((i, j, k)) # q에 추가한다.

# 탐색!
while q:
    vh, vi, vj = q.popleft()
    for dh, di, dj in delta:
        nh = vh + dh
        ni = vi + di
        nj = vj + dj
        if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M and arr[nh][ni][nj]==0:
            arr[nh][ni][nj] = arr[vh][vi][vj]+1 # 익었다! (토마토가 익는 시간을 기록하기 위해, 지난번 토마토가 익은 시간 +1로 기록한다.)
            q.append((nh,ni,nj))                # 익었다!

print(check(arr, H, N, M))
