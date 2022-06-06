# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg
T = int(input())

for t in range(1, T+1):
    words = input()
    list_ = [0]                    # 괄호를 저장할 리스트. 기본값 0 으로 설정

    print(f'#{t}', end = ' ')
    for word in words:
        if word == '(':
            list_.append('(')
        elif word == ')':
            if list_[-1] == '(':   # '('랑 짝이기 때문에 '('가 가장 마지막에 추가된 괄호여야 함
                list_.pop()
            else:
                print(0)
                break
        elif word == '{':
            list_.append('{')
        elif word == '}':
            if list_[-1] == '{':   # '{'랑 짝이기 때문에 '{'가 가장 마지막에 추가된 괄호여야 함
                list_.pop()
            else:
                print(0)
                break

    else:
        if list_== [0]:           # 끝나지 못한 괄호가 있는지 마지막으로 체크
            print(1)

        else:
            print(0)