# [제어문]continue_break

## continue

> 이후 코드를 건너뛰고 반복문을 계속 실행한다. 

```python
total = 0                                        # 합을 누적해 저장할 정수형 변수                           

for n in range(1,101):                           # 1~100까지의 정수를 차례대로 변수 n에 대입
    if n % 5  == 0:                              # n의 값이 5의 배수인지 검사하기 위해 나머지 연산자 사용
        continue                                 # n의 값이 5의 배수이면 나머지 코드는 무시하고 for 반복문으로 다시 이동한다.              
    total += n                                   # n의 값이 5의 배수가 아닐 때 변수 total에 값을 누적                                  


print(f'5의 배수를 제외한 총합: {total}')           # 4000 // 접근할 항목이 없을 경우 for문을 빠져나와 print()함수 호출 
```

<br>

```python
for word in 'mamamoo':                          # 'mamamoo'문자열을 차례대로 변수 word에 대입
    if word == 'm':                             # 문자열에 'm'이 있는지 검사하기 위해 관계 연산자 사용
        continue                                # word의 값이 'm'이면 나머지 코드는 무시하고 for 반복문으로 다시 이동한다.
    print(word)                                 # word의 값이 'm'이 아니면 출력한다. 
    
#출력
a
a
o
o
```

<br>

## break

> 반복문을 멈추고 빠져나간다. 

```python
num_list = []                 # 값을 저장할 비어있는 리스트 변수 

for n in range(1, 101):       # 1~100까지의 정수를 차례대로 변수 n에 대입
    if n * 2 > 50:            # 변수 n * 2이 50보다 큰지 확인인하기 위해 비교 연산자 사용
        break                 # 변수 n * 2이 50보다 크다면 바로 for 반복문을 이탈해서 print()문을 실행한다.
    num_list+= [n * 2]        # 변수 n * 2의 값을 빈 리스트에 저장

print(num_list)               # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
```

<br>

```python
word = 0                      # 변수 초기화    

while True:
    word = int(input('100을 나눌 값을 입력해주세요^_^ \n0이나 1을 입력하면 프로그램이 종료됩니다.'))
    if word == 0 or word == 1:                  
        break                            
    print(f'100을 {word}로 나눈 값은 {100/word}입니다.')
    
print('끝!')                 # word가 0 혹은 1과 같으면 while반복문을 이탈하여 print('끝!')을 실행한다.
```

<br>

