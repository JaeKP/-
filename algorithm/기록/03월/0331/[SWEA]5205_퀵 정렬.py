# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDYSqAAbw5UW6&subjectId=AWUYFsQq11kDFAVT

def partition(array, start, end):
    pivot = array[end]  # 크기를 비교할 숫자
    i = start - 1       # pivot 보다 작은 숫자 중 마지막 인덱스

    for j in range(start, end):  # 숫자를 순회하며, 정렬 시작!
        # pivot보다 작은 숫자이면, 교환한다.
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i] # 교환

    # pivot보다 큰 숫자 중 첫번째로 위치한 원소와 자리를 교환한다.
    # (pivot보다 작은 숫자) pivot (pivot보다 큰숫자)
    array[i+1], array[end] = array[end], array[i+1]
    return i+1 # pivot은 평생 이 자리다..

def quick_sort(array, start, end):
    if start >= end:
        return
    q = partition(array, start, end)     # 분할
    quick_sort(array, start, q-1) # 왼쪽 정렬
    quick_sort(array, q+1, end)   # 오른쪽 정렬

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    quick_sort(arr, 0, N-1)

    print(f'#{t} {arr[N//2]}')
