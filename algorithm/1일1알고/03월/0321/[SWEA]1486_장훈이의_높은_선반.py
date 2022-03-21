# 문제url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV2b7Yf6ABcBBASw
def dfs(n, h):
    global min_h
    if h >= B and h - B > min_h:  # 가지 치기 (이미 최솟값 보다 크면 리턴)
        return
    if n == N:                    # 종료 조건
        if h >= B and min_h > h - B:
            min_h = h - B
        return
    dfs(n + 1, h + arr[n])        # n번째 직원을 포함한다.
    dfs(n + 1, h)                 # n번째 직원을 포함 하지 않는다.


T = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))

    min_h = B                    # 최솟 값을 구하기 위한 변수

    dfs(0, 0)
    print(f'#{t} {min_h}')

