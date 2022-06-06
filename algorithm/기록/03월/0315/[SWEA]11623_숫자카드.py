# 문제 url: solving club - 0315
from collections import deque
T = int(input())

for t in range(1, T+1):
    N = int(input())

    # 자료구조 queue 활용
    q = deque()
    for n in range(N):
        q.append(n+1)

    # 가장 앞에 있는 카드를 버리고 그 다음으로 앞에 있는 카드를 가장 뒤로 이동시킨다.
    while len(q) > 1:   # 숫자가 1개 남으면 반복문 종료
        q.popleft()
        if len(q) ==1:
            break
        new = q.popleft()
        q.append(new)

    print(f'#{t}', end=' ')
    print(*q)






