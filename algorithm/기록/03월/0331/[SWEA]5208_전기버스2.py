# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYGf7K180DFAVT

def bus(i, power, cnt):
    global min_cnt
    if cnt >= min_cnt:   # 가지 치기
        return
    if not power:        # power가 없으면 이동을 못한다.
        return
    if i >= N-1:         # 목적지에 도착하면 리턴!
        if min_cnt > cnt:
            min_cnt = cnt
        return

    bus(i+1, arr[i+1] , cnt+1)  # 배터리 교체
    bus(i+1, power-1, cnt)     # 배테러 교체를 하지 않는다.

T = int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))
    N = arr[0]
    min_cnt = N   # 최솟값
    bus(1, arr[1], 0)
    print(f'#{t} {min_cnt}')





