# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg#

from collections import deque

T = int(input())
for t in range(1, T+1):
    V, E = map(int,input().split())
    arr = [list(map(int, input().split()))for _ in range(E)]
    S, G = map(int, input().split())

    graph = [[] for _ in range(V + 1)]
    # 인접 배열 만들기
    for ti, tj in arr:
        graph[ti].append(tj)
        graph[tj].append(ti)

    def bfs():
        q = deque()
        visit = [0 for _ in range(V + 1)]

        # 출발 지점은 무조건 처음에 방문하기 때문에 미리 추가
        q.append(S)
        visit[S] = 1

        while q:  # 빈 q가 아니면 반복
            v = q.popleft()
            for node in graph[v]:
                # 도착하면 반복문 종료
                if node == G:
                    return visit[v]

                # 방문하지 않았던 인접 좌표
                if visit[node] == 0:
                    q.append(node)
                    visit[node] = visit[v]+ 1
        return 0   # 도착하지 못하면 0을 출력

    print(f'#{t} {bfs()}')

