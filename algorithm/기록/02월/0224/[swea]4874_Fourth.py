# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg
T = int(input())

for t in range(1, T+1):
    words = input().split()
    print(f'#{t}', end = ' ')
    stack = []

    for word in words:
        if word == '+':           # + 연산자일 경우
            if len(stack) <= 1:   # 피연산자가 부족하거나 스택이 비어있으면
                print('error')    # 에러!
                break
            else:                 # 그렇지 않을 경우, 정상적으로 연산을 해서 스택에 저장
                stack.append(stack[-2] + stack[-1]) 
                stack.pop(-2)     # 연산에 사용한 피연산자 제거 
                stack.pop(-2)     # 연산에 사용한 피연산자 제거 
        elif word == '-':
            if len(stack) <= 1:
                print('error')
                break
            else:
                stack.append(stack[-2] - stack[-1])
                stack.pop(-2)
                stack.pop(-2)
        elif word == '/':
            if len(stack) <= 1:
                print('error')
                break
            else:                # /연산자일 경우,  항상 나누어떨어지기 때문에 //로 연산
                stack.append(stack[-2] // stack[-1])
                stack.pop(-2)
                stack.pop(-2)
        elif word == '*':
            if len(stack) <= 1:
                print('error')
                break
            else:
                stack.append(stack[-2] * stack[-1])
                stack.pop(-2)
                stack.pop(-2)
        elif word == '.':       # 무조건 가장 마지막에 오는 토큰
            if len(stack) > 1:  # 스택에 남아있는 피연산자가 2개 이상이면 에러!
                print('error')
                break
            else:
                print(stack[0])
        else:
            stack.append(int(word))

