T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    Dict = {chr(num):0 for num in range(65, 91)}    # key = 알파벳 , value = 0 인 딕셔너리 생성

    for word in str2:                               # 문자열 str2 순회
        Dict[word] += 1                             # 문자를 key로 갖는 딕셔너리의 value에 +1 (중복 횟수 저장)

    max_v = 0                                      # 최대 중복 횟수를 구하기 위한 변수
    for word in str1:                              # 문자열 str 1 순회
        if Dict[word] > max_v:                     # 값이 더 크다면 (중복이 더 많이 되었다면)
            max_v = Dict[word]                     # 변수 재할당

    print(f'#{t} {max_v}')


#=========================================================================
# 빈딕셔너리 만들지 않고 바로 저장하기

T = int(input())

for t in range(1, T+1):
    str1 = input()
    str2 = input()
    dict = {}

    for word in str2:
        if dict.get(word) == None:              # 딕셔너리에 해당 하는 키가 없으면,
            dict[word] = 1                      # key =word, value = 1인 딕셔너리를 생성
        else:
            dict[word] += 1                     # 딕셔너리에 키가 있으면 그냥 +1

    max_v = 0
    for word in str1:
        if dict.get(word) > max_v:
            max_v = dict[word]

    print(f'#{t} {max_v}')
