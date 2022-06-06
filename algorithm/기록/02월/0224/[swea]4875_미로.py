# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(input())for _ in range(N)]
    print(f'#{t}', end = ' ')

    v = []                                   # 현재 방문위치를 저장할 변수

    # 시작 지점 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '2':
                v.append(i)
                v.append(j)

    visited = [[False]*N for _ in range(N)] # 방문이력을 체크하기 위한 2차 배열

    stack = [v]                              # 경로를 확인하기 위한 stack (시작 지점은 추가)
    visited[v[0]][v[1]] = True               # 시작 지점은 무조건 방문하기 때문에 미리 추가

    # 미로 탈출하기
    while stack:                            # 방문 경로가 없을때까지 반복한다. (스택이비워져있을 때 까지)
        v = [stack[-1][0],stack[-1][1]]     # 현재 방문 좌표는 stack[-1]에 있는 좌표임
        if arr[v[0]][v[1]] == '3':            # 도착!
            print(1)
            break

        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:   # 델타 (이동할수 있는 좌표에 접근하기위함)
            if not 0 <= v[0]+i < N:                       # 미로 내에 있는 좌표여야 이동할 수 있음
                continue
            elif not 0 <= v[1]+j < N:                     # 미로 내에 있는 좌표여야 이동할 수 있음
                continue
            elif arr[v[0]+i][v[1]+j] != '1' and visited[v[0]+i][v[1]+j] == False:  # 통로이고, 방문한 적이 없다면
                visited[v[0] + i][v[1] + j] = True                               # 방문!
                list_ =[v[0] + i, v[1] + j]
                stack.append(list_)                                              # 경로에 추가
                break
        else:
            stack.pop()

    else: print(0)


