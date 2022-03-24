# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYDLaK1kMDFAVT#url:

T = int(input())
for t in range(1, T+1):
    number = float(input())
    print(f'#{t}', end=' ')

    result = []
    while len(result) <= 12:     # 13자리 이상이 필요한 경우 overflow
        if not number:  # 이진수가 완성되면 종료
            break
        # 차례대로 2를 곱한 값이 1보다 크면 1!
        # 2의 -1승, -2승....이기 때문에 해당 자리의 수가 1이면 플러스 지수만큼 곱하면 1이 나오기 때문이다.
        # 0.5 = (1) * (2의 -1승)  => (1) * (2의 -1승) * (2의 1승) = 1이다.
        number = number * 2
        result.append(1 if number >= 1 else 0 )
        number = number % 1   # 소숫점 자리 수

    else:
        print('overflow')
        continue   # 아래 출력을 무시

    print(*result, sep = '')
