# 문제url: https://www.acmicpc.net/problem/14502
from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 안전 영역의 크기를 출력하는 함수
def check(array, cnt):
    for i in range(N):
        for j in range(M):
            if array[i][j] == 0:
                cnt += 1
    return cnt

# 해당 조합에 벽을 설치할 경우 안전영역을 체크하는 함수
def bfs(array):
    copy_map = [factor[:] for factor in map]  # 현재 지도를 복사한다.

    # 벽을 놓을 좌표를 순회하여 지도에 반영한다.
    for row, column in array:
        copy_map[row][column] = 1 # 해당 좌표에 벽을 세운다

    # 바이러스 근원지로부터 바이러스가 얼마나 퍼지는지 맵에 표현한다.
    for vi, vj in virus:
        q = deque()
        q.append((vi, vj))
        while q:
            i, j = q.popleft()
            for di, dj in delta:
                ni = i + di
                nj = j + dj
                # 범위 및 벽이 아닌 빈 공간인지 확인한다.
                if 0 <= ni < N and 0 <= nj < M and not copy_map[ni][nj]:
                    copy_map[ni][nj] = 2 # 감염!
                    q.append((ni, nj))   # 감염!
    cnt = check(copy_map, 0)
    return cnt

# 벽 리스트의 조합을 생성하여 해당 조합의 안전 영역 최대 크기를 비교한다.
def combination(s, r, n): # n 개중 r개를 뽑아야 한다., s: 시작인덱스
    global max_area, result
    if r == 0:
        area = bfs(result)
        if area > max_area:
            max_area = area
        return
    for k in range(s, n-r+1):
        result[r-1] = wall[k]
        combination(k+1, r-1, n)

N, M = map(int, input().split()) # N: 세로길이, M: 가로 길이
map = [list(map(int, input().split()))for _ in range(N)]  # 연구소 지도
wall = []      # 벽을 놀 수 있는 좌표
virus = []     # 바이러스 시작 좌표
result = [0]*3 # 벽 좌표 조합 결과
max_area = 0   # 안전 영역의 최대 크기

# 빈 공간 좌표를 찾는다. (벽을 설치 할 수 있는 공간)
for i in range(N):
    for j in range(M):
        if map[i][j] == 2:
            virus.append((i, j))  # 바이러스 리스트에 바이러스의 좌표 추가
        elif not map[i][j]:
            wall.append((i, j))   # 벽 리스트에 빈 공간 좌표 추가

combination(0, 3, len(wall))
print(max_area)