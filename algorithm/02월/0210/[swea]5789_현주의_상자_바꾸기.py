import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    box, re = map(int, input().split())
    boxes = [0]*box                        # 번호 0이 적힌 상자 리스트 생성

    for i in range(1, re+1):                
        L, R = map(int, input().split())   
        for j in range(L-1, R):           # L ~ R 상자 (index는 0부터 시작하기 때문에 -1)    
            boxes[j] = i                  # 박스에 숫자 부여

    print(f'#{t}', end = ' ')                    
    print(*boxes)                         # 언패킹을 통해 리스트안에 있는 값을 꺼내서 출력
