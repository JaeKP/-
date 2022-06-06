# 문제 url: https://www.acmicpc.net/problem/16234
from collections import  deque
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#  연합 국가를 찾는 함수
def bfs(row, column):
    # member: 같은 연합에 있는 나라의 좌표
    # cnt: 연합에 있는 국가의 수
    # ssum: 연합에 있는 국가의 인구 수 총 합
    member = [(row,column)]; cnt = 1; ssum = arr[row][column]
    q = deque()
    q.append((row, column))
    visit[row][column] = 1

    # 더 이상 연합할 나라가 없다면 반복을 종료한다.
    while q:
        ri, rj = q.popleft()
        for di, dj in delta:
            ni = ri + di
            nj = rj + dj
            # 조건(delta 범위 체크, 방문 체크, L <= 인접한 국가의인구수 차이 <= R인지 확인)
            if 0<= ni < N and 0 <= nj < N and not visit[ni][nj] and  L <= abs(arr[ri][rj]- arr[ni][nj]) <= R:
                visit[ni][nj] = 1        # 연합!
                member.append((ni, nj))  # 연합!
                q.append((ni, nj))       # 연합!
                cnt += 1                 # 연합 국가의 수 +1
                ssum += arr[ni][nj]      # 연합 국가 인구수 총합 +

    return (cnt, ssum, member)

# 연합된 국가끼리 인구 이동을 하는 함수
def merge(union, union_member):
    global move
    for index in range(len(union)):
        # people = 연합 국가의 총 인구수 // 연합 국가의 수
        people =  union_member[index][1] // union_member[index][0]
        for row, column in union[index]:
            arr[row][column] = people
    move += 1 # 인구 이동했다!

N, L, R = map(int, input().split())
arr = [list(map(int, input().split()))for _ in range(N)]
move = 0

while True:
    visit = [[0] * N for _ in range(N)]
    union = []
    union_member = []
    # 모든 좌표를 확인
    for i in range(N):
        for j in range(N):
            # 연합에 포함되지 않은 나라면 연합국가를 찾는다.
            if not visit[i][j]:
                cnt, ssum, member = bfs(i, j)

                # 연합이 있다면 연합 국가의 좌표와 연합에 대한 정보를 기록한다.
                if cnt > 1:
                    union_member.append((cnt, ssum))   # cnt: 연합에 있는 국가의 수, ssum: 연합에 있는 국가의 인구 수 총 합
                    union.append(member)               # meber: 연합에 포함된 국가의 좌표를 튜플로 기록한 리스트

    # 만약 연합국가가 없다면 반복을 종료한다.
    if not union:
        break
    else:
        merge(union, union_member)

print(move)
