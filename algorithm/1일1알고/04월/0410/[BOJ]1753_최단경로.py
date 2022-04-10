# 문제 url: https://www.acmicpc.net/problem/1753
from heapq import heappop, heappush

def make_short(start):
    q = [(0, start)]      # 출발!
    while q:
        w, v = heappop(q) # 현재 가장 거리가 짧은 정점을 pop!
        if graph[v]: continue
        graph[v] = 1      # 해당 정점 확정!
        # 인접정점 탐색
        for weight, node in arr[v]:
            # 확정된 정점이 아니고 거리가 기존에 기록된 것보다 짧다면 갱신한다.
            if not graph[node] and distance[node] > distance[v] + weight:
                distance[node] = distance[v] + weight
                heappush(q, (distance[node], node))

V, E = map(int, input().split()) # V: 정점의 개수, E: 간선의 개수
K = int(input())

# 인접 정점 및 가중치에 대한 정보를 저장하는 리스트
arr = [[] for _ in range(V+1)]

# (가중치, 인접 정점)을 저장한다.
for _ in range(E):
    s, e, w = map(int, input().split())
    arr[s].append((w, e))

# 확정되었는지 확인하는 리스트
graph = [0]*(V+1)

# 거리를 저장하는 리스트(default는 아주 큰 값이다)
distance = [0xffffff]*(V+1)
distance[K] = 0  # 출발점은 거리가 0이다.

make_short(K)

for i in range(1, V+1):
    # default값 그대로라면 경로가 존재하지 않는 것이다.
    if distance[i] == 0xffffff:
        print('INF')
    else:
        print(distance[i])
