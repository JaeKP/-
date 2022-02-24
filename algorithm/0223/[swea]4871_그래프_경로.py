# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg

T = int(input())

for t in range(1, T+1):
    V, E = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(E)]
    S, G = map(int, input().split())
    print(f'#{t}', end = ' ')

    map_list = [[0]*51for _ in range(51)]
    # 인접 행렬 만들기
    for i in range(E):
        a = arr[i][0]
        b = arr[i][1]
        map_list[a][b] = 1   # 양방향

    v = S
    visited = [False] * 51
    stack = [v]
    visited[v] = True

    # 스택을 이용하여 지도 조사하기
    while stack:
        v = stack[-1]
        if v == G:
            print(1)
            break
        for i in range(V+1):
            if map_list[v][i] == 1 and visited[i] == False:
                stack.append(i)
                visited[i] = True
                break
        else:
            stack.pop()
    else:
        print(0)
