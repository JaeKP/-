# 문제 url: https://www.acmicpc.net/problem/2493

# stack에 있는 탑은 수신할 타워를 찾고 있는 탑들이다.
# 지금 index에서 pop한 탑이 수신할수 있는 타워인지 확인한다.
def compare(x):
    # 스택이 비어있으면 비교를 하지 않는다.
    while stack:
        # 현재 pop한 타워의 높이 >= stack에 쌓여있는 탑이라면, 현재 pop한 타워가 레이저 신호를 수신한다.
        if tower[x] >= tower[stack[-1]]:
            ans[stack[-1]] = x+1
            # 수신하는 탑을 찾은 탑은 stack에서 pop한다.
            stack.pop()
        # 그렇지 않다면 return
        else:
            return
    return

N = int(input())   # 타워의 수
tower = list(map(int, input().split())) # 타워의 높이
index = list(range(N)) # 타워의 인덱스
stack = []  # 비교를 위한 stack
ans = [0]*N # 정답을 기록할 리스트 (수신하는 탑의 인덱스를 기록한다. )

# 타워를 다 확인해볼때까지 반복한다.
while index:
    tower_index = index.pop()
    compare(tower_index)
    # 비교가 끝났으면 pop한 탑을 stack에 push 한다.
    # 이 탑도 수신하는 탑을 찾아야 하기 때문이다.
    stack.append(tower_index)

print(*ans)