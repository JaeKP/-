# 문제 url: https://www.acmicpc.net/problem/15656

def dfs(cnt):
    # M개의 수열
    if cnt == M:
        print(*arr)
        return
    for i in number:
        arr.append(i)  # i를 수열에 추가
        dfs(cnt+1)     # 다음에 들어갈 숫자 찾기
        arr.pop()      # number[i]를 수열에서 제거함으로서 원상태로 복구한다.

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort() # 오름차순 정렬
arr = []      # 수열을 저장할 빈 리스트

dfs(0)