# JAVASCRIPT ON THE BROWSER

## 1. HTML in JavaScript

### 1) 크롬 개발자 도구 console

```javascript
// 크롬 개발자도구 console
// document를 통해 자바 스크립트로 HTML에 접근하고 변경할 수 있다. 
document                            // # document
document.body                      // <body>...</body>
document.getElementById("title")   // <h1 id="title">Grab me!</h1>
```

- document는 브라우저에 이미 존재하는 객체이며 자바스크립트 입장에서는 HTML을 가리키는 객체이다.
- JavaScript에서 HTML을 읽어올 뿐만 아니라, HTML을 변경 할 수도 있다.

<br>

### 2) JavaScript

> 자바스크립트로 HTML을 읽고 수정할 수 있다. 

### (1) 기본 개념

```javascript
const title = document.getElementById("title");
console.log(title);

// console.log() 보다 더 자세하게 element를 보여주는 함수
// 모든 것은 HTML에 표현되어 있는 것이다. 
console.dir(title);
```

<br>

```javascript
const title = document.getElementById("title");
console.dir(title);

//console.dir()를 통해 본 element을 이용해서 html을 마음껏 수정 할 수 있다. 
title.innerText = "Got you"; 
```

- document(객체)의 함수 중 하나인 `getElenemtById`를 통해 HTML에서 id를 불러올 수 있다. 
- 찾은 id를 통해 element를 찾는다.
- element를 찾은 다음엔 HTML을 얼마든지 수정할 수 있다. 😉

<br>

**이제부터 우리는 HTML에서 항목을 가지고 와서, JavaScript를 통해 항목들을 변경할 수 있다.** 

<br>

### (2) JavaScript에서 HTML을 가져오는 다른 방법

> HTML의 경우, 대부분의 경우는 id를 사용하지 않는다. 
>
> 보통 className을 사용하거나 둘 다 사용한다. 

📌 **클래스**

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
  <h1 class="hello">Grab me!</h1>
  <h1 class="hello">Grab me!</h1>
  <h1 class="hello">Grab me!</h1>
  <h1 class="hello">Grab me!</h1>
  <h1 class="hello">Grab me!</h1>
  <script src="app.js"></script>  
</body>
</html>
```

```javascript
const hellos = document.getElementsByClassName("hello");

// hellos는 현재 많은 h1이 담겨있는 array이다. 
console.log(hellos)
```

- 객체가 아니기때문에 `hellos.`을 못한다 ㅠㅠ 우리가 원하는 상태가 아님!

<br>

📌 **태그**

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
  <div class="hello">
    <h1>Grab me!</h1>
  </div>
  <script src="app.js"></script>  
</body>
</html>
```

```javascript
const title = document.getElementsByTagName("h1");

// title은 h1이 하나만 들어가 있는 array이다. 
console.log(title);  // HTMLCollection [h1]
```

- 객체가 아니기때문에 `title.`을 못한다 ㅠㅠ 우리가 원하는 상태가 아님!

<br>

📌 **가장 멋진 방법 ! `querySelector`, `querySelectorAll`**

```javascript
// querySelector는 element를 CSS방식으로 검색할 수 있다. 
const title = document.querySelector(".hello h1");

console.log(title);  // <h1>Grab me!</h1>
```

- 드디어!

- `querySelector`는 단 하나의 element를 return 한다.  **=> 여러 개일 경우 첫번째 element만 return!**

   ```javascript
   // 전자보다 후자의 방식이 더 좋다
   const title = document.getElementById("title");  
   const title = document.querySelector("#title");
   ```

  ```javascript
  // CSS 셀렉터를 통해 편하게 HTML element에 접근할 수 있다  
  const title = document.querySelectorAll("div.hello:first-child h1");
    
  console.log(title); 
    
  title.innerText = "Hello";
  ```

