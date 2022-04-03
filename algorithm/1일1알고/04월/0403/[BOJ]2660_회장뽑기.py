# 문제 url: https://www.acmicpc.net/problem/2660
from collections import deque

# i를 시작점으로 모든 정점을 탐색한다
def bfs(i):
    visit = [0]*(N+1)
    q = deque()
    q.append(i)
    visit[i] = 1
    while q:
        v = q.popleft()
        for node in arr[v]:
            # 방문한 적이 없다면 방문!
            if visit[node] == 0:
                visit[node] = visit[v]+1
                q.append(node)
    return visit[v]-1 # 해당정점이 모든 정점을 방문하는 깊이를 반환 (자신은 깊이에 포함되지 않기 때문에-1을 해야 한다.)

N = int(input())
arr = [[]for _ in range(N+1)]
depth = [0xffffff]*(N+1)           # 깊이를 기록하는 리스트 (최솟 값을 구하기 대문에 최댓값으로 채워놓는다.)
candidate_cnt = 0 ; candidate = [] # 후보자의 수, 후보자 리스트

# 인접 리스트를 생성한다. (회원의 번호를 인덱스로 회원과 직접 연결된 친구를 기록한다.)
while True:
    v1, v2  = list(map(int, input().split()))
    if v1 == -1 and v2 == -1:
        break
    else:
        arr[v1].append(v2)
        arr[v2].append(v1)

# 각 정점이 모든 정점을 방문하는 depth를 구한다.
for i in range(1, N+1):
    depth[i] = bfs(i) # i번 회원의 깊이를 기록한다.

# 깊이가 가장 적은 인덱스(회원 번호)를 찾기 위한 반복문
for i in range(1, N+1):
    if depth[i] == min(depth):
        candidate_cnt += 1
        candidate.append(i)
candidate.sort()

print(min(depth), candidate_cnt)
print(*candidate)

