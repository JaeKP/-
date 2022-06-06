# 문제 url: https://www.acmicpc.net/problem/17471
from collections import  deque

# 배열안의 요소들을 반복하여 해당 요소가 연결되어있는지 확인 하는 함수
def check(array):
    if len(array) == 1:
        return True
    check_visit = [0] * (N + 1)
    q = deque()
    q.append(array[0])
    check_visit[array[0]] = 1
    while q:
        node = q.popleft()
        for v in arr[node]:
            if not check_visit[v] and v in array:
                check_visit[v] = 1
                q.append(v)
    for num in array:
        if not check_visit[num]:
            return False
    return True

# 차이를 계산하는 함수 2
def calc_array(array1, array2):
    a = 0
    b = 0
    for num1 in array1:
        a += population[num1]
    for num2 in array2:
        b += population[num2]
    return abs(a-b)

# 조합을 생성하는 함수
def make_combination(s):
    global minus
    if s > N:
        if zone_a and zone_b:
            ans_a=check(zone_a)
            ans_b=check(zone_b)
            if ans_a and ans_b:
                ans = calc_array(zone_a, zone_b)
                if ans < minus:
                    minus = ans
        return

    zone_a.append(s)
    make_combination(s+1)
    zone_a.pop()

    zone_b.append(s)
    make_combination(s+1)
    zone_b.pop()


# 연결을 확인하는 함수 2
def check_connect(n, cnt, array):
    q = deque()
    q.append(n)
    array[n] = cnt
    while q:
        node = q.popleft()
        for v in arr[node]:
            if array[v] == -1:
                array[v] = cnt
                q.append(v)


# 차이를 계산하는 함수 2
def calc(array):
    zone_a = 0
    zone_b = 0
    for i in range(1, N+1):
        if array[i] == 1:
            zone_a += population[i]
        else:
            zone_b += population[i]
    return abs(zone_a-zone_b)


N = int(input())
population = [0] + list(map(int, input().split()))
arr = [[]for _ in range(N+1)]

for i in range(1, N+1):
    node_list = list(map(int, input().split()))
    list_length = len(node_list)
    arr[i] = node_list[1:list_length]

visit = [-1]*(N+1)
cnt = 0
for i in range(1, N+1):
    if visit[i] == -1:
        check_connect(i, cnt, visit)
        cnt += 1

if cnt >= 3:
    print(-1)
elif cnt == 2:
    print(calc(visit))
else:
    zone_a = []
    zone_b = []
    minus= 0xffffff
    make_combination(1)
    print(minus)
