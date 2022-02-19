# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT

T = int(input())

#  베이비 진인지 확인하는 함수
def baby_jin(count):
    for index in range(10):
        if count[index] >= 3:            # triplet!
            return True
    for index in range(8):               # 인덱스 에러가 나지 않기 위해 범위 조절
        if count[index] > 0 and count[index + 1] > 0 and count[index + 2] > 0:  # Run!
            return True

for t in range(1, T+1):
    arr = list(map(int, input().split()))

    count_a = [0]*10                   # counting을 하기 위한 빈 배열
    count_b = [0]*10                   # counting을 하기 위한 빈 배열
    victory = 0                        # 아무도 run, triplet을 달성하지 않으면 무승부이기때문에 무승부를 기본 값으로 설정

    # 카드 뽑기
    for i in range(12):
        if i%2 == 0:                  # 짝수면 a가 뽑는 순서이다.
            count_a[arr[i]] += 1
            if baby_jin(count_a):
                victory = 1           # a가 먼저 뽑기 때문에 먼저 달성하면 우승! (불합리하네..)
                break                 # 우승자가 나왔기 때문에 반복문 종료

        else:
            count_b[arr[i]] += 1
            if baby_jin(count_b):
                victory = 2
                break

    print(f'#{t} {victory}')




