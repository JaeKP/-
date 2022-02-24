# 문제 url: https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD&categoryId=AV14tDX6AFgCFAYD&categoryType=CODE&problemTitle=계산기

isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3}

for t in range(1, 11):
    n = int(input())
    word = input()

    # 중위 표기식의 후위 표기식 변환
    stack = []  # stack계산을 위한 리스트
    words = []  # 출력 할 리스트

    for token in word:
        # 연산자인 경우
        if token in isp:
            # 스택이 비어있다면 추가
            if not stack:
                stack.append(token)
            # toekn을 키로 갖는 icp 딕셔너리의 값 > stack[-1]을 키로 갖는 isp 딕셔너리 값이면, stack에 추가
            elif isp[stack[-1]] < icp[token]:
                stack.append(token)
            # stack[-1]을 키로 갖는 isp 딕셔너리 값 >= token을 키로 갖는 icp 딕셔너리의 값이면, pop!
            else:
                while icp[token] <= isp[stack[-1]]:
                    words.append(stack.pop())
                    if not stack:               # 스택이 비어있다면 반복문을 빠져나가서 그냥 추가한다.
                        break
                stack.append(token)

        # 닫는 괄호인 경우, 여는 괄호를 만나기 전까지 pop!
        elif token == ')':
            while stack[-1] != '(':
                words.append(stack.pop())
            stack.pop()  # 짝을 이룬 여는 괄호는 버린다.

        # 피연사자인 경우, 출력준비..
        else:
            words.append(token)

    # 스택에 남은 연산자 pop!
    while stack:
        words.append(stack.pop())

    # 후위 표기법의 수식을 스택을 이용하여 계산
    for token in words:
        # 연산자인 경우,
        if token == '+':
            stack.append(stack[-2] + stack[-1])
            stack.pop(-2)  # 연산후, 제거
            stack.pop(-2)  # 연산후, 제거
        elif token == '-':
            stack.append(stack[-2] - stack[-1])
            stack.pop(-2)
            stack.pop(-2)
        elif token == '*':
            stack.append(stack[-2] * stack[-1])
            stack.pop(-2)
            stack.pop(-2)
        elif token == '/':
            stack.append(stack[-2] / stack[-1])
            stack.pop(-2)
            stack.pop(-2)

        # 피 연산자인 경우, 숫자로 변환하여 스택에 추가!
        else:
            stack.append(int(token))

    print(f'#{t} {stack[0]}')