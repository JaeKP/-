T = int(input())

for t in range(1, T+1):
    word = input()
    change = [['b', 'd'], ['d' ,'b'], ['p', 'q'], ['q', 'p']]  # 문자를 교체하기 위한 리스트
    length = len(word)
    n_word = ['']*length

    for i in range(length):                       # 문자 순회
        for j in range(4):                        # 교체 리스트를 순회
            if word[length-1-i] == change[j][0]:  # 문자를 교체하기 위한 조건문
                n_word[i]= change[j][1]           # 교체된 값을 문자열을 뒤집어서 새로운 리스트에 저장

    print(f'#{t}', end = ' ')
    print(*n_word, sep = '')
