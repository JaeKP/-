from heapq import heappop, heappush

def bfs(i, j):
    return_list = [] # A노드의 비용 및 좌표를 기록할 리스트
    visit = [[0]*X for _ in range(Y)]
    bfs_q = [(i, j)]
    visit[i][j] = 1
    while bfs_q:
        vi, vj = bfs_q.pop(0)
        # 델타 이동
        for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ni = vi + di
            nj = vj +dj
            # 범위체크, 방문 체크, 이동할 수 있는 공간(A이거나 '_')인지 확인
            if 0 <= ni < Y and 0 <= nj < X and not visit[ni][nj] and not tree[ni][nj] and (arr[ni][nj] == 'A' or arr[ni][nj] == '_'):
                visit[ni][nj] = visit[vi][vj] +1
                bfs_q.append((ni, nj))
                # A이면 해당 정점에서부터 비용 및 좌표를 기록!
                if not tree[ni][nj] and arr[ni][nj] == 'A':
                    return_list.append((visit[vi][vj], ni, nj))
    return return_list

T = int(input())
for t in range(1, T+1):
    X, Y = map(int, input().split()) # X: 가로 Y: 세로
    arr = [list(input())for _ in range(Y)]
    weight = [[0xffffff]*X for _ in range(Y)]  # 가중치를 기록할 리스트
    tree= [[0]*X for _ in range(Y)]            # 트리로 확정된 정점을 기록하는 리스트
    total_weight = 0
    q = []

    # 트리 시작 좌표 찾기
    for i in range(Y):
        for j in range(X):
            if arr[i][j] == 'S':
                q.append((0, i, j)) # q에 추가
                weight[i][j] = 0    # 가중치는 0

    while q:
        w, vi, vj = heappop(q)
        if tree[vi][vj]: continue # 확정 트리가 아닌지 체크
        tree[vi][vj] = 1          # 이제 트리다!
        total_weight += w         # 이제 내 가중치다!
        node_distance= bfs(vi, vj)
        for value, i, j in node_distance:
            # 확정 트리가 아니고, 가중치가 더 적으면 갱신한다.
            if not tree[i][j] and weight[i][j] > value:
                weight[i][j] = value       # 갱신!
                heappush(q, (value, i, j)) # 갱신!

    print(total_weight)
