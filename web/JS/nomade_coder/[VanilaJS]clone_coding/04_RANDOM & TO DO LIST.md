# RANDOM & TO DO LIST

## 1. RANDOM

### 1) Quotes 

```html
<!DOCTYPE html>
<html lang="en">
...
  <div id="quote">
...
</html>
```

```javascript
// 명언 Array
const quotes = [...
];

const quote = document.querySelector("#quote span:first-child");
const author = document.querySelector("#quote span:last-child");


// Math 모듈을 이용하여 랜덤으로 인덱스를 뽑아 quotes Array의 해당 원소에 접근하기 
// Math.random(): 0에서 1사이의 랜덤한 숫자를 제공 
// Math.random() * [number]: 0에서 number 사이의 랜덤한 숫자를 제공 (모든 실수)
// Math.round(): 인자로 받은 숫자를 반올림한다. 
// Math.ceil(): 인자로 받은 숫자를 올림한다.
// Math.floor(): 인자로 받은 숫자를 내림한다.  

// 인덱스는 정수이기 때문에 floor()를 사용한다. 
const todaysQuote = quotes[Math.floor(Math.random() *  quotes.length)]


// html에 적용
quote.innerText = todaysQuote.quote;
author.innerText = todaysQuote.author;
```

- math모듈을 활용하여 랜덤으로 숫자를 뽑는다. (숫자는 접근하고 싶은 배열의 인덱스 범위로 한정)
- Array에 랜덤으로 뽑은 숫자를 인덱스로 갖는 명언 객체를 변수에 저장한다. 
- html에 접근하여 해당 명언으로 내부 텍스트를 변경!

<br>

### 2) BackGround

```javascript
// 현재 img 폴더에 배경화면으로 사용할 이미지를 저장한 상태. 
// 배열의 원소로 배경화면으로 사용할 이미지파일의 이름갖는다.  
const images = [
  "00.jpg",
  "01.jpg",
  "02.jpg",
  "03.jpg",
  "04.jpg",
  "05.jpg",
];

// 랜덤으로 images배열의 원소를 변수에 저장한다.
const chosenImage = images[Math.floor(Math.random() *  images.length)]

//======================================================================
// 자바스크립트로 이미지를 html에 추가하기
// 자바스크립트에서 html태그를 생성하여 body 내부에 추가한다.
// 태그 생성
const bgImage = document.createElement("img");
bgImage.src = `img/${chosenImage}`;

// body 내부에 추가
document.body.appendChild(bgImage)
```

<br>

## 2. TO DO LIST

```html
<!DOCTYPE html>
<html lang="en">
...
  <!-- 유저가 To Do를 입력하기위한 form   -->
  <form id="todo-form">
    <input type="text" placeholder="Write a TO DO and Press Enter" required>
  </form>
    
  <!-- 유저가 입력한 To Do를 리스트로 생성 -->
  <ul id="todo-list"></ul>
...
</html>
```

<br>

### 1) Adding ToDos

```javascript
const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");

//const toDoInput = document.querySelector("#todo-form input");과 동일
const toDoInput = toDoForm.querySelector("input");


// todo list를 추가하는 함수
function paintToDo(newTodo){
  const li = document.createElement("li");
  const span = document.createElement("span");
  
  // span을 li의 자식 태그로 추가한다. 
  li.appendChild(span);

  // 함수 호출시 받은 인자를 텍스트로 추가한다. 
  span.innerText = newTodo;

  // html에 이미 존재하는 ul태그에 자바스크립트로 만든 li태그를 자식으로 추가한다.  
  toDoList.appendChild(li);
}


// 유저가 submit 이벤트를 수행할 시 호출하는 함수
function handleToDoSubmit(event){
  // submit이벤트가 발생해도 새로고침 X 
  event.preventDefault();

  const newTodo = toDoInput.value;
  
  // 제출하면 입력 값이 사라진다.
  // 이미 변수에 저장되어 있기때문에 지워도 상관 없다.  
  toDoInput.value = "";
  
  // todo list를 추가하는 함수 호출!
  // 사용자가 입력한 vaule(string)를 저장한 변수를 인자 
  paintToDo(newTodo);

}

toDoForm.addEventListener("submit", handleToDoSubmit);

```

