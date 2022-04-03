# 문제 url: https://www.acmicpc.net/problem/2636
from collections import deque

# 외곽의 공기를 숫자 2로 수정하는 함수.
def bfs(i,j):
    visit = [[0]*W for _ in range(H)]
    q = deque()
    q.append((i, j))
    visit[i][j] = 1   # 방문!
    cheese[i][j] = 2
    while q:
        vi, vj = q.popleft()
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = vi + di
            nj = vj + dj
            # 범위, 방문 여부, 공기가 맞는지 확인한다.
            if 0 <= ni < H and 0 <= nj < W and visit[ni][nj] == 0 and (cheese[ni][nj] == 0 or cheese[ni][nj] == 2):
                q.append((ni, nj))
                visit[ni][nj] = 1  # 방문!
                cheese[ni][nj] = 2

H, W = map(int, input().split())  # H: 세로길이, W: 가로 길이
cheese = [list(map(int, input().split()))for _ in range(H)]
bfs(0, 0)

# 처음 판에 위치한 치즈 개수를 치즈 개수 리스트에 넣어준다.
cheese_cnt = []
first = 0
for i in range(H):
    for j in range(W):
        if cheese[i][j] == 1:
            first += 1
cheese_cnt.append(first)

# 치즈가 모두 녹아 없어질때까지 반복한다.
time = 0;
while True:
    cnt = 0
    for i in range(H):
        for j in range(W):
            melting = False
            if cheese[i][j] == 1:
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni = i + di
                    nj = j + dj
                    # 외곽의 공기(2)와 맞닿아 있다면 이번 시간에 녹는 치즈이다.
                    if 0 <= ni < H and 0 <= nj < W and cheese[ni][nj] == 2:
                        melting = True
                        break
                # 녹을 치즈라면 0으로 체크해준다.
                if melting:
                    cheese[i][j] = 0
                # 녹지 않는 치즈라면 카운팅!
                else:
                    cnt += 1
    # 한 번 순회가 끝나면 1시간이 지난 것이다.
    time += 1

    # 만약 녹지 않은 치즈가 없다면 반복문을 종료한다.
    if cnt == 0:
        break
    # 녹지 않은 치즈가 남았다면 다 녹을 때까지 반복한다.
    else:
        bfs(0, 0)
        cheese_cnt.append(cnt) # 치즈 개수 리스트에 추가

print(time)
print(cheese_cnt[-1])


