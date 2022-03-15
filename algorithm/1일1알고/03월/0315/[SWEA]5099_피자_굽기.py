# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIoJqqfYDFAWg#

from collections import deque
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    ci = list(map(int, input().split()))

    oven = deque()  # 오븐에 들어간 피자
    pizza = deque() # 오븐에 들어가지 않은 피자

    # 화덕 갯수에 따라 초기에 오븐에 들어갈 피자를 찾는다.
    for i in range(M):
        if i < N:
            oven.append([i,ci[i]])
        else:
            pizza.append([i,ci[i]])

    # 오븐에 피자가 한개 남을 때까지 반복한다.
    while len(oven) != 1:
        # 치즈가 녹으면 꺼내고 아직 오븐에 안넣은 피자가 있다면 뒤에 추가한다.
        if oven[0][1]//2 == 0:
            oven.popleft()
            if pizza:
                oven.append(pizza[0])
                pizza.popleft()
        # 치즈가 아직 녹지 않았으면 뒤로 보낸다.
        else:
            p = oven.popleft()
            oven.append([p[0],p[1]//2])

    print(f'#{t} {oven[0][0]+1}')  # 인덱스는 0부터 시작이기 때문에 피자번호를 구하기 위해서는 +1해야 한다.
