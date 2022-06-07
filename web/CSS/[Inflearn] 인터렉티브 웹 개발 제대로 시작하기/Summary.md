# 인터렉티브 웹 개발 시작하기

[toc]

## 1. Transform 

- 기준점을 자유자재로 바꿀 수 있다.
- 하드웨어 가속을 사용해서 성능이 굉장히 좋다.

```css
.box:hover {
    /* transform: scale(2) rotate(15deg); */
    /* transform: skewY(-30deg); */
    /* transform: translate(30px, 10px); */
    /* transform: translateY(-30px); */
    transform: scale(1.5);
    /* transform-origin: right bottom; */
    transform-origin: 50% 100%;
    background-color: crimson;
}
```

<br>

### 1) transform

> [공식문서](https://developer.mozilla.org/ko/docs/Web/CSS/transform)

| 속성      | 설명                                                      | 예시                             |
| --------- | --------------------------------------------------------- | -------------------------------- |
| scale     | 크기 조정<br />scaleX, scaleY, scaleZ                     | tranform: scale(2)               |
| skew      | 비틀기<br />skewX, skewY                                  | transform: skew(20deg, 30deg)    |
| rotate    | 회전<br />rotage3d, rotateX, rotateY, rotateZ             | transform: rotate(180deg)        |
| translate | 이동<br />translate3d, translateX, translateY, translateZ | transform: translate(30px, 10px) |

<br>

### 2) transform-origin

> 기준점 변경 [공식문서](https://developer.mozilla.org/en-US/docs/Web/CSS/transform-origin)

- 방향 ex) `transform-origin: right bottom;`
- 값   ex) `transform-origin: 50% 100%;`

<br>

### 3) transition

