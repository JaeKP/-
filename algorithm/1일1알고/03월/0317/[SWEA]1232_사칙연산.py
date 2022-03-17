import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    N = int(input())
    arr = [list(input().split())for _ in range(N)]

    # 정점의 왼쪽 자식, 오른쪽 자식을 저장한다.
    # 인덱스: 부모의 정점 번호, 값: 자식의 정점 번호
    left = [0] * (N + 1)
    right = [0] * (N+1)
    for num in arr:
        if len(num)>=3:
            left[int(num[0])] = int(num[2])
        if len(num)>=4:
            right[int(num[0])] = int(num[3])

    # 트리를 후위 순회 하는 함수
    tree = []
    def make_tree(v):
        if not v:
            return
        make_tree(left[v])
        make_tree(right[v])
        tree.append(v)
    make_tree(1)

    # 트리 정점의 값으로 채워진 리스트 생성 (후위 순회 순서로 정렬되어 있음)
    calculation = []
    for num in tree:
        math = arr[num-1][1]
        calculation.append(math)

    # stack으로 후위 표기법 계산하기
    # 피연산자는 스택에 push한다.
    # 연산자는 필요한 만큼의 피연산자를 stack에서 pop하여 연산하고, 연산 결과를 stack에 push한다.
    stack = []
    for num in calculation:
        if num  not in '+-*/':
            stack.append(int(num))
        if num == "+":
            a = stack.pop()
            b = stack.pop()
            stack.append(b+a)
        if num == "-":
            a = stack.pop()
            b = stack.pop()
            stack.append(b-a)
        if num == "*":
            a = stack.pop()
            b = stack.pop()
            stack.append(b*a)
        if num == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(b//a)
    print (f'#{t}', end=' ')
    print(*stack)









