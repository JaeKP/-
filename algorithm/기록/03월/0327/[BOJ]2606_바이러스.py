# 문제 url: https://www.acmicpc.net/problem/2606

from collections import deque

N = int(input())
M = int(input())
arr = [list(map(int, input().split()))for _ in range(M)]

# 인접 배열 생성
virus = [[] for _ in range(N+1)]
for v in arr:
    virus[v[0]].append(v[1])
    virus[v[1]].append(v[0])

# 방문 리스트,큐 생성
visit = [0]*(N+1)
q = deque()

# 시작점 셋팅
visit[1] = 1
q.append(1)
cnt = 0      # 바이러스에 걸리는 컴퓨터의 수

# 탐색!
while q:
    node = q.popleft()
    for new in virus[node]:
        if visit[new] == 0: # 방문한 적 없는 정점이면
            cnt += 1        # 정점을 이동할 때 마다 카운팅!
            visit[new] = 1  # 방문!
            q.append(new)   # 방문!

print(cnt)