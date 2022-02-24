# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

T = int(input())

def battle(i, j):
    if arr[i] == 1:
        if arr[j] == 2:
            return j
        else:
            return i
    elif arr[i] == 2:
        if arr[j] == 3:
            return j
        else:
            return i
    elif arr[i] == 3:
        if arr[j] == 1:
            return j
        else: return i


def check(start, end):
    # 종료 조건
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        l = check(start, mid)
        r = check(mid + 1, end)
        return battle(l, r)

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{t} {check(0, N-1)+1}')   # arr[0]이 1번 학생이기 때문에 결과에 +1을 함

