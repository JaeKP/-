# 문제 url: https://swexpertacademy.com/main/learn/course/lectureProblemViewer.do

from collections import deque

# q에 다음 연산을  추가한다.
def append(n, q, cnt):
    q.append((n+1, cnt+1)) # (연산을 거친 n의 값, 연산 수행 횟수 cnt)
    q.append((n-1, cnt+1))
    q.append((n*2, cnt+1))
    q.append((n-10, cnt+1))

# 탐색
def bfs(n, m, cnt): # n: 연산 전의 자연수, m: 목표 자연수, cnt: 연산 횟수
    q = deque()
    # n과 m이 같으면 종료하고 연산 횟수를 반환한다.
    if n == m:
        return cnt
    append(n, q, cnt)

    while q:
        n, cnt = q.popleft()
        if n == m:
            return cnt
        if 0 <= n <= M*2+1 and not number[n]: # 범위 체크, 방문여부 확인
            number[n] = 1
            append(n, q, cnt)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())  # N: 시작, M: 목표
    # 같은 결과를 내는 연산을 반복하지 않게 하기 위해 숫자 결과에 대한 방문리스트 생성
    # 0이면 해당 숫자를 연산 결과로 도출한 적이 없다는 의미이다.
    number = [0]*(M*2+1)
    print(f'#{t} {bfs(N, M, 0)}')
