# 문제 url: https://www.acmicpc.net/problem/1932

def recur(r, c):
    # 종료 조건
    if r == N-1:
        return arr[r][c]

    # default값이 아니면 최댓값을 기록했기때문에 바로 사용한다.
    if memo[r][c] != -1:
        return memo[r][c]

    right = recur(r+1, c+1) # 오른쪽 대각선
    left = recur(r+1 , c)   # 왼쪽 대각선
    memo[r][c] = max(right, left) + arr[r][c]  # 내가 선택할 수 있는 가장 큰 수와 나의 합을 기록한다.
    return memo[r][c]


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
memo = [[-1]*N for _ in range(N)] # default는 -1

print(recur(0, 0))





