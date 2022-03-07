# WELCOME TO JAVASCRIPT

## 1. JS 데이터

> 브라우저는 HTML을 열고, HTML은 CSS와 자바스크립트를 불러온다. 

### 1) Connect

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <link rel="stylesheet" href="style.css">
  <title>Momentum</title>
</head>
<body>
  <script src="app.js"></script>  
</body>
</html>
```

<br>

### 2) Variables

#### (1) `const`

> constant(상수)라는 의미로 값이 바뀔 수 없다는 의미를 갖는다. (값을 업데이트 할 수 없다)
> 기본적인 변수형.

```javascript
// 변수 만들기
const a = 5;
const b = 2;
const veryLongVariableName = 'jk'; 

console.log(a + b);
console.log(a * b);
console.log(a / b);
```

- 자바스크립트에서는 공백이 필요할 경우 대문자로 수정한다. 
  - 자바스크립트:  `veryLongVariableName`
  - 파이썬: `very_long_variable_name`

<br>

```javascript
// const 변수는 업데이트 할 수 없다. 
const a = 5;
const b = 2;
const myName = 'jk'; 

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log(myName);


// 새로운 값을 할당할 수 없기때문에 에러가 발생한다. 
myName = 'jkp'; 
console.log(myName);
```

<br>

#### (2) `let`

> 새로운 것을 생성할 때 사용하는 키워드로 업데이트 할 수 있는 변수를 생성한다. 
> 변수가 업데이트가 필요할 때 사용!

```javascript
// 변수 만들기
const a = 5;
const b = 2;
let myName = 'jk'; 

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log(myName);


// 변수 업데이트 (let은 생성할 때만 사용하는 키워드이다. )
myName = 'jkp'; 
console.log(myName);
```

- `const`, `let`  둘의 사용의도가 다르기 때문에 코드를 쉽게 파악할 수 있다. 

<br>

#### (3) `var`

> 과거부터 존재했던 자바스크립트 변수
> 원한다면 어디서든 업데이트 할 수 있다. 

- 언어를 보호 받지 못한다는 단점이 있기 때문에 `const`, `let` 이 등장하게 되었다. 
- `var`은 `const`, `let` 처럼 구분할 수 없다. 

```javascript
// 변수 var
var a = 5;
var b = 2;
var myName = 'jk'; 

console.log(a + b);
console.log(a * b);
console.log(a / b);
console.log(myName);

myName = 'jkp'; 
console.log(myName);
```

<br>

### 3) Booleans

```javascript
const amITall = true;
const amISmall = false;

// null: '아무것도 없음'을 의미 => 비어있기보다는 아무 것도 없는 상태로 채워진 것 
// 변수 안에 어떤 값이 없다는 것을 확실하게 하기 위해 작성하는 것! 의도적인 비어있는 상태
const amIFat = null;  

// undefined: 변수는 존재하는데 정의가 되지 않음
// 즉, 컴퓨터 메모리안에 변수는 있지만 값이 저장되어 있지 않은 상태이다
let something;

console.log(amITall);
console.log(amISmall);
console.log(amIFat);     // null
console.log(something);  // undefined
```

<br>

### 4) Arrays

> 데이터를 정리하기 위함
>
> 하나의 변수안에 데이터의 리스트를 저장한다. 

```javascript
const daysOfWeek = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat'];

// 항목 받아오기
console.log(daysOfWeek[4]);

// 항목 추가
daysOfWeek.push('sun');
```

<br>

### 5) Objects

> 데이터를 정리 하기 위함  
>
> 배열과 가장 큰 차이점은 각 데이터에 속성을 부여하여 데이터에 대한 추가 설명이 가능하다. 

```javascript
const playerName = 'jk';
const playerPoint = 1212;
const playerHandsome = true;
const playerFat = 'littile bit';

// 배열을 사용한다면. 리스트의 각 항목이 무슨 의미인지 알 수가 없다. 
const player =['jk', 1212, true, 'little bit'];

// 객체 활용하기
// 속성: 값
const player2 = {
  name:'jk',
  point: 1212,
  handsome: true,
};

console.log(player2);
console.log(player2.name);
console.log(player2['point']);

// const인 대상은 객체인 player2 이기 때문에 속성을 추가 하거나 업데이트 할 수 있다. 
player2.handsome = false;
console.log(player2);   // {name: 'jk', point: 1212, handsome: false}

