# 문제 url: https://www.acmicpc.net/problem/15666

def dfs(cnt, pre): # cnt: 수열의 개수 , pre: 이전에 수열에 넣은 수
    # M개의 수열
    if cnt == M:
        ans.add(tuple(arr))
        return

    for num in number:
        # 이전에 뽑힌 수보다 같거나 커야 수열에 추가할 수 있다.
        if pre <= num:
            arr.append(num)        # number[i]를 수열에 추가
            dfs(cnt + 1, num)      # 다음에 들어갈 숫자 찾기
            arr.pop()              # number[i]를 수열에서 제거함으로서 원상태로 복구한다.

N, M = map(int, input().split())
number = list(map(int, input().split()))
number.sort()  # 오름차순 정렬

arr = []       # 수열을 저장할 빈 리스트
ans = set()    # 결과를 저장할 빈 리스트 (set을 활용하여 중복을 제거한다)

dfs(0, 0)

# set을 list로 변환후 오름차순으로 정렬한다.
ans = list(ans)
ans.sort()

# 정렬한 결과를 출력!
for factor in ans:
    print(*factor)