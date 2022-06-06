# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]

    cols = [_ for _ in range(N)]   # 순열
    min_v = 9 * 10                 # 최솟값을 저장하기 위한 변수 (최댓값으로 기본 설정)

    def check(k, check_sum):       # check_sum: 누적합
        global min_v
        if check_sum > min_v:      # 누적합이, 최솟값보다 크면 리턴
            return
        if k == N:                 # 종료조건
            if min_v > check_sum:
                min_v = check_sum  # 최솟값 저장
            return
        else:
            for i in range(k, N):
                cols[k], cols[i] = cols[i], cols[k]    # 교환의 방법으로 순열 구현
                check(k+1, check_sum+arr[k][cols[k]])  # 순열을 이용해 배열의 요소를 선택하고 이를 더함
                cols[k], cols[i] = cols[i], cols[k]    # 원본으로 복귀시키기 위한 코드

    check(0,0)
    print(f'#{t} {min_v}')