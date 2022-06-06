# 문제 url: https://www.acmicpc.net/problem/7576

from collections import deque

# 토마토의 상태를 확인하는 함수
def check(array, n, m):
    global day
    for i in range(n):
        for j in range(m):
            if arr[i][j] > day:
                day = arr[i][j]
            if arr[i][j] == 0 : # 익지 않은 토마토가 있으면 -1을 리턴한다.
                return -1
    return day-1                # 첫 토마토는 제외해야 한다.


M, N = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
q = deque()  # 탐색을 위한 q
day = 0      # 마지막으로 토마토가 익는 날짜를 위한 변수

# 익은 토마토 찾기 (탐색의 시작점)
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append((i, j)) # q에 추가한다.

# 탐색!
while q:
    vi, vj = q.popleft()
    for di, dj in delta:
        ni = vi + di
        nj = vj + dj
        if 0<= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            arr[ni][nj] = arr[vi][vj] + 1 # 익었다! (토마토가 익는 시간을 기록하기 위해, 지난번 토마토가 익은 시간 +1로 기록한다.)
            q.append((ni, nj))            # 익었다!

print(check(arr, N, M))