- `querySelectorAll`는 조건에 부합하는 모든 element를 return 한다.  **=> 이것 또한 array를 반환한다.**

<br>

### 3) Event

> 사용자가 웹페이지에서 하는 모든 상호작용은 event이다.
>
> 앞서 보았듯이, element의 내부를 보고 싶으면 `console.dir()`함수를 사용한다. 
> 이는 기본적으로 object로 표시한 element(전부 js object)를 보여주고  element 중 앞에 on이 붙은 것들은 event 보아도 무방하다. 

#### (1) Click Event

**우리는 이제부터 Click을 Listen한다.**

 ```javascript
 const title = document.querySelector("div.hello:first-child h1");
 
 function handleTitleClick(){
   console.log('타이틀은 클릭되었습니다!');
 }
 
 // addEventListener()는 말 그대로 event를 listen을 하는 것이다
 // 하지만 무슨 eveent를 listen하고 싶은지 알려주어야 한다
 // 첫번째 인자: listen하고 싶은 이벤트
 // 두번째 인자: 이벤트가 발생하면 실행되는 함수!
 title.addEventListener("click", handleTitleClick);
 ```

- 내가 직접 실행버튼을 누르지 않고, JavaScript에 이 함수 이름을 넘겨 주어서, 유저가  title을 click할 경우에 JavaScript가 나 대신 실행버튼을 눌러준다.
  - 그래서 `()`를 기입하지 않은 것! `()`는 함수를 실행하는 버튼과도 같기 때문이다. 
  - 즉, JS가 대신 실행해주는 것을 기다린다. 

<br>

#### (2) Mouse Event

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  console.log('타이틀은 클릭되었습니다!');
}

function handleMouseEnter(){
  title.innerText = '마우스는 여기있다!';
}

function handleMouseLeave(){
  title.innerText = '마우스는 떠났다!';
}

title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);
```

- 우린 직접적으로 무언가를 실행시키지 않았다. 
- **단지, JS에게 무엇을 할 지 알려주고, JS는 그것을 할 뿐!**

<br>

#### (3) More Event

:pencil2: 참고자료: https://developer.mozilla.org/ko/docs/Web/API/Window

:pencil2: 참고자료: https://developer.mozilla.org/ko/docs/Web/Events

<br>

- **event를 listne하는 다른 방법**

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  console.log('타이틀은 클릭되었습니다!');
}

function handleMouseEnter(){
  title.innerText = '마우스는 여기있다!';
}

function handleMouseLeave(){
  title.innerText = '마우스는 떠났다!';
}

title.onclick = handleTitleClick;
title.onmouseenter = handleMouseEnter;
title.onmouseleave = handleMouseLeave;
```

**`addEventListner`를 더 선호하는 이유는 `removeEventListner`로 이벤트를 쉽게 제거할 수 있기 때문이다.**

<br>

- **window 객체**

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  console.log('타이틀은 클릭되었습니다!');
}

function handleMouseEnter(){
  title.innerText = '마우스는 여기있다!';
}

function handleMouseLeave(){
  title.innerText = '마우스는 떠났다!';
}

// 기본적으로 document의 body 아래를 가져올 수 없다. 
function handleWindowResize(){
  document.body.style.backgroundColor = 'tomato';
}

title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);
title.addEventListener("resize", handleMouseLeave);

// document가 JS에서 기본적으로 제공되듯이, window도 기본적으로 제공한다.
window.addEventListener("resize", handleWindowResize);
```

**기본적으로 document의 body아래를 가져올 수 없다.** 

1. document의 `body`, `head`, `title`, 이런 것들은 중요하기 때문에 존재하는 것이다. 
2. **나머지 element는 `qeuryselector`sk `getElementById`등으로 찾아와야 한다.** 

<br>

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  console.log('타이틀은 클릭되었습니다!');
}

function handleMouseEnter(){
  title.innerText = '마우스는 여기있다!';
}

function handleMouseLeave(){
  title.innerText = '마우스는 떠났다!';
}

function handleWindowResize(){
  document.body.style.backgroundColor = 'tomato';
}

function handleWindowCopy(){
  alert("복사!");
}

title.addEventListener("click", handleTitleClick);
title.addEventListener("mouseenter", handleMouseEnter);
title.addEventListener("mouseleave", handleMouseLeave);
title.addEventListener("resize", handleMouseLeave);

window.addEventListener("resize", handleWindowResize);
window.addEventListener("copy", handleWindowCopy);
```

