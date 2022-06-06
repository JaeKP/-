# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDrI61lYDFAVT#

def battery(k, n):
    global g_ssum
    global g_min_ssum

    if g_min_ssum < g_ssum: # 가지치기
        return
    if k == n:
        g_ssum += arr[number[-1]][1]  # 마지막 베터리 사용량 추가
        if g_ssum < g_min_ssum:
            g_min_ssum = g_ssum
        g_ssum -= arr[number[-1]][1]  # 다시 제거한다.
        return

    for i in range(2, n):
        if used[i]:       # 현재 생성 중인 수열에 값이 포함되어 있으면 pass
            continue
        used[i] = 1       # 사용처리
        number.append(i)  # 생성 중인 수열에 추가
        g_ssum += arr[number[-2]][number[-1]] # 배터리 사용량을 더한다.
        battery(k+1, n)   # 재귀
        g_ssum -= arr[number[-2]][number[-1]] # 배터리 사용량을 복구
        number.pop()  # 생성 중인 수열에서 제거
        used[i] = 0   # 미사용 처리


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*(N+1)] + [[0] + list(map(int, input().split()))for _ in range(N)]
    number = [1]        # 맨 앞이 1인 수열을 생성해야 한다.
    used = [0] * (N+1)  # 해당 값을 수열에 포함시켰는지 확인하기 위한 리스트

    g_ssum = 0         # 배터리 소비량
    g_min_ssum = 1000  # 최소 배터리 소비량 (default: 최대)

    battery(2 , N+1)
    print(f'#{t} {g_min_ssum}')