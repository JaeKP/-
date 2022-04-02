# 문제 url:https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT#
from collections import deque

# 탐색
def bfs():
    q = deque()  # 탐색할 정점을 기록하는 큐
    # 시작점을 큐와 거리에 기록한다.
    q.append(0)
    distance[0] = 0
    while q:
        node = q.popleft() # 탐색 시작!
        for v, d in near[node]: # 인접 리스트의 원소를 순회한다. v: 인접 정점,  d: 인접 정점까지의 거리
            # 만약 현재 해당 정점에 저장된 거리보다 짧은 거리라면 이를 기록한다.
            if distance[v] > distance[node] + d:
                distance[v] = distance[node] + d # 이동! 거리 기록
                q.append(v)        # 이동! 아직까진 이 경로가 최적해이다.

T = int(input())
for t in range(1, T+1):
    N, E = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(E)]

    near = [[] for _ in range(N+1)]
    # 인접 리스트 생성. 원소는 (인접 정점, 거리)와 같이 튜플형식으로 저장한다.
    for s, e, w in arr:
        near[s].append((e, w))

    # 거리를 기록하는 리스트를 생성한다.
    distance = [0xffffff] * (N + 1)

    bfs()
    print(f'#{t} {distance[N]}')