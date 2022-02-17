T = int(input())

for t in range(10):
    TN, N = input().split()
    Number = list(input().split())
    length = int(N)
    NA = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    Dict = {NA[i]:i for i in range(10)}  # 정수를 value로 갖는 딕셔너리를 생성
    cnt = [0]*10                         # 카운팅을 하기위한 빈 리스트
    arr = ['']*length                    # 정렬 데이터를 저장할 리스트


    # 카운팅 하기
    for n in Number:
        cnt[Dict[n]] += 1               # 정렬할 데이터가 중복된 횟수를 카운팅

    # 누적 합 구하기
    for i in range(1, 10):
        cnt[i] += cnt[i-1]              # 중복 횟수의 누적 값을 저장

    # 정렬하기
    for n in Number:                   # 정렬해야 하는 데이터를 순회
        cnt[Dict[n]] -= 1
        arr[cnt[Dict[n]]] = n          # 정렬

    print(TN)
    print(*arr)





