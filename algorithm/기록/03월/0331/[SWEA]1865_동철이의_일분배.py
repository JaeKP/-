# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LuHfqDz8DFAXc

def success(work, used, percent): # work: 일 번호 인덱스  , used: 순열에 값이 있는지 확인하기 위한 값, percent: 확률
    global max_percent
    # percent는 곱할수록 점점 작아지기 때문에 이미 다 계산을 한 max_percent보다 작으면 안된다.
    if max_percent >= percent:
        return

    if work == N:
        if max_percent < percent:
            max_percent = percent
        return

    for person in range(0, N):
        # 1인지 확인한다. (1이면 순열에 포함된 상태)
        if used & (1 << person): continue
        # work번째 일을 하는 사람을 정한 뒤, work+1 번째 일을 할 사람을 정한다.
        success(work + 1, used | (1 << person), percent * arr[work][person])


T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(lambda x: int(x)*0.01, input().split())) for _ in range(N)]

    max_percent = -1
    success(0, 0, 1)

    print('#{0} {1:0.6f}'.format(t, max_percent * 100))
