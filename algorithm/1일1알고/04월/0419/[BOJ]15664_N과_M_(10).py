# 문제 url: https://www.acmicpc.net/problem/15664
def dfs(cnt, k):
    # M개의 수열
    if cnt == M:
        ans.add(tuple(arr))
        return

    # 중복을 허용하는 오름차순 수열이기 때문에 선택한 숫자와 같거나 큰 숫자를 수열에 추가할 수 있다.
    for i in range(k, N):
        if visit[i]: continue
        visit[i] = 1           # 방문 체크 (i번째 숫자는 수열에 포함된다)
        arr.append(number[i])  # number[i]를 수열에 추가
        dfs(cnt + 1, i+1)      # 다음에 들어갈 숫자 찾기 (number[i]와 같거나 큰 수)
        arr.pop()              # number[i]를 수열에서 제거함으로서 원상태로 복구한다.
        visit[i] = 0           # 방문하지 않은 상태로 복구

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()  # 오름차순 정렬

visit = [0]*N  # 방문 체크 리스트 (수열에 포함되었나 확인)
arr = []       # 수열을 저장할 빈 리스트
ans = set()    # 결과를 저장할 빈 리스트 (set을 활용하여 중복을 제거한다)

dfs(0, 0)

# set을 list로 변환후 오름차순으로 정렬한다.
ans = list(ans)
ans.sort()

# 정렬한 결과를 출력!
for factor in ans:
    print(*factor)