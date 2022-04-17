# 문제 url: https://www.acmicpc.net/problem/15651

def dfs(cnt, k):
    # M개의 수열
    if cnt == M:
        print(*arr)
        return

    # 오름차순 수열이기 때문에 선택한 숫자보다 큰 숫자를 수열에 추가할 수 있다.
    for i in range(k, N+1):
        arr.append(i)    # i를 수열에 추가
        dfs(cnt+1, i+1)  # 다음에 들어갈 숫자 찾기 (i+1부터)
        arr.pop()        # i를 수열에서 제거함으로서 원상태로 복구한다.

N, M = map(int, input().split())
arr = [] # 수열을 저장할 빈 리스트

dfs(0, 1)