# 문제 url: https://www.acmicpc.net/problem/21460
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상

def find_bridge(num, i, j): # num: 섬의 번호 
    global min_bridge
    q = deque()
    q.append((i, j))
    visit[i][j] = 1
    while q:
        row, column = q.popleft()
        for di, dj in delta:
            ni = row + di
            nj = column + dj
            # 범위 체크, 같은 섬이 아닌지, 방문했던 좌표 인지 확인한다.
            if 0 <= ni < N and 0 <= nj < N and island[ni][nj] != num and not visit[ni][nj]:
                # 같은 섬이 아닌데 숫자가 있으면 다른 섬이다.
                if island[ni][nj]:
                    if min_bridge > visit[row][column] - 1:
                        min_bridge = visit[row][column] - 1
                    return
                # 바다 일때 (0일때)
                else:
                    q.append((ni, nj))
                    visit[ni][nj] = visit[row][column] + 1


def bfs(i, j):
    q = deque()
    q.append((i, j))
    island[i][j] = cnt # 섬!
    while q:
        row, column = q.popleft()
        for di, dj in delta:
            ni = row + di
            nj = column + dj
            # 범위체크, 섬인지, 방문했던 좌표인지 확인
            if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] and not island[ni][nj]:
                q.append((ni, nj))   # 나랑 연결된 섬!
                island[ni][nj] = cnt # 나랑 연결된 섬!

N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]

# 연결 된 섬을 지도에 표시한다. 
island = [[0]*N for _ in range(N)] # 섬 지도
cnt = 0  # 섬의 개수
for i in range(N):
    for j in range(N):
        if arr[i][j] and not island[i][j]:
            cnt += 1
            bfs(i, j)

# 다른 섬까지 bfs!
min_bridge = 0xffffff
for i in range(N):
    for j in range(N):
        if island[i][j]:
            visit = [[0]*N for _ in range(N)]
            num = island[i][j]
            find_bridge(num, i, j)

print(min_bridge)