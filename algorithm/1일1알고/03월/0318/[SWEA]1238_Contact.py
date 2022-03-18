# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD&
from collections import deque
for t in range(1, 11):
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))


    # 인접 리스트 생성
    lst = [[]for _ in range(101)]
    for i in range(0, N, 2):
        lst[arr[i]].append(arr[i+1])

    # 연락 여부를 확인 하는 리스트
    calling = [0]*101

    # 연락하기
    # 연락을 시작하는 사람은 무조건 연락을 받기 때문에 미리 추가한다.
    q = deque()
    q.append(S)
    calling[S] = 1

    # 인접하고, 연락을 받지 않은 사람이면 연락한다.
    # 연락하고(v1) -> 연락 받고(v2) -> 연락 하고(v2) -> 연락 받고(v3)-> ...
    while q:
        v = q.popleft()                  # 연락을 하는 정점이면 q에서 제거한다.
        for i in range(len(lst[v])):
             if calling[lst[v][i]] == 0:
                 q.append(lst[v][i])            # 연락을 받은 인접한 정점을 q에 추가한다.
                 calling[lst[v][i]] = calling[v] + 1  # 연락을 몇번째로 받았는지를 연락방문여부를 확인하는 리스트에 추가한다.

    # 가장 연락을 늦게 받은 사람 중 가장 큰 번호를 확인한다.
    late = 0
    result = 0
    for i in range(101):
        if calling[i] >= late:
            late = calling[i]
            result = i

    print(f'#{t} {result}')