- 유저가 to do를 form에 입력한 뒤 제출하면  **`이벤트 발생`**
-  유저가 입력한 value를 list로 생성하여 웹사이트에 노출시킨다.  **`웹 사이트에 반영`**

<br>

### 2) Deleting To Dos

> toDo를 삭제하는 buton을 추가한다. 
>
> 이 버튼은 click event를 기다리고 있다는 것을 명심!

```javascript
const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");

//===============================================================================
// todo list를 삭제 하는 함수 
function deleteToDo(event){
  // 이벤트에 대한 정보를 얻을 수 있기 때문에 어떤 버튼을 클릭했는지 확인할 수 있다. 
  // console.log(event.target.parentElement);
  const li = event.target.parentElement;
  li.remove();
}

// todo list를 추가할 때 삭제버튼도 추가한다. 
function paintToDo(newTodo){
  const li = document.createElement("li");
  const span = document.createElement("span");
  
  // 삭제를 위한 버튼 태그를 추가한다. 
  const button = document.createElement("button");
  
  span.innerText = newTodo;
  button.innerText = "❌";

  // 삭제버튼은 클릭하는 순간을 기다리고있다.. 
  button.addEventListener("click", deleteToDo);
  
  // 삭제버튼은 li의 자식태그!(마지막 자식)
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
//===============================================================================
 
function handleToDoSubmit(event){
  event.preventDefault();
  const newTodo = toDoInput.value;
  toDoInput.value = "";
  paintToDo(newTodo);
}

toDoForm.addEventListener("submit", handleToDoSubmit);
```

- JS에서 html내부에 button태그를 추가한다. 
- button.addEventListener("click", deleteToDo); 에서 클릭이 발생하면 deleteToDo함수가 실행된다.
- deleteToDo함수는 클릭이벤트가 발생한 버튼의 부모태그를 찾아서 삭제한다. (본인도 함께 삭제.. )

<br>

### 3) Saving To Dos

> 새로고침을 할때 마다 to do list는 삭제된다.
>
> localStorage를 활용하여 이를 저장하자. 

```javascript
const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");

//toDO를 제출할 때마다 입력한 text를 저장할 빈 array
const toDos = [];


// localStorage에 저장하는 함수 
function saveToDos(){
  // toDos arry의 내용을 localStorage에 넣는다.
  // 첫 번째 인자는 key, 두 번째 인자는 저장할 value 
  // JSON.stringify(): 자바스크립트 객체나 배열을 String으로 변환 
  localStorage.setItem("todos",  JSON.stringify(toDos))
}

function deleteToDo(event){
  const li = event.target.parentElement;
  li.remove();
}

function paintToDo(newTodo){
  const li = document.createElement("li");
  const span = document.createElement("span");
  const button = document.createElement("button");
  span.innerText = newTodo;
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}

function handleToDoSubmit(event){
  event.preventDefault();
  const newTodo = toDoInput.value; 
  toDoInput.value = "";
  
  // //toDO를 제출할 때마다 입력한 text를 array에 push한다.  
  toDos.push(newTodo);
  
  paintToDo(newTodo);
  
  // toDos arry의 내용을 localStorage에 넣는 함수를 호출한다. 
  saveToDos()

}

toDoForm.addEventListener("submit", handleToDoSubmit);

```

- `JSON.stringify()`을 사용하는 이유
  - 예시) `const toDos = [diet, dring water, study]`일 경우
  - 사용하지 않을 때, localStorage: `key= todos , value = diet, dring water, study`
  - 사용할 때, localStorate: `key= todos , value = ["diet", "dring water", "study"]`
    - `["diet", "dring water", "study"]`는 문자열이다.
  - **jason.parse()를 활용하면 `["diet", "dring water", "study"]`과 같이 생긴 문자열을 다시 array로 변환할 수 있다.** 

-  todo - list의 배열 생성 =>  저장 기능을 가진 함수를 정의 
- 아직 localStorage에 저장된 데이터가 화면에 보이지는 않는 상태이다. 

