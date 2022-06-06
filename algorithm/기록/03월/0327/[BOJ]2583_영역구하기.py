# 문제 url: https://www.acmicpc.net/problem/2583

from collections import deque

delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
# 주변에 있는 같은 영역을 탐색하는 함수
def bfs(q, array):
    w = 1 # 넓이
    while q:
        vi, vj = q.popleft()
        for di, dj in delta:
            ni = vi + di
            nj = vj + dj
            if 0<= ni < M and 0<= nj < N and paper[ni][nj] == 0: # 델타 범위, 직사각형 포함 여부, 방문 체크
                paper[ni][nj] = 1   # 같은 영역!
                q.append((ni, nj))  # 같은 영역!
                w += 1              # 넓이 + 1
    return array.append(w)

M, N, K = map(int, input().split()) # M: 세로, N: 가로, K: 직사각형 개수
arr = [list(map(int, input().split()))for _ in range(K)]
paper = [[0]*N for _ in range(M)]
q = deque()


# 직사각형을 2차원 배열에 배치한다.
for left_j, left_i, right_j, right_i in arr:
    for row in range(M-right_i, M-left_i):
        for column in range(left_j, right_j):
            paper[row][column] = 2

cnt = 0
wide = []
# 배열을 탐색한다.
for i in range(M):
    for j in range(N):
        # 직사각형, 탐색한 영역이 아니면 영역 탐색의 시작점으로 삼는다.
        if paper[i][j] == 0:
            q.append((i, j))  # 새로운 영역!
            paper[i][j]  = 1  # 새로운 영역!
            bfs(q, wide)      # 주변에 있는 같은 영역을 탐색하는 함수
            cnt += 1          # 같은 영역 탐색이 끝남.(영역의 개수 카운트 + 1)

wide.sort() # 정렬

print(cnt)
print(*wide)


