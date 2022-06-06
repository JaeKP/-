# 문제 url: https://www.acmicpc.net/problem/15649

def dfs(cnt):
    # M개의 수열
    if cnt == M:
        print(*arr)
        return

    for i in range(1, N+1):
        # 중복없는 수열이기 때문에 중복이면 pass
        if i in arr: continue
        arr.append(i) # i를 수열에 추가
        dfs(cnt+1)    # 다음에 들어갈 숫자 찾기
        arr.pop()     # i를 수열에서 제거함으로서 원상태로 복구한다.

N, M = map(int, input().split())
arr = [] # 수열을 저장할 빈 리스트

dfs(0)