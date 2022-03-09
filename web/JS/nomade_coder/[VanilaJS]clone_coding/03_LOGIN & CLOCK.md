# LOGIN & CLOCK

## 1. 유저 데이터 받기 (LOGIN)

### 1) input

> js에는 정보를 기억하는 아주 간단한 방법이 있다. 
>
> 하지만 모든 것은 html에서 시작된다. 우선, html을 작성한 후 , element를 js로 끌고 온다.

#### (1) 유저가 입력하는 값의 유효성 확인

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
  <div id="login-form">
    <input type="text" placeholder="What is your name?">
    <button>Log In</button>
  </div>
  <script src="app.js"></script>  
</body>
</html>
```

```javascript
const loginInput = document.querySelector("#login-form input");
const loginButton = document.querySelector("#login-form button");


// 유저가 입력하는 값의 유효성을 확인하기 => 하지만 이는 html 속성만으로도 충분히 가능하다!
function btnClick(){
  const username = loginInput.value;
  if (username === ""){
    alert("Please Write your name" )
  } else if (username.length > 15 ){
    alert("Your name is too long.")
  }
};

function btnClick(){
  const username = loginInput.value;
  console.log(username);
}

loginButton.addEventListener("click", btnClick)

```

<br>

#### (2) HTML의 도움을 받기 (추천! :fire:)

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
  <form id="login-form">
    <input 
      required
      maxlength="15"
      type="text" 
      placeholder="What is your name?">
      
    <!-- <input type="submit" value="Log In"> -->
    <!-- 버튼을 누르면 form이 submit된다. -->
    <!-- 더 이상 클릭에 신경쓰지 않아도 된다. submit에 신경을 쓰면 된다.  -->
    <button>Log In</button>
  </form>
  <script src="app.js"></script>  
</body>
</html>
```

- `input`속성을 활용하여 더 쉽게 유저가 입력하는 값의 유효성을 검토할 수 있다. 
- `<button>Log In</button>`, `<input type="submit" value="Log In">`
  - 과 같은 버튼 을 누르면 form이 자동으로 submit된다. 
  - 그래서 우리는 이제 `button`의 클릭여부 말고 form의 `submit`에 관심을 갖게 된다. 

<br>

#### (3) preventDefault();

```javascript
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");

const link = document.querySelector("a");

function onLoginSubmit(event){
  // preventDefault(): 브라우저의 기본 동작이 발생되지 않도록 막는다.
  event.preventDefault();
  console.log(event);
}

function handleLinkClick(event){
  event.preventDefault();
  console.dir(event);
}


// 지정된 이벤트가 발생하면 브라우저는 우선 onLoginSumit 함수를 호출한다.
// 브라우저가 함수를 실행시키기 하지만 정보를 주기도 한다. 
loginForm.addEventListener("submit", onLoginSubmit);
link.addEventListener("click", handleLinkClick);
```

- 웹 브라우저의 기본 행동
  - submit 태그의  경우 웹브라우저가 자동적으로 홈페이지를 새로고침한다. 
  - a태그의 경우 웹브라우저가 자동으로 페이지를 이동시킨다. 

- **이런 경우,  이벤트에 대한 정보를 보기 힘들다 !!**

원래는  event object에 대한 자리만 할당해주면 해당 이벤트가 발생시킨 정보들에 대한 정보를 볼 수 있다. 

그런데 위의 경우는 해당 이벤트가 가진 웹브라우저의 기본 행동을 막기 위해 `preventDefault()`함수를 활용해야 한다.  

- 모든 event object는 `preventDefault()`함수를 기본적으로 갖고 있다.
- `preventDefault()` 함수는 EventListener 함수의 첫 번째 argument 안에 있는 함수이다.
- 이 arument는 지금 막 벌어진 event들에 대한 정보를 갖고 있고 기본 정보들을 제공한다.

<br>

### 2) form 

#### (1) Getting Username

```css
.hidden {
  display: none;
}
```

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
  <form id="login-form">
    <input 
      required
      maxlength="15"
      type="text" 
      placeholder="What is your name?">
    <button>Log In</button>
  </form>
  <h1 class="hidden" id="greeting"></h1>
  <script src="app.js"></script>  
</body>
</html>
```

- h1태그를 hidden 클래스가 있는 상태로 만든다. 

```javascript
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

// 일반적으로 string만 포함된 변수는 대문자로 표기한다.
// string을 저장하고 싶을 때 사용한다.
const HIDDEN_CLASSNAME = "hidden"

function onLoginSubmit(event){
  event.preventDefault();
  const username = loginInput.value;
  loginForm.classList.add(HIDDEN_CLASSNAME);
  // "Hello " + username;
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME)
}

loginForm.addEventListener("submit", onLoginSubmit);
```

- 유저가 이름을 제출하면, 웹 브라우저의 기본동작을 막는다. (새로고침)
- form 태그에 hidden 클래스가 추가된다. 
- 입력한 값을 변수 `username`에 저장한다. 
- h1태그에 텍스트를 추가한다. `Hello ${username}`
- h1 태그에 hidden 클래스를 제거한다. 

<br>

#### (2) Saving Username

:pencil2:공식 문서: https://developer.mozilla.org/ko/docs/Web/API/Window/localStorage

```javascript
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden"

function onLoginSubmit(event){
  event.preventDefault();
  const username = loginInput.value;

  // localStorage.setItem(key, value) : key를 갖는 value를 로컬저장소에 저장한다. 
  // 크롬 개발자도구 -애플리케이션-로컬 스토리지에서 확인이 가능하다. 
  // 새로 고침을해도 데이터는 여전히 저장되어 있다. 
  localStorage.setItem("username", username)

  loginForm.classList.add(HIDDEN_CLASSNAME);
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME)
}

