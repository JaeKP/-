# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상

def bfs():
    q = deque()
    q.append((0, 0)) # 시작점
    D[0][0] = 0      # 시작점
    while q:
        row, column = q.popleft()
        for di, dj in delta:
            ni = row + di
            nj = column + dj
            # 델타 범위 체크 및 해당 경로의 거리가 기존보다 짧으면 이동한다.
            if 0<= ni <N and 0<= nj < N and D[ni][nj]> D[row][column] + map[ni][nj]:
                D[ni][nj] = D[row][column] + map[ni][nj] # 거리를 갱신
                q.append((ni, nj))  # 이동 !

T = int(input())
for t in range(1, T+1):
    N = int(input())
    map = [list(input())for _ in range(N)]
    for i in range(N):  # 입력받은 지도의 값을 숫자로 변환한다.
        for j in range(N):
            map[i][j]  = int(map[i][j])
    D = [[0xffffff]*N for _ in range(N)]  # 거리를 기록하는 2차원 배열

    bfs() # 탐색!
    print(f'#{t} {D[N-1][N-1]}')