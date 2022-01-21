# function_map()

## 목차

1. [정의](#정의)
2. [활용 예시](#활용-예시)
	[int()](#int())
	[.split()](#.split())
	[.join()](#.join())



## map() 정의

```python
map(fuction, iterable)


#직접 만들어보면
def map_function(func, items):
    result = []
    for item in items:
        result.append(func(item))
    return result
```

- map은 **함수**와 **순회가능한 자료형**을 입력으로 받는다.
- 입력받은 자료형의 모든 요소에 fuction을 수행한 결과를 묶어서 돌려준다.
  즉, 순회가능한 자료형을 하나씩 꺼내 함수를 수행한 결과를 반환한다. 
- 그러나, 여기서 주의해야할 점은 **map함수의 반환 값은  map 객체이기 때문에** **`list`나 `tuple`형으로 반환시켜야 합니다.**

<br>

## 활용 예시 

### int()

> int(): 숫자나 문자열을 정수형 (Integer)으로 변환해 주는 내장 함수. 
>

- int()는 리스트와 튜플과 같은 자료형을 인수로 받지 못한다. 

- 그러나 map을 사용하면 편하게 인자들을 정수로 변환할 수 있다. 

```python
val_a = ['1', '2', '3', '4', '5']
val_b = map(int, val_a)

print(list(val_b)) # map의 반환값은 map객체이기에 list나 tuple로 반환해야 한다. 
      

# 결과
[1, 2, 3, 4, 5]
```

<br>

### .split()

> `문자열.split(sep=’구분자’, maxsplit=분할횟수)` 
>
> str클래스의 내부 함수로 특정문자를 기준으로 문자열을 분리시킨다. 

```python
# 기본: 띄워쓰기, 엔터 등을 인식해서 문자열을 분리.
문자열.split()


# 특정 구분자를 지정해서 문자열을 분리.
문자열.split('구분자')


# 정해진 분할 횟수에 따라 특정 구분자를 지정해서 문자열을 분리한다.
문자열.split('구분자', 분할횟수)
문자열.split(sep=’구분자’, maxsplit=분할횟수)
```

<br>

```python
# 입력 값을 변수 두 개에 저장하기
# 알고리즘 문제 풀이 때 자주 사용된다.

a, b = input('숫자 두 개를 입력하시오: ').split() #지정된 구분자가 없기 때문에 입력받은 값을 띄어쓰기로 구분
print( a, b,type(a), type(b) )


#실행
숫자 두 개를 입력하시오: 20 30
    
# 출력 
20, 30, <class 'str'>, <class 'str'> 
```

<br>

- **map을 사용하면 input()값을 일괄적으로 형 변환할 수 있다.** 

```python
a, b = map (int, input('숫자 두 개를 입력하시오: ').split())
print( a, b, type(a), type(b) )


#실행
숫자 두 개를 입력하시오: 20 3
    
# 출력 
20, 30, <class 'int'>, <class 'int'>
```

<br>

### .join()

> `'구분자'.join(list)`
>
> 매개변수로 반환된 리스트에 있는 요소를 모두 합쳐서 하나의 문자열로 반환하는 함수

```python
val = ['1', '2', '3', '4']

a = ''.join(val) # 구분자가 없음.
b = ',\n'.join(val) # 구분자는  ,\n

print(a, type(a))
print(b, type(b))



#출력
1234 <class 'str'>
1,
2,
3,
4 <class 'str'>
```

<br>

- **list에 저장된 값이 문자여야 한다.**
- **list의 인자가 정수나 실수 map()활용해 형을 변환시켜야 한다.** 

 ```python
 val = [1, 2, 3, 4, 5]
 
 a = (''.join(map(str, val)))
 
 print(a, type(a))
 
 
 #출력 
 12345 <class 'str'>
 ```

<br>

<br>
