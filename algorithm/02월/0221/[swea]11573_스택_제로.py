T =int(input())

for t in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    result = []                    # 숫자를 기록하기 위한 빈리스트
    total = 0                      # 기록된 숫자들의 합을 저장하기 위한 변수

    for number in numbers:         # 사용자가 입력한 숫자를 순회
        if number == 0:            # 숫자가 0이면
            total -= result[-1]    # 가장 최근에 result에 추가한 값을 숫자들의 합에서 제외
            result.pop()           # 숫자를 기록하는 리스트에서도 삭제
        else:
            total += number        # 기록할 숫자를 합에 추가
            result.append(number)  # 숫자를 기록


    print(f'#{t} {total}')
