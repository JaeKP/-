# 문제 url : https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD&categoryId=AV14geLqABQCFAYD&categoryType=CODE&problemTitle=1219

for test in range(10):
    t, n = map(int, input().split())
    arr = list(map(int, input().split()))
    print(f'#{t}', end=' ')

    # 인접 행렬 만들기
    map_list = [[0] * 100 for _ in range(100)]
    for i in range(n):
        a = arr[i * 2]
        b = arr[i * 2 + 1]
        map_list[a][b] = 1             # 일방 통행

    stack = [0]                        # 이동경로를 표현하는 스택을 쌓기 위한 리스트(기본값은 시작점으로 세팅)
    visited = [False] * 100            # 인접 도로에 방문여부를 확인하기 위한 리스트
    visited[0] = True                  # 시작지점은 처음에 방문하기 때문에 True

    # 스택을 활용하여 지도 조사
    while stack:
        v = stack[-1]                 # 시작 지점은 가장 최근에 방문한 곳
        if v == 99:                   # 99에 도착!
            print(1)
            break
        for i in range(100):          # 2차원 배열의 column을 순회
            # 만약 인접지역인데 방문한 적이 없다면 그 지역으로 이동
            if map_list[v][i] == 1 and visited[i] == False:
                visited[i] = True     # 방문한 적 있음을 리스트에 표시
                stack.append(i)       # 이동경로를 표현하는 stack에 추가
                break

        # 인접지역을 전부 다 방문했다면 방문한 적 없는 곳이 나올 때까지 pop!
        else:
            stack.pop()
    else:
        print(0)


