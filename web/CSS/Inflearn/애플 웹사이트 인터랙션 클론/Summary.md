# Summary

## 1. 섹션2 스크롤을 이용한 인터랙션 구현

### 1) 스크롤 섹션 데이터 저장 

 #### (1) 스크롤 구간 설명

예제의 경우, 총 4개의 스크롤 구간으로 나누어져있다. 해당 구간에 대한 정보를 저장하는 배열을 만들어서 기록한다.  

각 구간은 다음과 같은 데이터를 가지고 있다. 

| 데이터       | 설명                                                         |
| ------------ | ------------------------------------------------------------ |
| type         | 어떤 스크롤 애니메이션을 구현하는가. 이에 따라 스크롤 섹션의 scrollHeight를 구하는 방법이 달라진다. |
| heightNum    | scrollHeight를 세팅하기 위한 수치. 예시) heightNum: 5 일 경우, 브라우저의 높이 5배로 scrollHeight를 세팅한다는 의미가 된다. |
| scrollHeight | 계산된 scrollHeight.                                         |
| objs         | 변화가 발생하는 DOM 객체                                     |
| values       | 변화가 발생하는 CSS요소                                      |

<br>

#### (2) 구현

```javascript
const sceneInfo = [
    {
      // 0
      type: "sticky",
      heightNum: 5,    // 브라우저 높이의 5배로 scrollHeight를 세팅할 것이다.
      scrollHeight: 0, // 후에, scrollHeight를 계산하여 저장한다. 
      objs: {
        container: document.querySelector("#scroll-section-0"),
        messageA: document.querySelector("#scroll-section-0 .main-message.a"),
        messageB: document.querySelector("#scroll-section-0 .main-message.b"),
        messageC: document.querySelector("#scroll-section-0 .main-message.c"),
        messageD: document.querySelector("#scroll-section-0 .main-message.d"),
      },
      values: {
        messageA_opacity_in: [0, 1, {start: 0.1, end: 0.2}], // 투명도: [시작 값, 끝나는 값, {애니메이션이 재생되는 구간}]
        messageA_opacity_out: [1, 0, {start: 0.25, end: 0.3}], 
        messageA_translateY_in: [20, 0, {start: 0.1, end: 0.2}], // translate: [시작 값, 끝나는 값, {애니메이션이 재생되는 구간}]
        messageA_translateY_out: [0, -20, {start: 0.25, end: 0.3}],
      },
    },
    //... 생략
```

<br>

### 2) scroll-section의 높이를 세팅한다. 

#### (1) SetLayout()함수 

> ScrollHeight 세팅한다. 

```javascript
function setLayout() {
  for (let i = 0 ; i < sceneInfo.length; i++) {
    if (sceneInfo[i].type === "sticky"){
      sceneInfo[i].scrollHeight = sceneInfo[i].heightNum * window.innerHeight;
    } else if (sceneInfo[i].type === "normal") {
      sceneInfo[i].scrollHeight = sceneInfo[i].objs.container.offsetHeight;
    }

    // CSS 속성의 값을 변경함으로, DOM에 반영한다. 
    sceneInfo[i].objs.container.style.height = `${sceneInfo[i].scrollHeight}px`
  }
}
```

- `type`이 sticky이면 스크롤 애니메이션이 발생하기 때문에, 현재 브라우저의 높이의 heightNum배 만큼 늘린다. 
- `type`이 normal이면 스크롤 애니메이션이 발생하지 않기 때문에, 콘텐츠의 높이를 그대로 사용한다. 
- **CSS 속성의 `height`값을 변경한다. => DOM에 반영!**

<br>

#### (2) setLayOut()함수를 이벤트와 바인딩한다.

```javascript
window.addEventListener("load", setLayout);
window.addEventListener("resize", setLayout);
```

- load되거나 브라우저 창 크기를 변경할 때, 함수를 실행한다. 
- `load`이벤트와 `DomContentLoaded`이벤트의 차이점은 다음과 같다. 
  - `load`: DOM 객체 이외에도 이미지와 같은 미디어 파일이 로드되면 실행된다. 
  - `DOMContentLoaded`: DOM 객체가 로드되면 실행된다. 

<br>

