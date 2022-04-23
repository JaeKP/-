# 문제 url: https://www.acmicpc.net/problem/1197
from heapq import  heappop, heappush

def prim(start):
    global total_weight
    q = [(0, start)] # (가중치0, 시작정점)
    while q:
        # 가중치가 낮은 순서로 pop을 한다.
        weight, node = heappop(q)  # w: 가중치, node: 정점
        if tree[node] == 1: continue  # 이미 확정된 노드이면 pass
        tree[node] = 1
        total_weight += weight
        # 인접 정점을 순회한다.
        for w, v in arr[node]:
            # 확정되지 않았고 가중치가 더 적으면 q에 추가한다.
            if not tree[v] and weights[v] > w:
                weights[v] = w
                heappush(q, (w, v))

V, E = map(int, input().split())

tree = [0]*(V+1)             # 확정된 노드인지 확인하기 위한 리스트
weights = [2147483648]*(V+1) # 해당 노드의 가중치를 기록하는 리스트 (큰 수를 default로)
total_weight = 0             # 확정된 가중치의 합을 기록하는 변수

# 인접 리스트 생성
arr = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2, weight = (map(int, input().split()))
    arr[v1].append((weight, v2)) # (가중치, 인접 정점)
    arr[v2].append((weight, v1)) # (가중치, 인접 정점)

prim(1)
print(total_weight)
