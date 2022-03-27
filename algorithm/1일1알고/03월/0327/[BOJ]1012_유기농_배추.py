# 문제 url: https://www.acmicpc.net/problem/1012

from collections import deque

T = int(input())
for t in range(1, T+1):
    M, N, K = map(int, input().split())  # M: 가로,  N: 세로, K: 배추의 개수
    arr = [list(map(int, input().split()))for _ in range(K)]

    # 배추를 밭(2차원 배열)에 배치
    field = [[0]*M for _ in range(N)]    # 빈밭
    for j, i in arr:
        field[i][j] = 1

    # 탐색!
    delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visit = [[0]*M for _ in range(N)]
    cnt = 0  # 필요한 벌레의 개수를 카운팅

    # 배추가 존재하는 좌표를 순회
    for j, i in arr:
        q = deque()
        # 방문한 적이 없다면 시작점으로 삼아 탐색을 시작한다.
        if visit[i][j] == 0:
            visit[i][j] = 1
            q.append((i, j))
            while q:
                vi, vj = q.popleft()
                for di, dj in delta:
                    ni = vi + di
                    nj = vj + dj
                    # 범위, 방문 여부, 배추가 존재하는 지 체크
                    if 0<= ni < N and 0<= nj < M and visit[ni][nj] == 0 and field[ni][nj] == 1:
                        visit[ni][nj] = 1  # 방문!
                        q.append((ni, nj)) # 방문!
            cnt+= 1  # 한 구역 끝! (벌레가 필요!)

    print(cnt)