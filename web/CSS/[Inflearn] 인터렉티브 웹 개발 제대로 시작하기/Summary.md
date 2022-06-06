# 인터렉티브 웹 개발 시작하기

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
  - 일반적으로 컨테이너에 주는 속성 (3d 무대)
  - 요소에 `tranform: perspective`를 줄 수 있지만, 컨테이너에 주는 것과 효과가 다르다. 
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