<br>

### 4) Loading To Dos

#### (1) localStorage에 저장된 value들을 array로 전환

> array는 인덱스를 통해 접근할 수 있기 때문에 string을 array로 바꾼다. 

```javascript
...
// 오타를 방지하기 위해 문자를 중복으로 사용하면 변수로 설정한다. 
const TODOS_KEY = 'todos';
const toDos = [];

... 

function sayHello(item){
  console.log("This is", item);
}

// local sttorage에 TODOS_KEY를 key로 가진 value를 변수에 저장
const savedToDos = localStorage.getItem(TODOS_KEY);

if(savedToDos != null){
  // Json.parse()를 활용하여 문자열을 array로 변환하여 저장한다. 
  const parsedToDos = JSON.parse(savedToDos);

  // array의 각각 원소들에 대해 함수를 실행시킨다.
  parsedToDos.forEach(sayHello);
}
```

- `array.forEach(function)`:배열의 원소를 차례대로 인자에 넣어 함수를 실행한다. 

  - arrow함수를 사용할 수 있다. 위의 상황처럼 함수를 추가로 정의할 필요가 없다. 

    ```javascript
    const savedToDos = localStorage.getItem(TODOS_KEY);
    
    if(savedToDos != null){
      const parsedToDos = JSON.parse(savedToDos);
      parsedToDos.forEach((item) => console.log("This is", item));
    }
    ```

<br>

#### (2) 웹사이트 시각화

```javascript
const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");
const TODOS_KEY = 'todos';
const toDos = [];

function saveToDos(){
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos))
}


function deleteToDo(event){
  const li = event.target.parentElement;
  li.remove();
}


function paintToDo(newTodo){
  const li = document.createElement("li");
  const span = document.createElement("span");
  const button = document.createElement("button");
  span.innerText = newTodo;
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}


function handleToDoSubmit(event){
  event.preventDefault();
  const newTodo = toDoInput.value; 
  toDoInput.value = "";
  toDos.push(newTodo);
  paintToDo(newTodo);
  saveToDos()

}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);

if(savedToDos != null){
  const parsedToDos = JSON.parse(savedToDos);
  parsedToDos.forEach(paintToDo);
}
```

- `parsedToDos.forEach(paintToDo)`을 함으로써  localStorage에 자동으로 저장된 value를 리스트로 생성할 수 있다!

<br>

그러나, 아직 저장이 불완전하다. 새로 고침을 한 후 새로 toDo를 추가하면 localStorage 의  value가 초기화되고 

새로 저장하는 value들을 localStorage에  저장한다. 즉, 이전 데이터가 사라진다!

**원인은 `const toDos = [];`코드 때문이다. application이 시작될 때 toDos array는 항상 비어있기 때문이다.** 

<br>

#### (3) toDo Load

```javascript
const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");
const TODOS_KEY = 'todos';

// 새로 고침할때 이전에 저장되어 있던 원소가 배열에 그대로 남아 있어야 한다. 
// 업데이트가 가능한 변수로 수정
let toDos = [];

function saveToDos(){
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos))
}


function deleteToDo(event){
  const li = event.target.parentElement;
  li.remove();
}


function paintToDo(newTodo){
  const li = document.createElement("li");
  const span = document.createElement("span");
  const button = document.createElement("button");
  span.innerText = newTodo;
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}


function handleToDoSubmit(event){
  event.preventDefault();
  const newTodo = toDoInput.value; 
  toDoInput.value = "";
  toDos.push(newTodo);
  paintToDo(newTodo);
  saveToDos()

}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);

if(savedToDos != null){
  const parsedToDos = JSON.parse(savedToDos);
  
  // 먼저 toDos array에 이전에 저장되어 있던 원소들을 저장한다.
  // 사용자가 새로운 toDo를 제출하기 전에는 localStorage에 이전의 value가 남아 있기 때문에 웹사이트가 로드되자마자 이를 미리 저장한다.  
  toDos = parsedToDos;
  
  parsedToDos.forEach(paintToDo);
}

```

<br>

### 5) Deletign To Dos