<br>

## 2. CSS in JavaScript

### 1) 조건문 활용

``` javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  if(title.style.color === "blue"){
    title.style.color = "tomato";
  } else {
    title.style.color = "blue";
  }
}


title.addEventListener("click", handleTitleClick);
```

 **하지만 이보다 우린 코드를 더 깔끔하게 만들 수 있다!**

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  // 변수 정의 (변수가 가지는 의미에 따라서 나눠서 선언)
  // '원래 어떤 색이었는지'과 '새로 적용해줘야 할 색'으로 나누는 것이 가독성이 좋다. 
  const currentColor = title.style.color; 
  let newColor;
  if(currentColor === "blue"){
    newColor = "tomato";
  } else {
    newColor = "blue";
  }
  title.style.color = newColor;
}

title.addEventListener("click", handleTitleClick);
```

1.  **event 발생 및 함수 실행**
2.  **`currentColor` 변수 선언 후 `title.style.color` 값 복사 (getter)**
3.  **`newColor` 변수 선언**
4.  **`currentColor` 현재 값 확인**
5.  **조건에 따라 `newColor`에 "tomato" or "blue" 값 대입**
6.  **마지막으로 `title.style.color`에 `newColor`값 대입 (setter)**

<br>

### 2) CSS

> 사실, style은 CSS에서 수정하는 것이 좋다. 
>
> CSS는 HTML을 바라보고 JS는 HTML을 수정한다. 

```css
body{
  background-color: beige;
}

h1 {
  color: cornflowerblue;
}

.active {
  color: tomato;
}
```

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  //getter 이자 setter이다 
  title.className = "active";
}

title.addEventListener("click", handleTitleClick);
```

**앞서 만들었던 프로그램과 똑같이 만든다면..**

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  if(title.className === "active"){
    title.className = "";
  } else {
    title.className = "active" 
  };
}

title.addEventListener("click", handleTitleClick);
```

<br>

#### (1) 위의 코드를 깔끔하게 만드는 방법 

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  const activeClass = "active";
  if(title.className === activeClass){
    title.className = "";
  } else {
    title.className = activeClass 
  };
}

title.addEventListener("click", handleTitleClick);
```

- CSS와 JS간 오타가 발생하는 경우가 많은데, 변수를 활용하여 오타 체크가 비교적 쉽다.

<br>

#### (2) 위의 코드를 깔끔하게 만드는 방법 2 (추천하는 방법)

> 앞서 사용했던 방법처럼 className을 수정해버린다면, 최초로 설정된 className이 사라진다. 

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  const activeClass = "active";
  if(title.classList.contains(activeClass)){
    title.classList.remove(activeClass);
  } else {
    title.classList.add(activeClass); 
  };
}

title.addEventListener("click", handleTitleClick);
```

- `className`: 이전 class들은 상관하지 않고 모든 것을 교체한다. 
- `classList`:  class들의 목록으로 클래스 추가, 제거와 같은 작업을 할 수 있도록 허용해준다. 

<br>

```javascript
const title = document.querySelector("div.hello:first-child h1");

function handleTitleClick(){
  // toggle()은 클래스 리스트에 해당하는 클래스가 있는지 확인하고 
  // 없으면 추가. 있으면 제거 한다. 
  title.classList.toggle("active");
}

title.addEventListener("click", handleTitleClick);
```

<br>