### 3) 현재 활성화된 scroll-section이 어디인지 확인한다.
#### (1) scroll할 때마다 scroll-section을 체크하는 함수를 실행한다. 

```javascript
let yOffset = 0;           // window.scrollY를 저장하는 변수
let prevScrollHeight = 0;  // 현재 스크롤 위치(yOffset)보다 이전에 위치한 스크롤 섹션들의 스크롤 높이의 합
let currentScene = 0;      // 현재 활성화된 scene (scroll-section)
let enterNewScene = false; // 새로운 scene이 시작된 순간 true가 되는 변수

window.addEventListener("scroll", () => {
  yOffset = window.scrollY
  scrollLoop();
});
```

<br>


#### (2) scrollLoop() 함수

> 현재 스크롤 하는 곳이 몇번째 section인지 확인한다. (현재 활성시킬 scene을 결정한다.)

```javascript
function scrollLoop(){
  enterNewScene = false;
  prevScrollHeight = 0;
  for (let i = 0 ; i < currentScene; i++) {
    prevScrollHeight += sceneInfo[i].scrollHeight;
  };
  
  // 활성화된 section을 찾는다.
  if (yOffset > prevScrollHeight + sceneInfo[currentScene].scrollHeight) {
    enterNewScene = true;
    currentScene++;
    document.body.setAttribute("id", `show-scene-${currentScene}`);
  };
  
  if (yOffset < prevScrollHeight) {
    if (currentScene === 0 ) return; // 브라우저 바운스 효과로 인해 마이너스가 되는 것 방지 (모바일)
    enterNewScene = true;
    currentScene--;
    document.body.setAttribute("id", `show-scene-${currentScene}`);
  };
    
 // 4) 활성화된 section에 맞는 애니메이션을 구현한다. 
  if (enterNewScene) return;  // 씬이 바뀌는 순간에는 이상한 값이 들어가기 때문에 playAnimation을 막는다. 
  playAnimation(); 
};
```

- `prevScrollHeight`: 현재 활성화된 section을 토대로 이전 스크롤 높이를 계산하여 저장한다. 
- 현재 스크롤 높이가 이전 섹션 높이 + 현재 섹션 높이의 한보다 크면 다음 섹션으로 넘어간다는 의미이다.
- 현재 스크롤 높이가 이전 섹션높이보다 작으면 이전 섹션으로 돌아갔다는 의미이다. 
  - 현재 활성화된 섹션이 0이면 이전 섹션으로 돌아갈 수 없기 때문에 제한을 둔다.

- 활성화된 section을 표시하기 위해 body태그에 id로 기록한다. => 이를 기반으로 CSS처리

   ```css
    /* 스크롤 깊이에 따라 바디에 id값이 부여된다. 해당 영역의 고정된 요소만 보이게된다.*/
    body#show-scene-0 #scroll-section-0 .sticky-elem,
    body#show-scene-1 #scroll-section-1 .sticky-elem,
    body#show-scene-2 #scroll-section-2 .sticky-elem,
    body#show-scene-3 #scroll-section-3 .sticky-elem {
      display: block;
    }
   ```

<br>

#### (3) SetLayOut()함수 수정

```javascript
function setLayout() {
  // 각 스크롤 세션의 높이를 세팅한다.
  for (let i = 0 ; i < sceneInfo.length; i++) {
    if (sceneInfo[i].type === "sticky"){
      sceneInfo[i].scrollHeight = sceneInfo[i].heightNum * window.innerHeight;
    } else if (sceneInfo[i].type === "normal") {
      sceneInfo[i].scrollHeight = sceneInfo[i].objs.container.offsetHeight;
    }
    sceneInfo[i].objs.container.style.height = `${sceneInfo[i].scrollHeight}px`
  }

  // currentScene (현재 활성 씬 반영하기)
  let totalScrollHeight = 0;
  yOffset = window.scrollY;
  for (let i = 0; i <sceneInfo.length; i++) {
    totalScrollHeight += sceneInfo[i].scrollHeight;
    if (totalScrollHeight >= yOffset) {
      currentScene = i;
      break;
    };
  };
    // 현재 활성 씬에 따라 body의 id태그가 달라진다. 
    document.body.setAttribute("id", `show-scene-${currentScene}`);
};
```

