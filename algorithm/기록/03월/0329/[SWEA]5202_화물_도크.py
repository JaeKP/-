# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT#

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [tuple(map(int, input().split()))for _ in range(N)]
    arr.sort(key = lambda x: (x[1])) # 종료시간 오름차순으로 정렬

    cnt = 0
    end = 0
    for s, e in arr:
        # 현재 작업의 시작하는 시간이 이전 작업의 종료시간보다 크거나 같으면 작업이 가능하다.
        if end <= s:
            cnt += 1  # 작업 수 + 1
            # 이 작업을 수행할 것이기 때문에 다음 작업의 시작 시간과 비교하기 위해 작업의 종료시간을 기록!
            end = e

    print(f'#{t} {cnt}')
