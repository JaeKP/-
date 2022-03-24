# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT#

T = int(input())
for t in range(1, T+1):
    N, NUM = input().split()

    result = []
    for n in NUM:
        # 16진수를 10진수로 변환한다.
        decimal = int(n, 16)

        # 각 자리 숫자의 비트 값이 1인지 확인한다.
        # 16진수이기때문에 0부터 3까지의 자릿수를 확인한다.
        result.append(1 if decimal & 1 << 3 else 0)
        result.append(1 if decimal & 1 << 2 else 0)
        result.append(1 if decimal & 1 << 1 else 0)
        result.append(1 if decimal & 1 << 0 else 0)

    print(f'#{t}', end= ' ')
    print(*result, sep = '')