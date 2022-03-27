# 문제 url: https://www.acmicpc.net/problem/2589

from collections import deque

# 시작점 근처 육지를 너비 탐색하여 가장 깊은 깊이를 반환하는 함수
def bfs(q):
    while q:
        vi, vj = q.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = vi + di
            nj = vj + dj
            # 범위, 육지 방문 여부 확인
            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "L" and visit[ni][nj] == 0:
                visit[ni][nj] = visit[vi][vj] + 1  # 육지다!
                q.append((ni, nj))                 # 육지다!
    return visit[vi][vj]   # 깊이

N, M = map(int, input().split())
arr = [list(input())for _ in range(N)]
q = deque()
max_depth = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L': # 육지인 모든 정점을 탐색한다.
            visit = [[0] * M for _ in range(N)]
            visit[i][j] = 1  # 탐색 시작점
            q.append((i, j)) # 탐색 시작점
            depth = bfs(q)
            if max_depth < depth:
                max_depth = depth

print(max_depth-1)   # 깊이 1로 시작했기 때문에 깊이 -1을 해야 한다.
