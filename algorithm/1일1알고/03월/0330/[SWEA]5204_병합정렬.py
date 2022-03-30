# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT

def merge(start, l_mid, end, array):
    global cnt
    ls = start; le = l_mid      # ls: 왼쪽 리스트의 시작 인덱스, le: 왼쪽 리스트의 마지막 인덱스
    rs= l_mid+1; re = end       # rs: 오른쪽 리스트의 시작 인덱스, re: 오른쪽 리스트의 마지막 인덱스
    i = start

    # 두 리스트를 인덱스 순서대로 값을 비교한다.
    # 오름차순 정렬을 하기 위헤 더 작은 값을 먼저 기록한다.
    while ls <= le and rs <= re:
        # 왼쪽 리스트의 값이 더 작을 때
        if array[ls] <= array[rs]:
            temp[i] = array[ls] # 기록!
            i += 1
            ls += 1 # 해당 인덱스는 정렬을 했기 때문에 다음 인덱스와 비교한다

        # 오른쪽 리스트의 값이 더 작을 때
        else:
            temp[i] = array[rs]
            i += 1
            rs += 1

    # 왼쪽 리스트만 남았을 때
    if ls <= le:
        cnt += 1 # 결과 출력을 위한 카운팅
        while ls <= le:
            temp[i] = array[ls]
            i += 1
            ls += 1
    # 오른쪽 리스트만 남았을 때
    else:
        while rs<= re:
            temp[i] = array[rs]
            i += 1
            rs += 1

    # 원래 배열에 반영한다.
    for t in range(start, end+1):
        array[t] = temp[t]

def merge_sort(start, end, array): # start: 배열의 첫 인덱스 번호, end: 배열의 마지막 인덱스 번호, array: 배열
    if start >= end: # 배열에 하나의 원소만 남을 때(정복) 리턴한다.
        return
    l_mid = (start+end-1) // 2
    merge_sort(start, l_mid, array)
    merge_sort(l_mid+1, end, array)

    merge(start, l_mid, end, array) # 병합


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    temp = [0] * N
    cnt = 0

    merge_sort(0, N-1, arr)
    print(f'#{t} {arr[N//2]} {cnt}')