- 현재 활성 씬은 스크롤 하지 않아도 해당 페이지를 도달하면 찾아내야 하기 때문에 setLayOut()함수에 관련 코드를 추가한다. 

<br>

### 4) scroll-sections에 맞는 애니메이션을 구현한다.

#### (1) playAnimation 함수

```javascript
function playAnimation(){
  const objs = sceneInfo[currentScene].objs;
  const values = sceneInfo[currentScene].values;
  const currentYOffset = yOffset - prevScrollHeight;        // 현재 section에서 얼마나 스크롤 되었는지 기록하는 변수
  const scrollHeight = sceneInfo[currentScene].scrollHeight // 현재 section의 스크롤 높이
  const scrollRatio =  currentYOffset / scrollHeight        // 현재 section에서 몇%로 스크롤 되었는지 계산

  switch (currentScene) {
    case 0 :
      if (scrollRatio <= 0.22) {
        // fadeIn
        const messageA_opacity_in = calcValues(values.messageA_opacity_in, currentYOffset);
        const messageA_translateY_in = calcValues(values.messageA_translateY_in, currentYOffset);
        objs.messageA.style.opacity = messageA_opacity_in;
        objs.messageA.style.transform = `translateY(${messageA_translateY_in}%)`
      } else {
        // fadeOut
        const messageA_opacity_out = calcValues(values.messageA_opacity_out, currentYOffset);
        const messageA_translateY_out = calcValues(values.messageA_translateY_out, currentYOffset);
        objs.messageA.style.opacity = messageA_opacity_out;
        objs.messageA.style.transform = `translateY(${messageA_translateY_out}%)`
      };

      break;
          
    case 1:
      //..이하 생략
  };
};
```

- 디자인 계획
  - 해당 section의 10%만큼 scroll하면, 20%가 될때까지 fadeIn한다. 
  - 해당 section의 25%만큼 scroll하면, 25%가 될때까지 fadeOut한다. 
  - 22% 이하이면 fadeIn, 그 외에는 fadeOut효과를 적용한다.
- `calcValues`함수를 통해 값을 계산한다.

<br>

#### (2) calcValues()함수

```javascript
function calcValues(values, currentYOffset){   // value:변경할 요소, currentYOffset: 각 세션에서 얼마만큼의 스크롤 되었는가
  let rv;

  const scrollHeight = sceneInfo[currentScene].scrollHeight;
  const scrollRatio = currentYOffset / scrollHeight;

  // 스크롤 범위에 맞춰 효과를 반영한다.  예시) 스크롤 될 수록 투명도가 0 => 1로 변한다. 
  if ( values.length === 3){
    // start ~ end 사이에 애니메이션 실행
    const partScrollStart = values[2].start * scrollHeight;
    const partScrollEnd = values[2].end * scrollHeight;
    const partScrollHeight = partScrollEnd - partScrollStart;
    if ( currentYOffset >= partScrollStart && currentYOffset <= partScrollEnd){
      rv = (currentYOffset - partScrollStart) / partScrollHeight  * (values[1] - values[0]) + values[0];
    } else if ( currentYOffset  < partScrollStart){  
      rv = values[0];
    } else if (currentYOffset > partScrollEnd) {
      rv = values[1];
    }
  } else {
    rv = scrollRatio * (values[1] - values[0]) + values[0];
  }
  return rv;
}
```

- start~end범위가 지정되어 있는 경우,
  - 해당 범위에만 적용하기 위해 , 범위의 시작점, 종료지점, scrollHeigh를 계산한다 (`partScrollStart`,  `partScrollEnd`,`partScrollHeight`) 
  - partScrollStart <= 현재 스크롤 한 높이 <= partEndScrollEnd일 경우 값을 계산한다.  (범위 안에 있는 경우)
    - 범위기준 스크롤 비율(`(currentYOffset - partScrollStart) / partScrollHeight`)으로 값을 계산한다. 
  - partScrollStart보다 스크롤 높이가 작을 경우, 시작 값으로 설정한다.
  - partScrollEnd보다 스크롤 높이가 클 경우, 종료 값으로 설정한다. 
- 범위가 없는 경우, 
  - 전체 section에 적용된다고 가정. 전체 section을 기준으로 값을 계산한다. 

<br>
