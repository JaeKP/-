# 재귀함수

## 정의 

> 자기 자신을 호출 하는 함수.
>
> 종료 조건이 충족될 때까지 반복적으로 자신을 불러내면서 주어진 작업을 수행한다. 

- 일반적으로 사용하지 않고 알고리즘 설계 및 구현에서 활용한다. 
- 파이썬 내의 최대 재귀 깊이가 있기때문에 무한루프를 방지해야 한다. 

<br>

```python
def recursive_function(): #재귀 함수 정의
	print('재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.')
	recursive_function()  #자기 자신 호출하여 다시 recursive_function()을 실행
    
    
recursive_function() # 함수 호출
```

```python
# 출력
# 최대 재귀 깊이가 1,000이기 때문에 최대 재귀 깊이를 초과하면 RecursionError가 발생합니다.
'재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.'
'재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.'
'재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.'
.
.
.
RecursionError: maximum recursion depth exceeded while calling a Python object 
```

<br>

## 활용

- 특정조건에 다다를 때 까지 스스로를 반복하기 때문에 이를 통해 직관적으로 알고리즘을 설계할 수 있다.
- 반드시 종료되는 상황을 작성해야 한다. (원하는만큼 반복을 하기 위함)
- 매개변수로 넘어온 값(전달인자)을 활용해 종료 조건으로  기입한다.

<br>

```python
def recursive_function(i): 
    if i == 5: # 종료 조건 작성
        return # return은 반환 값이 없어도 함수를 종료한다는 의미가 있음. 조건에 맞으면 함수를 종료시킴. 
    else:
        print('재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.')
    	recursive_function(i + 1)  # i+1을 하고 recursive_function()을 실행
    
    
recursive_function(0) # 함수 호출
```

```python
def recursive_function(i): 
    if i < 5: # 반복을 위한 조건
        print('재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.')
        recursive_function(i + 1) # 반복을 제어하기 위해 변수의 값 변경
        
recursive_function(0) # 함수호출
```

<br>

- `for` `while`과 같은 반복문으로 대체가 가능합니다. 이러한 반복문이 더 가독성이 좋은 경우도 있다.
- 또한, 재귀함수는 성능문제가 발생하기도 한다.
  - 호출될 때마다 메모리의 스택에 쌓이게 되고 앞서 사례처럼 한계 치 이상으로 호출되면 에러가 발생한다.
  - 속도면에 있어서도 반복문에 비해 시간을 더 소모한다.


```python
# while문을 활용
i = 0 
while i < 5:  
    print('재귀함수는 알고리즘 설계 및 구현에서 활용됩니다.')
    i += 1 # 반복을 제어하기 위해 변수의 값 변경
```

<br>

- 그러나 특정 상황에서 직관적으로 알고리즘을 설계할 수 있기때문에 알고리즘 설계 및 구현에서 활용된다. 이에 대한 예시는 다음과 같다.

<br>

## 예시

### 팩토리얼

> 팩토리얼(n!): 1부터 n까지의 정수를 곱하는 단순한 연산.  
>
> n! => n &#42;(n - 1)! => n&#42;(n - 1)&#42;(n-2) => ...



- for 반복 문 사용

```python
def factorial(num):
    result = 1 #값을 저장하기위해 변수 설정
    for i in range(1, num + 1):  #1 ~ n
        result= result * i  #순회한 값을 곱해서 변수에 저장
    return result
```



- 재귀 함수 사용

```python
def factorial(num):
    if num == 1:  # 종료조건을 설정
        return 1 # num이 1이되면 1을 반환하고 재귀 호출 종료
    return num * factorial(num -1 ) # num 이 1 이상이면 n과 함수에 n-1을 넣어 반한된 값을 곱함 
```

 <br>

:pencil2:**문제풀이 팁**

- 매개변수를 함수가 풀어야 하는 문제의 크기로 보면 이해가 쉽다.
- 재귀함수를 호출하면서 이런 문제의 크기가 점점 줄어들게 된다.
- 점점 줄어들게 되어 종료조건으로 수렴하게 되어 함수가 종료된다.  

<br>

<br>
