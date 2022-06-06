# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYHO7a2JoDFAVT#
from heapq import heappop, heappush

T = int(input())
for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    for _ in range(E):
        v1, v2, w = map(int, input().split())
        arr[v1].append((w, v2))
        arr[v2].append((w, v1))

    weight = [0xffffff]*(V+1)
    parent = [num for num in range(V+1)]
    visit = [0] * (V + 1)
    total_weight = 0

    # 임의의 정점을 시작점으로 한다.
    weight[0] = 0
    q = [(0, 0)]

    # q가 비어질 때까지 반복한다.
    while q:
        w, v = heappop(q) # q에 누적된 정점들 중에서 가장 가중치가 적은 것을 pop한다.
        if visit[v]: continue
        # 방문하지 않은 정점(확정되지 않은 정점)이면 방문처리한다.
        # 이 때, 해당 정점의 가중치는 w로 확정된다.
        visit[v] = 1
        total_weight += w

        # 확정된 정점의 인접정점을 확인한다.
        for value, node in arr[v]:
            # 만약 확정되지 않았고, 가중치가 현재 기록된 것 보다 적다면 갱신한다.
            if not visit[node] and weight[node] > value:
                weight[node] = value # 가중치 수정
                parent[node] = v     # 부모 수정
                heappush(q, (value, node)) # q에 추가


    print(f'#{t} {total_weight}')
