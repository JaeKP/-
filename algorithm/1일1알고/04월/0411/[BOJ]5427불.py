# 문제 url: https://www.acmicpc.net/problem/5427
from collections import deque

# 불이 퍼진다.
def break_out_fire():
    new_fire = []
    while fire:
        i, j = fire.pop()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < H and 0 <= nj < W and building[ni][nj] == '.':
                new_fire.append((ni, nj))
                building[ni][nj] = '*'
    fire.extend(new_fire)

# 상근이가 주변을 탐색하여 이동한다.
def bfs(r, c):
    cnt = 0
    q = deque()
    q.append((r, c))
    visit[r][c] = 1
    while q:
        row, column = q.popleft()

        # 탈출 조건
        if not row or not column or row == H-1 or column == W-1:
            return visit[row][column]

        # 탐색하는 depth가 깊어질 때, 불이 퍼진다.
        if visit[row][column] > cnt:
            break_out_fire()
            cnt += 1

        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = row + di
            nj = column + dj
            # 범위, 빈 공간, 방문 여부를 확인한다.
            if 0 <= ni < H and 0 <= nj < W and not visit[ni][nj] and building[ni][nj] == '.':
                visit[ni][nj] = visit[row][column] + 1  # 이동 거리(depth)를 기록한다.
                q.append((ni, nj))                      # 이동!

    return "IMPOSSIBLE"

T = int(input())
for t in range(T):
    W, H = map(int, input().split()) # W: 너비 . H: 높이
    building = [list(input())for _ in range(H)]

    # 방문여부를 확인할 수 있는 리스트
    visit = [[0]*W for _ in range(H)]

    # 불의 좌표를 기록
    fire = []

    # 시작 좌표를 기록
    start = 0
    for i in range(H):
        for j in range(W):
            if building[i][j] == '*':  # 불
                fire.append((i, j))
            elif building[i][j] == '@': # 시작 좌표
                start = (i, j)

    print(bfs(start[0], start[1]))