# 문제 url: https://www.acmicpc.net/problem/24955
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000000)

def dfs(v, end, num):
    # 종료 조건 (도착지에 도착하면 종료)
    if v == end:
        return print(num % MOD)

    # 인접한 노드를 탐색한다.
    for node in close[v]:
        if not visit[node]:
            visit[node] = 1
            # 숫자 계산
            new = home[node]    # 더할 숫자 (이번에 탐색한 숫자)
            len_new = len(str(new))
            # 현재 숫자 = (기존 숫자 * 10**더할 숫자의 길이) + 더할 숫자
            number = ((num*10**len_new)%MOD + new%MOD)% MOD
            dfs(node, end, number)

MOD=1000000007

N, Q = map(int, input().split())  # N: 집의 수 Q: 철수가 놀이를 할 횟수
home = [0] + list(map(int, input().split()))  # 집의 숫자

# 인접 리스트 생성
close = [[]for _ in range(N+1)]
for _ in range(3, N+2):
    s, e = map(int, input().split())
    close[s].append(e)
    close[e].append(s)

for _ in range(N+2, N+Q+2):
    start, end = map(int, input().split())
    visit = [0]*(N+1)
    num = home[start] % MOD
    visit[start] = 1
    dfs(start, end, num)
