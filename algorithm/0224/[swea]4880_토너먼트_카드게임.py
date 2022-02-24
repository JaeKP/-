# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg

T = int(input())

# 가위 바위 보 승리
def battle(i, j):
    if arr[i] == 1:                  # 가위
        if arr[j] == 2:
            return j
        else:
            return i
    elif arr[i] == 2:                # 바위
        if arr[j] == 3:
            return j
        else:
            return i
    elif arr[i] == 3:                # 보
        if arr[j] == 1:
            return j
        else: return i


def check(start, end):
    # 종료 조건
    if start == end:                # 탐색이 끝나면
        return start                # return
    else:
        mid = (start + end) // 2    # 두 그룹으로 나누기 위함 
        l = check(start, mid)       # 중간 값 기준 왼쪽 구간을 재귀
        r = check(mid + 1, end)     # 중간 값 기준 오른쪽 구간 재귀
        return battle(l, r)         # 재귀를 통해 얻은 l,r의 값을 battle함수의 매개변수로 활용

for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    print(f'#{t} {check(0, N-1)+1}')   # arr[0]이 1번 학생이기 때문에 결과에 +1을 함

