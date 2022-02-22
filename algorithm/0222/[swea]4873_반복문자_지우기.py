# 문제 url: https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVHzyqqe8DFAWg
T = int(input())

for t in range(1, T+1):
    s = input()
    result = []                    # 반복문자를 제거하고 문자를 저장할 빈 리스트

    for word in s:
        if not result:             # 리스트가 비어있으면 무조건 추가
            result.append(word)
        elif result[-1] == word:   # 리스트의 마지막 인덱스가 추가할 문자와 같다면 (반복문자)
            result.pop()           # 마지막 인덱스 값 제거
        else:
            result.append(word)    # 반복문자가 아닐경우엔 리스트에 문자 추가

    print(f'#{t} {len(result)}')