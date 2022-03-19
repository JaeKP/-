# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWngfZVa9XwDFAQU
from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())   # N: 정점의 수, M: 간선의 수
    arr = [list(map(int, input().split()))for _ in range(M)]

    # 인접 배열 생성
    lst = [[] for _ in range(N+1)]
    for i in range(M):
        lst[arr[i][0]].append(arr[i][1])
        lst[arr[i][1]].append(arr[i][0])

    # 방문 리스트 생성 (중복 방문 방지를 위한 리스트)
    visit = [0]*(N+1)

    # 방문하기
    q = deque()
    cnt = 0                 # 무리의 수
    for i in range(1, N+1): # 정점 번호를 순회한다.
        if visit[i] == 0:   # 아직 방문하지 않은 정점이라면, 방문 처리한다.
            visit[i] = 1
            q.append(i)
            cnt += 1        # 무리로 카운팅!

            # 이 정점과 관계가 있는 다른 정점이 있는지 확인
            # 관계가 있는 정점이 있다면, 이들도 차례대로 방문! (BFS)
            # 같은 앞서 카운팅한 무리와 같은 무리이기때문에 추가로 카운팅 하지 않는다.
            while q:
                node = q.popleft()
                for v in lst[node]:
                    if visit[v] == 0:
                        q.append(v)
                        visit[v] = node+1

    print(f'#{t} {cnt}')




