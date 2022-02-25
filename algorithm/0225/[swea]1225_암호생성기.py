import sys
sys.stdin = open('input.txt')

for _ in range(10):
    t = int(input())
    Q = [0] + list(map (int, input().split()))  # 원형 queue를 위한 빈자리 추가

    #  데이터 삽입 함수
    def enqueue(add):
        global rear
        rear = (rear +1) % n   # 모듈러 연산
        Q[rear] = add

    # 데이터 삭제 함수
    def dequeue():
        global front
        front = (front +1) % n  # 모듈러 연산

    n = len(Q)
    front = 0
    rear = n-1                  # 이미 Q에 데이터가 저장이 되었기 떄문에 full처리

    Flag = True                 # 함수를 종료시키기 위한 변수
    while Flag:
        for i in range(1, 6):   # 암호화를 위해 더할 값 1~5 순회
            dequeue()           # 데이터를 추가하기 위해 데이터 삭제
            if Q[front]-i <= 0: # 암호화가 된 데이터가 0이하면 반복문 종료!
                enqueue(0)      # 0이하의 값은 0으로 취급
                Q.pop(front)    # 순서를 정리하기위해 빈자리 제거
                Flag= False
                break
            else:               # 데이터 추가
                enqueue(Q[front]-i)

    # 만약 rear가 Q의 마지막 인덱스에 위치해있으면 그대로 출력해도 된다. (위치조정이 필요 없음)
    # 그렇지 않을 경우 Q[front] Q[front]~ Q[n-1]을 먼저 출력한뒤, Q[0]~Q[rear]을 출력한다.
    if rear == (len(Q)-1):
        print(f'#{t}', end = ' ')
        print(*Q)
    else:
        a = Q[front:n]
        b = Q[0:front]
        print(f'#{t}', end = ' ')
        print(*a , end= ' ')
        print(*b)

