# 문제 url: https://www.acmicpc.net/problem/10026

from collections import deque
delta= [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우하좌상

# 적록색약인 사람이 탐색할 경우
def bfs_rg(q, visit):
    while q:
        vi, vj = q.popleft()
        for di, dj in delta:
            ni = vi + di
            nj = vj + dj
            if 0<= ni < N and 0<= nj < N and visit[ni][nj] == 0:
                if (arr[vi][vj] == 'R' or arr[vi][vj] == 'G') and (arr[ni][nj] == 'R' or arr[ni][nj] == 'G'):
                    visit[ni][nj] = 1
                    q.append((ni, nj))
                elif arr[vi][vj] == arr[ni][nj]:
                    visit[ni][nj] = 1
                    q.append((ni, nj))

# 적록색약이 아닌 사람이 탐색할 경우
def bfs_rgb(q, visit):
    while q:
        vi, vj = q.popleft()
        for di, dj in delta:
            ni = vi + di
            nj = vj + dj
            if 0<= ni < N and 0<= nj < N and arr[vi][vj] == arr[ni][nj] and visit[ni][nj] == 0:
                visit[ni][nj] = 1
                q.append((ni, nj))

def check(function):
    global cnt
    visit = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            q = deque()
            if visit[i][j] == 0:
                visit[i][j] = 1
                q.append((i, j))
                function(q, visit)
                cnt += 1
    return cnt

#=============================
N = int(input())
arr = [list(input())for _ in range(N)]

cnt = 0
cnt_rgb = check(bfs_rgb)  # 적록색약이 아닌 사람

cnt = 0  # 리셋
cnt_rg = check(bfs_rg)    # 적록색약인 사람

print(cnt_rgb, cnt_rg)