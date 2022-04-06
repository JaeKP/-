# 문제 url: https://www.acmicpc.net/problem/2206
from collections import deque

def bfs(y, x, cnt):
    q = deque()
    q.append((0, y, x))
    visit[0][y][x] = 1  # 방문 체크
    while q:
        wall, vi, vj = q.popleft()
        # 도착지에 도착하면 종료한다.
        if vi == N - 1 and vj == M - 1:
            return visit[wall][vi][vj]
        # 주변을 델타로 이동한다.
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = vi + di
            nj = vj + dj
            # 범위, 방문여부를 체크한다.
            if 0 <= ni < N and 0 <= nj < M and not visit[wall][ni][nj]:
                # 벽이면, 벽을 부신 횟수를 확인하고 부신 적이 없으면 이동한다.
                if arr[ni][nj] == '1':
                    if wall: continue
                    visit[1][ni][nj] = visit[wall][vi][vj] + 1
                    q.append((1, ni, nj))
                # 통로면, 그냥 이동한다.
                else:
                    visit[wall][ni][nj] = visit[wall][vi][vj] + 1
                    q.append((wall, ni, nj))

    return -1


N, M = map(int, input().split()) # N: 세로, M: 가로
arr = [list(input())for _ in range(N)]
visit =[[[0 for _ in range(M)] for _ in range(N)]for _ in range(2)]   # 3차원 방문 배열 visit[벽 부신 횟수][row][column]
print(bfs(0, 0, 0))