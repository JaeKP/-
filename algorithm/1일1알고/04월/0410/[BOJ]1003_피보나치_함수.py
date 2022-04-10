# 문제 url: https://www.acmicpc.net/problem/1003

# 피보나치 함수
# 메모이제이션을 활용하여 실행시간을 단축시킨다.
def fibonacci(n, array):
    # -1이 아니면 리스트에 값이 기록되어 있는 것이다.
    if array[n] != -1:
        return array[n]
    
    array[n] = fibonacci(n-1, array) + fibonacci(n-2, array)
    return array[n]

# N은 최대 40이기 때문에 0부터 40까지 저장한다.(default는 -1이다)
fibo_0 = [-1]*41  # 0 개수를 기록하는 리스트
fibo_1 = [-1]*41  # 1 개수를 기록하는 리스트

# 기저사례를 표시한다.
fibo_0[0] = fibo_1[1] = 1
fibo_0[1] = fibo_1[0] = 0

T = int(input())
for t in range(T):
    N = int(input())

    print(fibonacci(N, fibo_0), fibonacci(N, fibo_1))