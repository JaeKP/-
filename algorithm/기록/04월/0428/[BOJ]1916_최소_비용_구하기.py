# 문제 url: https://www.acmicpc.net/problem/1916
from heapq import heappush,heappop

def dijkstra(s, e):
    q = [(0, s)]
    cost = [0xffffffff] * (N + 1) # 비용을 저장하는 리스트
    bus = [0] * (N + 1)         # 확정된 정점인지 확인하기 위한 리스트
    cost[s] = 0
    while q:
        # 가중치가(비용) 낮은 순서로 pop!
        weight, node = heappop(q)
        if bus[node]: continue
        bus[node] = 1 # 확정!
        if node == e:
            return cost[e]
        # 인접 정점 순회
        for w, r in arr[node]:
            # 확정되지 않았고, 가중치(비용) 더 적으면
            if not bus[r] and cost[r] > cost[node] + w:
                cost[r] = cost[node] + w
                heappush(q, (cost[r], r))
    return cost[e]


N = int(input())  # 도시의 개수
M = int(input())  # 버스의 개수


# 인접 리스트 생성
arr = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, w = map(int, input().split())
    arr[s].append((w, e))  # (버스 비용, 도착지)

S, E = map(int, input().split()) # S: 출발지 E: 도착지

print(dijkstra(S, E))
