# 문제 url: https://www.acmicpc.net/problem/2667
from collections import deque

N = int(input())
arr = [input()for _ in range(N)]

# 인접 좌표를 기록하는 배열 생성
lst = [[[]for _ in range(N)] for _ in range(N)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(N):
    for j in range(N):
        # 순회한 곳이 집이면 내 주변 집의 좌표를 기록한다.
        if arr[i][j] == '1':
            for di, dj in delta:
                ni = i+di
                nj = j+dj
                if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == '1':  # 범위 체크!
                    lst[i][j].append((ni, nj))
print(lst)
# 방문을 체크하는 배열 생성
visit = [[0]*N for _ in range(N)]  # 아직 방문을 하지 않았기 때문에 모두 0으로 기록한다.

# 2차배열을 순회하면서 방문한 적이 없는 집을 찾는다.
cnt = 0      # 단지의 수
house = []   # 단지별 집의 수를 저장하는 리스트
q = deque()  # 순회 때 사용하는 queue
for i in range(N):
    for j in range(N):
        house_cnt = 0
        # 지도를 순회하여 방문한 적이 없고, 집이면 단지의 시작점으로 설정
        if arr[i][j] == '1'and visit[i][j] == 0:
            q.append((i, j))
            visit[i][j] = 1
            cnt += 1        # 단지 수 +1
            house_cnt += 1  # 단지 내의 집의 수 +1

            # 시작 점을 기준으로 단지를 순회한다 (BFS)
            while q:
                vi, vj = q.popleft()
                for hi, hj in lst[vi][vj]:
                    if visit[hi][hj] == 0:
                        q.append((hi, hj))
                        visit[hi][hj] = 1
                        house_cnt += 1   # 단지 내의 집의 수 +1
            house.append(house_cnt)      # 단지 내의 총 집의 수를 기록한다.

# 출력 형식 맞추기
print(cnt)
house.sort()
for h in house:
    print(h)