loginForm.addEventListener("submit", onLoginSubmit);
```

새로고침을 하면, `localStorage`에는 유저의 정보가 남아 있지만form 창이 다시 보이고 h1태그가 안보이게 된다. 

**내가 원하는 것은 `localStorage`에 유저 정보가 있으면 새로고침을 해도 form을 보여주지 않고 h1태그를 보여주는 것이다.** 

<br>

#### (3) Loading Username

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
  <form class="hidden" id="login-form">
    <input 
      required
      maxlength="15"
      type="text" 
      placeholder="What is your name?">
    <button>Log In</button>
  </form>
  <h1 class="hidden" id="greeting"></h1>
  <script src="app.js"></script>  
</body>
</html>
```

```javascript
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden"
// string 오타는 발견하기 힘들기 때문에 2번 이상 사용된다면 꼭 변수로 정의해서 사용하자!
const USERNAME_KEY = "username"

function onLoginSubmit(event){
  event.preventDefault();
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  loginForm.classList.add(HIDDEN_CLASSNAME);
  paintGreeting(username);
}

// 중복제거를 위한 함수 정의
function paintGreeting(username){
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if(savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
}else { 
  paintGreeting(savedUsername);
```

<br>

```javascript
const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const HIDDEN_CLASSNAME = "hidden"
const USERNAME_KEY = "username"

function onLoginSubmit(event){
  event.preventDefault();
  const username = loginInput.value;
  localStorage.setItem(USERNAME_KEY, username);
  loginForm.classList.add(HIDDEN_CLASSNAME);
  paintGreeting();
}

function paintGreeting(){
  const username = localStorage.getItem(USERNAME_KEY);
  greeting.innerText = `Hello ${username}`;
  greeting.classList.remove(HIDDEN_CLASSNAME);
}

const savedUsername = localStorage.getItem(USERNAME_KEY);

if(savedUsername === null) {
  loginForm.classList.remove(HIDDEN_CLASSNAME);
  loginForm.addEventListener("submit", onLoginSubmit);
}else { 
  paintGreeting(s);
}
```

- 이렇게 할 수도 있지만, `localStorage`를 두 번이나 확인한다는 단점이 있다. 
- 그래서 니코쌤은 전자를 사용!

<br>

## 2. CLOCK

### 1) Intervals

> '매번'일어나야 하는 무언가를 뜻한다.

```html
<!DOCTYPE html>
<html lang="en">
...
  <h2 id="clock">00:00</h2>
...
</html>
```

```javascript
const clock = document.querySelector("h2#clock");

function sayHello(){
  console.log("hello");
}

// setInterval(): 첫번째 인자로 실행하고자 하는 함수, 두번째 인자로 호출되는 함수가 실행되는 간격(ms)를 받는다. 
setInterval(sayHello, 5000)
```

- `setInterval()`: 첫번째 인자로 실행하고자 하는 함수, 두번째 인자로 호출되는 함수가 실행되는 간격(ms)를 받는다.
- 5초마다 콘솔에 hello가 찍히는 것을 확인할 수 있다. 

<br>

### 2) Timeout

> 일정시간이 지난 후에 실행 

```javascript
const clock = document.querySelector("h2#clock");

function sayHello(){
  console.log("hello");
}

// setTimeout(): 첫번째 인자로 실행하고자 하는 함수, 두번째 인자로 실행 전에 대기하는 시간(ms)을 받는다. 
setTimeout(sayhello, 5000)
```

- ` setTimeout()`: 첫번째 인자로 실행하고자 하는 함수, 두번째 인자로 실행 전에 대기하는 시간(ms)을 받는다. 

<br>

### 3) DateObject

:pencil2:참고자료: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Date

```javascript
const clock = document.querySelector("h2#clock");

// 함수가 호출되면 새로운 Date object를 만든다. 
// new Date object는 현재 날짜, 시간, 분, 초에 대한 정보를 가지고 있다. 
// setInterval(getClock,1000)에 의해 object를 매 초마다 새로 create!
function getClock() {
  const date = new Date();
  clock.innerText = (`${date.getHours()}:${date.getMinutes()}:${date.getSeconds()}`);
}

// 웹사이트가 로드되자마자 시작하기위해 함수를 직접 호출
getClock()

// 1초마다 함수를 호출한다. 
setInterval(getClock,1000);
```

- new 를 선두에 쓰고 생성자 함수를 호출하면 instance object를 반환!
  - 즉, 변수 date는 Date객체의 인스턴스(객체)!

<br>

### 4) PadStart()

> 시계를 좀 더 보기 좋게 하기위해 수정! 

```javascript
// string에 사용하는 함수이다.
// PadStart(): 첫번쨰 인자로 최소 글자 수, 두번째 인자로 글자 수가 미달할 경우 앞에 추가할 문자를 받는다.   
PadStart(2, "0")

// 글자 수가 미달할 경우, 뒤에 문자를 추가
PadEnd(2, "0")
```

```javascript
const clock = document.querySelector("h2#clock");

function getClock() {
  const date = new Date();

  //padStart()를 사용하기 위해 문자로 전환
  const hours = String(date.getHours()).padStart(2, "0");
  const minutes = String(date.getMinutes()).padStart(2, "0");
  const seconds = String(date.getSeconds()).padStart(2, "0");
  clock.innerText = (`${hours}:${minutes}:${seconds}`);
}

getClock()
setInterval(getClock,1000);

```

<br>