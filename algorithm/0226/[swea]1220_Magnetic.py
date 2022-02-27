# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD

# 10개의 테스트케이스
for t in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range (N)]  # 0: 빈자리, 1: N극, 2: S극

    cnt = 0

    for j in range(N):         # 열 우선 순회
        stack = []             # 빈 스택
        i = 0                  # i = 0 (새로운 열을 탐색할 때 마다 리셋)
        while i < N:           # 행 순회
            # 스택이 비워있고 1이 나오면 스택에 1을 추가
            if  arr[i][j] == 1 and not stack:
                stack.append(1)
            # 스택이 비워져있지 않고 2가 나오면 스택 pop하고 교착 상태 카운트 +1
            elif arr[i][j] ==2 and stack:
                stack.pop()
                cnt += 1
            i += 1

    print(f'#{t} {cnt}')



