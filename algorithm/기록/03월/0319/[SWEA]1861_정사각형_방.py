# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LtJYKDzsDFAXc
import sys
sys.stdin = open('input.txt')
from collections import deque
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

# 첫 풀이
    # # 이동할 수 있는 방을 표현하는 배열 생성
    # # 현재 좌표의 값과 인접한 좌표의 값이 1차이가 난다면 인접한 좌표를 기록
    # lst = [[[]for _ in range(N)] for _ in range(N)]
    # delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    # for i in range(N):
    #     for j in range(N):
    #         for di, dj in delta:
    #             ni = i + di
    #             nj = j +dj
    #             if 0 <= ni < N and 0 <= nj < N and ( arr[ni][nj] == arr[i][j] + 1 or arr[ni][nj] == arr[i][j] - 1):
    #                 lst[i][j].append((ni,nj))
    #
    # # 방문을 check 하는 빈 배열 생성
    # visit = [[0]*N for _ in range(N)]
    #
    # # lst 배열 순회
    # q = deque()
    # result = (100000, 0)     # 출력해야하는 결과를 저장할 변수 (방 번호, 방 이동 수)
    # for i in range(N):
    #     for j in range(N):
    #         cnt = 0    # 이동할 수 있는 방의 수를 할당하기위한 변수
    #         first = 0  # 탐색을 시작 하는 정점의 번호
    #         last = 0   # 마지막 탐색 정점의 번호
    #
    #         # 탐색을 시작하는 정점을 찾기 위한 조건문
    #         # lst[i][j]의 길이가 1이면 방 이동을 시작하는 정점이거나 마지막으로 방을 이동한 정점이다.
    #         if len(lst[i][j]) == 1 and visit[i][j] == 0:
    #             q.append((i, j))
    #             visit[i][j] = 1
    #             first = arr[i][j]    # 탐색을 시작하는 정점의 번호를 저장
    #
    #             #완전 탐색!(BFS)
    #             while q:
    #                 vi, vj = q.popleft()
    #                 for ri, rj in lst[vi][vj]:
    #                     if visit[ri][rj] == 0:
    #                         q.append((ri, rj))
    #                         visit[ri][rj] = visit[vi][vj] + 1
    #                         last = arr[ri][rj]  # 마지막 탐색 정점의 번호를 저장
    #         else:
    #             continue
    #
    #         cnt = visit[vi][vj]
    #
    #         # 탐색 시작 정점이 방 이동을 시작하는 정점인지, 마지막으로 방이동을 한 정점인지 파악
    #         if last < first:   # 탐색 시장 정점이 마지막 탐색 정점인 경우
    #             if result[1] < cnt or result[1] == cnt and last < result[0]:
    #                 result = (last, cnt)

    #         else:              # 탐색 시작 정점이 방 이동을 시작한 정점인 경우
    #             if result[1] < cnt or result[1] == cnt and first < result[0]:
    #                 result = (first, cnt)
    #
    # print(f'#{t}', end=' ')
    # print(*result)

# 다시 풀기.....ㅠㅠ

    # 탐색을 위한 함수
    def bfs(row, column):
        q = deque()
        visit_node = []  # 방문한 정점에 대한 정보를 저장한다.
        q.append((row, column))
        visit[row][column] = 1
        visit_node.append(arr[row][column])

        while q:
            vi, vj = q.popleft()
            for di, dj in [(0, 1), (1, 0), (0, -1),(-1, 0)]: # delta
                ni = vi + di
                nj = vj + dj
                if 0 <= ni < N and 0 <= nj < N and visit[ni][nj] == 0 and abs(arr[vi][vj]-arr[ni][nj])==1:
                    q.append((ni, nj))
                    visit[ni][nj] = 1
                    visit_node.append(arr[ni][nj])
        return min(visit_node), len(visit_node)


    # 방문을 체크하는 빈 배열을 생성
    visit = [[0] * N for _ in range(N)]

    # 탐색 시작 정점을 찾는다.
    max_cnt = 0
    min_node = 1000000
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                node, cnt = bfs(i, j)  # 탐색
                if cnt > max_cnt or cnt == max_cnt and min_node > node: # 결과 도출을 위한 비교
                    max_cnt = cnt
                    min_node = node

    print(f'#{t} {min_node} {max_cnt}')




