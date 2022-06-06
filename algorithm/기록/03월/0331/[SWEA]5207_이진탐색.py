# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT

def binary_search(array, k , start, end):
    prev = ''  # 이전에 어느쪽을 탐색했는지 기록한다.
    s = start  # 시작
    e = end    # 끝
    while s <= e:
        mid = (s+e)//2
        if array[mid] == k:  # 탐색 성공!
            return True
        # 배열의 중간값이 검색하고자 하는 값보다 크다면 배열의 왼쪽을 탐색한다.
        elif array[mid] > k:
            if prev == 'left':  # 연속으로 같은 방향을 탐색할 수 없다.
                return False
            prev = 'left'
            e = mid - 1
        # 배열의 중간 값이 검색하고자 하는 값보다 크다면 배열의 오른쪽을 탐색한다.
        else:
            if prev == 'right': # 연속으로 같은 방향을 탐색할 수 없다.
                return False
            prev = 'right'
            s = mid + 1

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split()) # N: a_list의 길이 , M: b_list의 길이
    a_list = sorted(list(map(int, input().split())))  # 정렬해서 저장
    b_list = list(map(int, input().split()))          # binary search를 할 원소리스트

    count = 0         # 조건에 맞는 경우의 수
    for b in b_list:
        # a_list에 b의 원소가 없다면 아예 binary search를 할 이유가 없다.
        if b in a_list:
            result = binary_search(a_list, b, 0, N - 1)
            if result:
                count += 1

    print(f'#{t} {count}')
