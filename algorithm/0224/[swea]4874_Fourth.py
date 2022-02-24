# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg
T = int(input())

for t in range(1, T+1):
    words = input().split()
    print(f'#{t}', end = ' ')
    stack = []

    for word in words:
        if word == '+':
            if len(stack) <= 1:
                print('error')
                break
            else:
                stack.append(stack[-2] + stack[-1])
                stack.pop(-2)
                stack.pop(-2)
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
            else:
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
        elif word == '.':
            if len(stack) > 1:
                print('error')
                break
            else:
                print(stack[0])
        else:
            stack.append(int(word))

