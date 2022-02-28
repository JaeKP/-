# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVFCzaqeUDFAWg
T = int(input())

for t in range(1, T+1):
    N, M = map(int, input().split())
    list_ = list(map(int, input().split()))
    max_v = 0                     # 최댓값을 구하기 위한 변수 설정
    min_v = 10000 * M             # 최솟값을 구하기 위한 변수 설정 (리스트원소의 최댓 값은 10000이기 때문에 이를 활용하여 기본값 세팅)

    # 구간 합 구하기
    for i in range(0, N-M+1):     # 시작 인덱스
        total = 0
        for j in range(0, M):     # 합을 구할 구간의 인덱스를 순회
            total += list_[i+j]   # 구간 합!
        if total > max_v:         # 최댓값인지 확인하기 위한 조건문
            max_v = total
        if total < min_v:         # 최솟값인지 확인하기 위한 조건문
            min_v = total

    print(f'#{t} {max_v - min_v}')
