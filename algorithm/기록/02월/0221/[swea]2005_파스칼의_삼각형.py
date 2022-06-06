T = int(input())

for t in range(1, T+1):
    N = int(input())
    number= []

    print(f'#{t}')
    for i in range(N):
        result= []
        for j in range(i+1):
            if j == 0:                    # result 첫 번째 인덱스(무조건 값이 1이다)
                result.append(1)
            elif j == i:                  # result의 마지막 인덱스(무조건 값이 1이다)
                result.append(1)
            else:                         # 파스칼 삼각형의 패턴!(문제풀이 참고)
                result.append(number[-1] + number[-2])
                number.pop()
        print(*result)
        number = result