player2.lastName = 'Park';
console.log(player2)   // {name: 'jk', point: 1212, handsome: false, lastName: 'Park'}

player2.point = player2.point + 15;
console.log(player2.point)   // 1227
```

<br>

##  2. JS 함수

> 코드의 반복을 줄이기 위함 
>
> 어떤 코드를 캡슐화해서, 실행을 여러 번 할 수있게 도와준다.

### 1) 함수 기본

```javascript
// console.log('hello my name is jk')
// console.log('hello my name is da1')
// console.log('hello my name is chicken')
// console.log('hello my name is pizza')

function sayHello(nameOfPerson, age){
  // 여기에 기입되는 것이 sayHello을 실행할때 마다 실행되는 코드이다. 
  console.log('Hello my name is '+ nameOfPerson + ' and I am ' + age);
}

sayHello('jk', 10);  // Hello my name is jk and I am 10
sayHello('dal', 23);  // Hello my name is dal and I am 23
sayHello('chicken', 21);  // Hello my name is chicken and I am 21
sayHello('pizza', 2);  // Hello my name is pizza and I am 2
sayHello();  // Hello my name is undefined and I am undefined
```

<br>

### 2) 메서드 

```javascript
//객체 함수 (메서드)
const player = {
  name:'jk',
  sayHello: function(otherPersonsName){
    console.log('Hello! ' + otherPersonsName + ' nice to meet you');
  },
}

console.log(player.name);  // jk
player.sayHello('chicken'); // Hello! chicken nice to meet you
```

- `otherPersonsName`는 함수 body에서만 접근 할 수 있다. 밖에서 접근 불가능!

<br>

### 3) Returns

> 일반적으로 함수는 어떤일을 수행하고 우리는 그 결과를 받는다. 

```javascript
const age = 96;

// 이 함수를 작동시키면서 console에 표시하는 것을 원하는 것이 아니다.
// 한국 나이로 계산된 결과를 코드로 받기를 원한다
function calculateKrAge(ageOfForeigner){
  return ageOfForeigner + 2;
}

//calculateKrAge(age)가 리턴값으로 변경되어 krAge에 리턴 값을 할당한다. 
const krAge = calculateKrAge(age);
console.log(krAge);  // 	98
```

- 어떤 작업을 처리하고 그 결과를 return하기 위해 함수를 사용하는 경우가 종종 있다. 
- `return`이 함수가 외부와 소통하는 방법이다. 
  - 함수를 다른 함수의 인자로 전달할 수 있다. 
- `return`을 하면, 함수의 작동은 멈추고 결과 값을 `return`하고 끝나버린다.

<br>

## 3. JS 조건문

### 1) 조건문 기본

```javascript
// prompt()는 사용자에게 창을 뛰울 수 있도록 해준다. 
// 사용자가 입력한 값이 prompt()의 반환 값이다. 
const age = prompt('How old are you?');
console.log(age);  // 121212

// typeof : value의 타입을 보는 키워드 
console.log(typeof age);  // string


//parseInt(): string을 int로 타입을 변경
console.log(parseInt(age));  //121212
console.log(typeof parseInt(age));  // number
```

-  `parseInt(age)`가 number가 아니라면 메시지를 띄워보자.

```javascript
const age = parseInt(prompt('How old are you?'));

// isNaN(): number인지 아닌지 boolean으로 알려준다. 
// NaN: Not a Number
if(isNaN(age)){
  console.log('숫자를 입력하시오');
} else{
  console.log('감사합니다!');
}
```

<br>

#### (1) 조건문 기본형태

```javascript
if(condition){
  // condition === true
} else {
  // condition == false
}
```

<br>

### 2) 조건문 활용

```javascript
const age = parseInt(prompt('How old are you?'));

if(isNaN(age) || age < 0){
  console.log('나이를 입력하시오');
} else if(age < 18){
  console.log('미성년자!');
} else if(age >= 18 && age <= 50){
  console.log('음주 가능!');
} else  {
  console.log('음주 불가능!');
}
```

- `&&`는 and 연산자이다.

- `||`는 or 연산자이다. 

- **비교연산자**

  ​	`===`,  `!==`, `<` , `>`,  `<=`,  `>=` 

- `else`는 선택사항이다.

<br>