> 값이 변할 때, 중간과정에 애니메이션으로 바꿔준다. 
>
> transform에만 적용되는 것이 아니라 width, font-size, background컬러의 값이 변할 때 등과 같이 값(숫자)가 변할 때 적용 된다. 
>
> [공식문서](https://developer.mozilla.org/ko/docs/Web/CSS/transition)

```css
.box {
    /* 만약, width: auto면 transition은 적용이 안된다. (숫자로된 값이 아니기 때문이다.) */
    width: 100px;
    height: 100px;
    border: 2px solid black;
    background-color: rgba(255, 255, 0, 0.7);
    transition: 1s 2s cubic-bezier(0.25, 0.1, 0.49, 1.73);
}
```
<br>

- `transition-property`:transition을 적용시킬 속성을 정한다.
- `transition-duration`: 애니메이션이 완료되는 데 걸리는 시간을 설정한다.
- `transition-timing-function`:  transition의 진행 속도를 결정한다. 
- `transition-delay`: transition될 속성이 transition 요청을 받은 이후 실제로 transition하기까지 기다려야하는 시간을 설정한다.

| ![image-20220606230311643](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220606230311643.png) | <img src="https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220606230324645.png"> |
| :----------------------------------------------------------: | :----------------------------------------------------------: |



<br>

## 2. Animation

- 애니메이션이 transition과 다른 점은 키프레임을 추가할 수 있는 것이다. 
- 변화가 있는 지점을 keyFrame이라고 한다. 시작부터 끝날때까지 keyFrame을 줄 수 있다.
- [공식문서](https://developer.mozilla.org/ko/docs/Web/CSS/CSS_Animations/Using_CSS_animations)

```css
    @keyframes sample-ani {
      0% {
        transform: translate(0, 0);
      }
      50% {
        transform: translate(500px, 0);
        background-color: crimson;
      }
      100% {
        transform: translate(700px, 500px);
      }
    }
    .box {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 100px;
      height: 100px;
      border: 2px solid #000;
      background-color: #fff000;
      /* animation: 생성한 애니메이션 이름, 재생시간, 가속도, 반복, 디렉션, 필모드, 플레이 스테이트 등 */
      animation: sample-ani 3s linear forwards;
    }
    /* 호버하는 순간 멈춘다. */
    .box:hover {
      animation-play-state: paused;
    }
```

<br>

- `animation-duration`: 한 싸이클의 애니메이션이 얼마에 걸쳐 일어날지 지정합니다.
- `animation-timing-function`: 중간 상태들의 전환을 어떤 시간간격으로 진행할지 지정합니다.
- `animation-delay`: element가 로드되고 나서 언제 애니메이션이 시작될지 지정합니다.
- `animation-direction`: 애니메이션이 종료되고 다시 처음부터 시작할지 역방향으로 진행할지 지정합니다.
  - nomal, reverse, alternate, alternate-reverse
- `animation-fill-mode`: 애니메이션이 시작되기 전이나 끝나고 난 후 어떤 값이 적용될지 지정합니다.
  - none 
  - forwards: 마지막 keyframe에 의해 설정된 계산된 값을 유지한다. 
  - backwards: 대상에 적용되는 즉시 첫 번째 관련 keyframe에 정의 된 값을 적용하고 animation-delay기간 동안 이 값을 유지한다.
  - both:  애니메이션 속성이 양방향으로 확장된다.
- `animation-play-state`: 애니메이션을 멈추거나 다시 시작할 수 있습니다.
  - runnint, paused
- `animation-iteration-count`: 애니메이션이 몇 번 반복될지 지정합니다. `infinite`로 지정하여 무한히 반복할 수 있습니다.

| ![image-20220606231509928](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220606231509928.png) | ![image-20220606231541536](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220606231541536.png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: |

<br>

## 3. 3D

- `perspective`: 원근법을 주는 속성 
  - 일반적으로 컨테이너에 주는 속성 (3d 무대) => 시점에 따라 요소에 대한 효과가 조금 다르게 보인다.
  - 요소에 `tranform: perspective`를 줄 수 있다. => 요소마다 똑같이 효과가 적용된다.  
- `transform-style: preserve-3d`: 자식들 또한 3d공간에 배치하기 위한 속성

<br>

## 4. JS

DOM SCRIPT (Document Object Model)

- html element를 객체(object)로 보고 자바스크립트로 제어한다.
- 시각적으로 보이는 인터스페이스를 제어하는 것이기 때문에, DOM Script를 제어한다.

<br>

### 1) 이벤트 위임

> 부모에게 이벤트를 위임한다. 모든 요소에 이벤트를 주면 요소가 많아질 수로 성능이 떨어지기때문이다.

```js
(function () {
    const stage = document.querySelector(".stage");
    // classList.contains("클래스 이름"): 클래스 이름을 갖고 있는지 true, false 값을 반환한다.
    function clickHandler(event) {
        if (event.target.classList.contains("ilbuni")) {
            stage.removeChild(event.target);
        }
    }
    stage.addEventListener("click", clickHandler);
})();
```

<br>

### 2) 이벤트 핸들러

- 하나의 이벤트 핸들러에 모든 것을 다 처리 하는 것은 좋지 않다. 
- 구체적인 기능은 따로 함수를 만들고 이벤트 핸들러에서는 해당 함수를 호출해서 사용한다. 

```html
<script>
    // 여러개 중 하나만 활성화 하기 패턴.
    (function () {
    const stageElem = document.querySelector(".stage");

    //현재 활성화된 아이템을 저장하는 변수
    // const currentItem = document.querySelector(".door-opened");
    let currentItem = null;

    // 클릭한게 문이면, 문 열기
    function activate(elem) {
        elem.classList.add("door-opened");
        currentItem = elem;
    }

    // 열려있는 문이 있으면, 닫기
    function inactivate(elem) {
        elem.classList.remove("door-opened");
    }

    function doorHandler(event) {
        const targetElem = event.target;
        if (currentItem) {
            inactivate(currentItem);
        }
        if (targetElem.classList.contains("door-body")) {
            activate(targetElem.parentNode);
        }
    }
    stageElem.addEventListener("click", doorHandler);
})();
</script>
```

<br>

### 3) 객체

```javascript
// 생성자 (constructor)함수
function Person(nickname, age){
    this.nickname = nickname;
    this.age = age;
}

// 공통 메서드 생성
// 메모리 효율이 더 좋다. 
// 객체마다 똑같이 공유하는 메서드나 속성은 prototype 객체에 정리를 하면 된다. 
Person.prototype.introduce = function(){
    console.log(`안녕하세요? 저는 ${this.nickname}입니다.`)
}

// 인스턴스 (instance) 생성
const person1 = new Person('일분이', 10);
const person2 = new Person('이분이', 8);
```

<br>

- 객체를 html로 반영하기

```javascript
function Card(num, color) {
    this.num = num;
    this.color = color;
    this.init();
}

// 아예 prototype 객체를 다시 만들 때는 constructor 속성을 넣어주어야 한다.
Card.prototype = {
    constructor: Card,
    init: function () {
        const mainElem = document.createElement("div");
        mainElem.style.color = this.color;
        mainElem.innerText = this.num;
        mainElem.classList.add("card");
        document.body.appendChild(mainElem);
    },
};

const card1 = new Card(1, "green");
const card2 = new Card(7, "blue");
```

<br>

| ![image-20220607181737109](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607181737109.png) | ![image-20220607181635958](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607181635958.png) |
| :----------------------------------------------------------: | :----------------------------------------------------------: |

<br>

### 4) 스크롤 이벤트

```html
<script>
  (function () {
    const outputElem = document.querySelector(".output");
    const ilbuniElem = document.querySelector(".ilbuni");
    function showValue() {
      // window.pageYOffset: 스크롤을 얼마나 했는지 px로 나타내는 속성이다.
      // offsetTop: 요소의 처음 위치를 가져온다. => 고정된 값
      // window.innerHeight: 현재 브라우저의 높이
      // getBoundingClientRect(): 요소의 크기와 위치에 대한 정보를 갖고 있는 객체를 반환하는 메서드이다.
      let posY = ilbuniElem.getBoundingClientRect().top;
      outputElem.innerText = posY;

      if (posY < window.innerHeight * 0.2) {
        ilbuniElem.classList.add("zoom");
      } else {
        ilbuniElem.classList.remove("zoom");
      }
    }

    window.addEventListener("scroll", function () {
      showValue();
    });
  })();
</script>
```

- `getBoundingClientRect()`
	| ![image-20220607185243300](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607185243300.png) |
  | ------------------------------------------------------------ |



<br>

### 5) transition 이벤트 

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      .ball {
        position: absolute;
        left: 0;
        top: 0;
        width: 30px;
        height: 30px;
        /* margin: -15px 0 0 -15px; */
        border-radius: 50%;
        background-color: crimson;
        transition: 1s;
      }
      .ball.end {
        background: dodgerblue;
      }
    </style>
  </head>
  <body>
    <div class="ball"></div>
    <script>
      const ballElem = document.querySelector(".ball");
      // mouse event의 event.clientX, event.clientY는 발생한 좌표를 의미한다.(브라우저 창 왼쪽 꼭대기 기준 좌표)
      window.addEventListener("click", function (event) {
        console.log(event.clientX, event.clientY);
        ballElem.style.transform = `translate(
          ${event.clientX - 15}px, ${event.clientY - 15}px
          )`;
      });

      // transitionstart: transition이 시작하면 발생하는 이벤트
      // transitionend: transition이 끝나면 발생하는 이벤트
      ballElem.addEventListener("transitionend", function (event) {
        ballElem.classList.add("end");

        // transitionEvent.elapsedTime: transition duration타임
        console.log(event.elapsedTime);

        // transitionEvent.propertyName: transition 전환과 관련한 css 속성의 이름
        console.log(event.propertyName);
      });
    </script>
  </body>
</html>

```

- 마우스 클릭한 좌표로 공이 이동하지 않는 이유

  - 바디자체에 마진이 있어서 

    => 바디 마진을 제거한다. 

    => ball 속성을 `position: absolute`, `top: 0` , `left:0`으로 수정한다.

  - 클릭한 곳이 중간이 되도록 이동하지 않는다. (클릭한 곳이 왼쪽 상단이 되도록 이동함)  

    => 볼 자체에 너비와 높이만큼 마이너스 마진을 준다 

    => 이동할때 볼 너비와 높이만큼 마이너스하여 이동한다.

- transitionEvent

  | ![image-20220607190839783](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607190839783.png) | ![image-20220607190915101](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607190915101.png) |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |

<br>

### 6) 애니메이션 이벤트

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>
      @keyframes ball-ani {
        from {
          transform: translate(0, 0);
        }
        to {
          transform: translate(200px, 200px);
        }
      }
      .ball {
        position: absolute;
        left: 0;
        top: 0;
        width: 30px;
        height: 30px;
        border-radius: 50%;
        background-color: crimson;
        /* animation: ball-ani 1s 3 alternate forwards; */
      }
      .ball.end {
        border: 5px solid dodgerblue;
      }
    </style>
  </head>
  <body>
    <div class="ball"></div>
    <script>
      const ballElem = document.querySelector(".ball");
      ballElem.addEventListener("click", function () {
        ballElem.style.animation = "ball-ani 1s 3 alternate forwards";
      });

      // animationstart: 애니메이션이시작할때 발생하는 이벤트
      // animationend: 애니메이션이 끝날 때 발생하는 이벤트
      ballElem.addEventListener("animationend", function (event) {
        ballElem.classList.add("end");
        console.log(event);
      });

      // animationiteration: 애니메이션이 반복이 될 때 발생하는 이벤트 (처음에는 x)
      ballElem.addEventListener("animationiteration", function (event) {
        console.log(event);
      });
    </script>
  </body>
</html>

```

- animationEvent

  | ![image-20220607192205008](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607192205008.png) | ![image-20220607192232316](https://raw.githubusercontent.com/JaeKP/image_repo/main/img/image-20220607192232316.png) |
  | ------------------------------------------------------------ | ------------------------------------------------------------ |

<br>

### 7) 타이밍

#### (1) setTimeout

```javascript
// 첫 번째 매개변수: 함수, 두 번째 매개변수: 시간(ms)
setTimeout(function(){
    console.log('setTimeout!')
}, 1000)
```

- 1000ms 즉, 1초 후에 이 함수가 실행된다. 
- 내가 원하는 시간만큼 지연시킬 때, 사용한다.

<br>

```javascript
let timeId;

function sample(){
    console.log('sample!');
}

// setTimeout은 숫자를 반환한다.처음에는 1을 반환하며 반복하여 실행할 수록 숫자가 1증가한다. 
timeId = setTimeout(sample, 3000);
console.log(timeid)

// clearTimeout으로 취소할 수 있다. 
// 3초가 되기 전(setTimeout이 실행되기 전)에 clear를 함으로 setTimeout이 취소된다. 
clearTimeout(timeId);
```

<br>

#### (2) setInterval

```javascript
let timeId;
const btn = document.querySelector(".btn");
function sample(){
    console.log('sample!');
}

// 첫번째 매개변수: 함수, 두 번째 매개변수: 시간 (ms)
timeId = setInterval(sample, 1000);

// clearInterval로 취소할 수 있다. 
btn.addEventListener("click", function(){
    clearInterval(timeId)
});
```

- 1000ms에 한번 씩 함수를 실행한다. 

<br>

#### (3) requestAnimationFrame

- setInterval의 단점을 개선!
- [공식문서](https://developer.mozilla.org/ko/docs/Web/API/Window/requestAnimationFrame)

```html
<script>
  let timeId;
  let n = 0;
  const btn = document.querySelector(".btn");

  function sample() {
    n++;
    console.log(n);

    // return 하면 requestAnimationFrame을 실행하지 않기 때문에 반복을 종료한다.
    if (n > 200) {
      return;
    }

    // 초당 60번 반복을 목표로 빠르게 반복한다.
    timeId = requestAnimationFrame(sample);
  }

  sample();

  // cancleAnimationFrame:
  btn.addEventListener("click", function () {
    cancelAnimationFrame(timeId);
  });
</script>
```

<br>
