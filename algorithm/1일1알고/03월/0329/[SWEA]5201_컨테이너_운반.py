# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYEGw61n8DFAVT#

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    cargo = list(map(int, input().split()))
    truck = list(map(int, input().split()))

    cargo.sort(reverse=True) # 내림차순 정렬
    truck.sort(reverse=True) # 내림차순 정렬

    weight = 0    # 총 운반 무게
    i = 0         # 트럭리스트의 인덱스
    for c in cargo:
        # 화물 무게 <= 트럭 적재용량이면 운반할 수 있다.
        if c <= truck[i]:
            weight += c  # 운반!
            i += 1       # 다음 트럭!

        # 모든 트럭이 운반을 완료!
        if i == M:
            break
    print(f'#{t} {weight}')
