T = int(input())

for t in range(1, T+1):
    Word = input()
    length= len(Word)                     # 입력받은 문자열의 길이의 값을 할당

    print(f'#{t}', end = ' ')

    #비교
    for i in range(length//2):            # 문자열 길이 //2 만큼 순회
        if Word[i] != Word[length-1-i]:   # 같지 않으면 회문이 아님 (데칼코마니)
            print(0)
            break                         # 더이상 회문이 아니기때문에 반복문 종료
    else:
        print(1)
