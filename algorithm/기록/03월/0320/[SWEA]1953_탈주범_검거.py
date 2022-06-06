# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PpLlKAQ4DFAUq
from collections import deque

T = int(input())
for t in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    # 파이프를 표현하는 list를 생성한다.
    # 0번: 상, 1번: 하, 2번:좌, 3번:우
    pipe = [(),(0, 1, 2, 3), (0, 1), (2, 3), (0, 3), (1, 3), (1, 2),(0, 2) ]

    # 현재 내 파이프에 0 이 있을 때, 인접 파이프에 1이 있어야 이동이 가능하다.
    # 현재 내 파이프에 1 이 있을 때, 인접 파이프에 0이 있어야 이동이 가능하다.
    # 현재 내 파이프에 2 가 있을 때, 인접 파이프에 3이 있어야 이동이 가능하다.
    # 현재 내 파이프에 3 이 있을 때, 인접 파이프에 2가 있어야 이동이 가능하다.
    next_pipe = [1, 0, 3, 2]  # 현재 파이프의 번호를 인덱스로 하고, 인접파이프에 있어야 하는 파이프 번호를 값으로 넣는다.

    # 방문을 확인하는 배열
    visit = [[0]*M for _ in range(N)]

    cnt = 0  # 탈주범이 이동할 수 있는 파이프를 카운팅하는 변수
    def bfs(r, c):   # r: 출발하는 행의 위치 c: 출발하는 열의 위치
        global cnt
        q = deque()
        q.append((r, c))
        visit[r][c] = 1  # 방문 배열에 탐색 깊이를 저장한다.
        cnt += 1

        while q:
            vi, vj  = q.popleft()
            if visit[vi][vj] == L:  # L의 깊이만큼 이동하면 반복을 종료한다.
                return cnt
            delta_r = [-1, 1, 0, 0]      # 상 하 좌 우
            delta_c = [0, 0, -1, 1]      # 상 하 좌 우
            for p in pipe[arr[vi][vj]]:  # 현재 위치한 파이프가 가지고 있는 상세 파이프 번호를 순회
                ni = vi + delta_r[p]
                nj = vj + delta_c[p]

                # 범위체크, 파이프 확인 , 방문 여부 확인 => 이 모든 조건을 만족하면 이동한다.
                if 0 <= ni < N and 0 <= nj < M and  next_pipe[p] in pipe[arr[ni][nj]] and visit[ni][nj] == 0:
                    q.append((ni, nj))
                    visit[ni][nj] = visit[vi][vj] + 1   # 방문 배열에 탐색 깊이를 저장한다.
                    cnt += 1

        return cnt

    print(f'#{t} {bfs(R, C)}')


