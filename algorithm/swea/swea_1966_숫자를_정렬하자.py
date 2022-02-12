T = int(input())

# 테스트 케이스 개수 만큼 반복한다.
for t in range(1, T+1):
    N= int(input())
    list_ = list(map(int, input().split()))

    # 오름차순 정렬 (카운팅 정렬 연습)
    # 카운팅 정렬을 하기 위해 최댓 값 구하기.
    max = list_[0]                   # 최댓값을 할당하기 위한 변수 선언
    for list_max in list_ :          # 리스트를 순회해서
        if max < list_max:           # 리스트의 값이 max에 할당된 값보다 크면
            max = list_max           # 리스트의 값을 변수 max에 재할당

    # 반복 횟수 구하기
    count = [0]*(max+1)              # 길이 max+1(0이 있기 때문에 1을 더함)인 리스트 생성
    for l_index in range(0, N):      # list_의 인덱스를 순회
        count[list_[l_index]] += 1   # list_의 값을 인덱스로 하는 count 리스트의 값에 1을 추가

    # 누적 횟수로 리스트 변환
    for c_index in range(1, max+1):  # count 인덱스 순회해서 누적 값을 재 할당
        count[c_index] = count[c_index] + count[c_index-1]

    # 정렬
    arry=[0]*N                       # 정렬된 리스트를 할당하기 위한 변수
    for l_index in range(0, N):      # 사용자가 입력한 리스트의 인덱스를 순회
        arry[(count[list_[l_index]])-1] =list_[l_index]   # pdf 자료 참고
        count[list_[l_index]] -= 1   # 중복 데이터를 정렬하기 위해 -1

    print(f'#{t}', end = ' ')
    print(*arry)