> toDO를 삭제할 때 마다 localStorage를 업데이트 해야 한다. 

#### (1) localStorage의 value를 객체의 array로 만든다. 

>  어떤 toDo를 데이터베이스에서 지워야 하는지 모르기 때문에 id속성을 부여한다. 

`예시` [chicken, pizza] ========> [{id:1212, text:chicken}, {id:2323, text:pizza}]  

```javascript
...

// 이제 text가 아닌 object를 인자로 받기 때문에 수정해야 한다. 
function paintToDo(newTodo){
  const li = document.createElement("li");
  
  // id 추가 (유저가 어떤 아이디를 지우기를 원하는지 알려주어야 한다.)
  li.id = newTodo.id;

  const span = document.createElement("span");
  const button = document.createElement("button");
  
  // 수정
  span.innerText = newTodo.text;

  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}

function handleToDoSubmit(event){
  event.preventDefault();
  const newTodo = toDoInput.value; 
  
  // 이제 object를 push할 것이다. 
  const newTodoObj = {
    text: newTodo,
    id: Date.now(),
  };

  toDoInput.value = "";
  
  // toDos.push(newTodoO);
  // paintToDo(newTodo);
  // 위의 코드를 다음과 같이 수정
  toDos.push(newTodoObj);
  paintToDo(newTodoObj);
  saveToDos()
}
...
```

<br>

#### (2) Delete!

> filter()를 활용하여 삭제할 원소를 제외하고 새로운 배열을 만든다. 

```javascript
const toDoForm = document.getElementById("todo-form");
const toDoList = document.getElementById("todo-list");
const toDoInput = toDoForm.querySelector("input");
const TODOS_KEY = 'todos';
let toDos = [];

function saveToDos(){
  localStorage.setItem(TODOS_KEY, JSON.stringify(toDos))
}


function deleteToDo(event){
  const li = event.target.parentElement;
  li.remove();
  
  // 삭제를 클릭한 li의 id를 갖고 있는 toDo를 지운다. 
  // 클릭한 li.id와 다른 toDo는 배열에 남겨둔다. 
  // toDo.id는 number, li.id는 string이기때문에 변환을 해야 한다. 
  // DOM의 id는 문자열이다. 
  toDos = toDos.filter((toDo) => toDo.id !== parseInt(li.id));

  //toDos DB에서 todo를 지운 뒤에 saveToDos 호출
  saveToDos()
  
}

function paintToDo(newTodo){
  const li = document.createElement("li");
  li.id = newTodo.id;
  const span = document.createElement("span");
  const button = document.createElement("button");
  
  span.innerText = newTodo.text;
  button.innerText = "❌";
  button.addEventListener("click", deleteToDo);
  li.appendChild(span);
  li.appendChild(button);
  toDoList.appendChild(li);
}


function handleToDoSubmit(event){
  event.preventDefault();
  
  const newTodo = toDoInput.value; 
  const newTodoObj = {
    text: newTodo,
    id: Date.now(),
  };

  toDoInput.value = "";
  toDos.push(newTodoObj);
  paintToDo(newTodoObj);
  saveToDos()
}

toDoForm.addEventListener("submit", handleToDoSubmit);

const savedToDos = localStorage.getItem(TODOS_KEY);

if(savedToDos != null){
  const parsedToDos = JSON.parse(savedToDos);
  toDos = parsedToDos;
  parsedToDos.forEach(paintToDo);
}
```

**:speech_balloon:`array.filter(function)`**

주어진 함수의 테스트를 통과하는(True 값을 반환하는) 모든 요소를 모아 새로운 배열로 반환한다. 

즉, array의 item을 유지하고 싶으면 True를 리턴해야 한다. 

```javascript
const arr = ["pizza", "banana", "tomato"]
function sexyFilter(food){return food !== "banana"}
arr.filter(sexyFilter) // ['pizza', 'tomato']
```

```javascript
const arr = [1234, 5656, 454, 343, 12, 4646, 405] 
function sexyFilter(num){return num <= 1000}
arr.filter(sexyFilter) // [454, 343, 12, 405]
```

<br>