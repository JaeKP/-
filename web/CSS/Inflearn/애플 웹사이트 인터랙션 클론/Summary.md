# Summary

## 1. 스크롤을 이용한 인터랙션 구현

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

## 2. 고해상도 비디오 인터렉션

### 1) 고화질 비디오 처리하기 

#### (1) 비디오 

```javascript
const videoElem = document.querySelector('.sample-video');
let progress;
let currentFrame;
function init() {
	document.body.classList.remove('before-load');

	window.addEventListener('scroll', function () {
       	// 전체 스크롤 비율:  현재 스크롤 한 길이 / 전체 스크롤 가동 범위
		progress = pageYOffset / (document.body.offsetHeight - window.innerHeight);
		if (progress < 0) progress = 0;
		if (progress > 1) progress = 1;

        // currentTime: 현재 재생시간, duration: 비디오 전체 재생시간
		videoElem.currentTime = videoElem.duration * progress;
	});
}

window.addEventListener('load', init);
```

- 현재 비디오 재생시간 =  비디오 전체 재생 시간 * 스크롤 비율 

<br>

#### (2) 이미지

```javascript
const imgElem = document.querySelector('.sample-img');
const videoImages = [];
let totalImagesCount = 960;
let progress;
let currentFrame;

function setImages() {
	for (let i = 0; i < totalImagesCount; i++) {
		let imgElem = new Image();
		imgElem.src = `../video/002/IMG_${7027 + i}.JPG`;
		videoImages.push(imgElem);
	}
}

function init() {
	document.body.classList.remove('before-load');

	window.addEventListener('scroll', function () {
		progress = pageYOffset / (document.body.offsetHeight - window.innerHeight);
		if (progress < 0) progress = 0;
		if (progress > 1) progress = 1;

		requestAnimationFrame(function () {
            // 이미지 인덱스는 0부터 959이기때문에 -1을 한다. 또한, 정수로 만들기 위해 반올림을 한다. 
			currentFrame = Math.round((totalImagesCount - 1) * progress); 
			imgElem.src = videoImages[currentFrame].src; // DOM에 반영
		});
	});
}

window.addEventListener('load', init);
setImages();
```

- 먼저 이미지객체를 사용하여 이미지를 배열에 저장한다. 
- 현재 프레임 (스크롤에 맞는 이미지의 인덱스) = 이미지 마지막 인덱스 * 스크롤 비율
  - 스크롤에 맞는 이미지의 인덱스는 정수여야 하기 때문에 반올림을 한다. 
- 이미지 태그의 속성에 현재 스크롤에 맞는 이미지를 넣는다.

<br>

`이미지 객체`

[공식문서](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image)

```javascript
new Image();
new Image(width);
new Image(width, height);

var myImage = new Image(100, 200);
myImage.src = 'picture.jpg';
document.body.appendChild(myImage); // <img width="100" height="200" src="picture.jpg">
```

<br>

#### (3) 캔버스

```javascript
const canvas = document.querySelector('.sample-canvas');
const context = canvas.getContext('2d');
const videoImages = [];
let totalImagesCount = 960;
let progress;
let currentFrame;

function setImages() {
	for (let i = 0; i < totalImagesCount; i++) {
		let imgElem = new Image();
		imgElem.src = `../video/002/IMG_${7027 + i}.JPG`;
		videoImages.push(imgElem);
	}
}

function init() {
	document.body.classList.remove('before-load');

	// 첫번째 이미지를 먼저 그려준다.
	context.drawImage(videoImages[0], 0, 0);

	window.addEventListener('scroll', function () {
		progress = pageYOffset / (document.body.offsetHeight - window.innerHeight);
		if (progress < 0) progress = 0;
		if (progress > 1) progress = 1;

		currentFrame = Math.round((totalImagesCount - 1) * progress);

		// drawImage(내가 그릴 이미지, x좌표, y좌표 ): 이미지를 캔버스에 그린다.
		context.drawImage(videoImages[currentFrame], 0, 0);
	});
}

window.addEventListener('load', init);
setImages();
```

- 먼저 이미지객체를 사용하여 이미지를 배열에 저장한다. 
- 현재 프레임 (스크롤에 맞는 이미지의 인덱스) = 이미지 마지막 인덱스 * 스크롤 비율
  - 스크롤에 맞는 이미지의 인덱스는 정수여야 하기 때문에 반올림을 한다. 
- 이미지를 캔버스에 그린다. (`canvas`[공식문서](https://developer.mozilla.org/ko/docs/Web/API/Canvas_API/Tutorial/Basic_usage))



<br>

### 2) 캔버스를 창 사이즈에 맞추기

#### (1)  sceneInfo배열에 이미지 관련 데이터 추가

```javascript
const sceneInfo = [
  {
    // 2 
    type: "sticky",
    heightNum: 5, 
    scrollHeight: 0,
    objs: {
      //생략
      canvas: document.querySelector("#video-canvas-0"),
      context: document.querySelector("#video-canvas-0").getContext('2d'),
      videoImages: [], // 이미지 배열
    },
    values: {
      // 생략
      videoImageCount : 300,
      imageSequence: [0, 299],
      canvas_opacity: [1, 0, {start: 0.9, end: 1}]
    }
  },
   // 생략
}
```

<br>

#### (2) setLayOut()수정

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

  document.body.setAttribute("id", `show-scene-${currentScene}`);


  // canvas 사이즈 맞추기
  const heightRatio = window.innerHeight / 1080;
  sceneInfo[0].objs.canvas.style.transform = `translate3d(-50%, -50%, 0) scale(${heightRatio})`;
};
```

- 캔버스를 화면에 꽉 맞게 만들기 위해 style의 tranform속성을 변화시킨다. (height를 꽉채워서 보여준다.)

- `height`를 fit 시킨다 => scale로 조정한다

  - `const heightRatio = window.innerHeihgt / 1080;` : 브라우저의 높이 / 원래 캔버스의 높이
  - 위의 비율에 맞춰 scale을 조정한다. 

- 가운데 정렬을 한다. 

  ```css
  .sticky-elem-canvas {
    height: 100%;
    top: 0;
  }
  
  .sticky-elem-canvas canvas {
    position: absolute;
    top: 50%;
    left: 50%;
  }
  ```

  화면을 꽉채우기 위해, scale을 조정하면 top: 0%, left: 0%를 해도 scale로 인해 크기가 조정되었기 때문에, 조정으로 인해 바뀐 요소가 위에 붙지 않는다.

  그래서 그냥 `top:50%`, `left: 50%`으로 밀어버리고 => translate로 다시 이동시킨다. 

<br>

 ### 3) 비디오 인터랙션 적용하기 

#### (1) 이미지 저장

```javascript
// 이미지 저장. 
function setCanvasImage(){
  let imgElem;
  for (let i = 0; i < sceneInfo[0].values.videoImageCount ; i++){
    imgElem = new Image();
    imgElem.src = `./video/001/IMG_${6726 + i}.JPG`;
    sceneInfo[0].objs.videoImages.push(imgElem);
  }
  // 생략
};
setCanvasImage();
```

- 이미지 객체를 통해 생성한 이미지를 배열에 저장한다. 
- 이미지는 배열의 인덱스를 통해 접근이 용이해진다. 

<br>

#### (2) 스크롤 애니메이션 구현: `playAnimation()`

```javascript
function playAnimation(){
  const objs = sceneInfo[currentScene].objs;
  const values = sceneInfo[currentScene].values;
  const currentYOffset = yOffset - prevScrollHeight;
  const scrollHeight = sceneInfo[currentScene].scrollHeight
  const scrollRatio =  currentYOffset / scrollHeight
  
  switch (currentScene) {
    case 0 :
      // canvas에 그린다. 
      let sequence = Math.round(calcValues(values.imageSequence, currentYOffset));
      objs.context.drawImage(objs.videoImages[sequence], 0, 0);

      // canvas 투명도
      objs.canvas.style.opacity = calcValues(values.canvas_opacity, currentYOffset);
  }
  // 생략
};
```

<br>

#### (3) 첫번째 이미지를 그린다. 

```javascript
// 첫번쨰 이미지를 그린다. 
 window.addEventListener("load", ()=> {
    setLayout();
    sceneInfo[0].objs.context.drawImage(sceneInfo[0].objs.videoImages[0], 0, 0);
  });
```

- 스크롤을 해야 그려지기 때문에, 스크롤 전에 첫번째 이미지를 그린다. 

<br>

## 3. 동적 위치와 크기 계산을 이용한 스크롤 인터랙션 구현

### 1) 블렌딩 캔버스 크기 계산

> 가로/ 세로 모두 꽉차게 하기 위해 크기를 계산한다. 
>
> 실제 브라우저 비율과 캔버스의 비율이 달라서 캔버스 사이즈를 억지로 fit시킨다. 

```javascript
function playAnimation(){
  const objs = sceneInfo[currentScene].objs;
  const values = sceneInfo[currentScene].values;
  const currentYOffset = yOffset - prevScrollHeight;
  const scrollHeight = sceneInfo[currentScene].scrollHeight
  const scrollRatio =  currentYOffset / scrollHeight  // 현재 scene에서 얼마나 스크롤 되었는가 / 현재 씬의 scrllHeight

  switch (currentScene) {
	// 생략
    case 3:
      const widthRatio = window.innerWidth / objs.canvas.width;
      const heightRatio = window.innerHeight / objs.canvas.height;
      let canvasScaleRatio;

      // 어느 비율이여도 화면을 full로 채우기 위함
      if (widthRatio <= heightRatio) {
        // 캔버스보다 브라우저 창이 홀쭉한 경우
        canvasScaleRatio = heightRatio;
      } else {
        // 캔버스보다 브라우저 창이 납작한 경우 
        canvasScaleRatio = widthRatio;
      };
      // DOM에 반영하기 
      objs.canvas.style.transform = `scale(${canvasScaleRatio})`;
          
      // 이미지 그려주기 
      objs.context.drawImage(objs.images[0], 0, 0);
      break;
  }
};
```

- 어떤 비율이여도 캔버스를 화면에 꽉 채우게 하기 위해, 조건문을 사용한다. 
  - `const widthRatio = window.innerWidth / objs.canvas.width;`  : 브라우저의 높이 / 원래 캔버스의 높이
  - `const heightRatio = window.innerHeight / objs.canvas.height;`  : 브라우저의 너비 / 원래 캔버스의 너비

- scale을 조정한다. (DOM에 반영)
- 첫번째 이미지를 그린다. 

<br> 

### 2) 좌우 흰색 영역 위치 및 크기 잡기 

```javascript
function playAnimation(){
  const objs = sceneInfo[currentScene].objs;
  const values = sceneInfo[currentScene].values;
  const currentYOffset = yOffset - prevScrollHeight;
  const scrollHeight = sceneInfo[currentScene].scrollHeight
  const scrollRatio =  currentYOffset / scrollHeight  // 현재 scene에서 얼마나 스크롤 되었는가 / 현재 씬의 scrllHeight

  switch (currentScene) {
	// 생략
    case 3:
      const widthRatio = window.innerWidth / objs.canvas.width;
      const heightRatio = window.innerHeight / objs.canvas.height;
      let canvasScaleRatio;

      // 캔버스 화면에 꽉 채우기 
      if (widthRatio <= heightRatio) {
        canvasScaleRatio = heightRatio;
      } else { 
        canvasScaleRatio = widthRatio;
      };
      objs.canvas.style.transform = `scale(${canvasScaleRatio})`;
          
      // 이미지 그려주기 
      objs.context.drawImage(objs.images[0], 0, 0);
          
      // 캔버스 사이즈에 맞춰 innerWidth와 innerHeight 비율 계산
      // 크롬의 경우, 스크롤바가 영역을 차지 하기 때문에, innerWidth에서 스크롤바를 제외한 폭을 구해야 한다.  
      // const recalculatedInnerWidth = window.innerWidth / canvasScaleRatio;
      const recalculatedInnerWidth = document.body.offsetWidth / canvasScaleRatio;
      const recalculatedInnerHeight = window.innerHeight / canvasScaleRatio; 
          
      // 하얀 박스의 너비
      const whiteRectWidth = recalculatedInnerWidth * 0.15;
      // 스크롤 애니메이션: 왼쪽박스 출발 X좌표 
      values.rect1X[0] = (objs.canvas.width - recalculatedInnerWidth) / 2;
      // 스크롤 애니메이션: 왼쪽박스 도착 X좌표
      values.rect1X[1] = values.rect1X[0] - whiteRectWidth;
      // 스크롤 애니메이션: 오른쪽박스 출발 X좌표
      values.rect2X[0] = values.rect1X[0] + recalculatedInnerWidth - whiteRectWidth;
      // 스크롤 애니메이션: 오른쪽박스 도착 X좌표
      values.rect2X[1] = values.rect2X[0] + whiteRectWidth; 

      // 좌우 흰색 박스 그리기: fillStyle, fillRect(x, y, 너비, 높이 )
      objs.context.fillStyle = "white";
      objs.context.fillRect(
          parseInt(calcValues(values.rect1X, currentYOffset)), 0, parseInt(whiteRectWidth), objs.canvas.height
      );
      objs.context.fillRect(
          parseInt(calcValues(values.rect2X, currentYOffset)), 0, parseInt(whiteRectWidth), objs.canvas.height
      );
      break;
  }
};
```
<br>

| <img src="https://raw.githubusercontent.com/JaeKP/image_repo/main/img/220615browser.png" alt="220615browser" style="zoom: 33%;" /> | 브라우저 화면 기준으로 캔버스 크기가 조정되어 있다<br />즉, 브라우저 창의 높이만큼 채우기 위해 일정 비율이 줄어들었다. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

- 그래서 새로운 캔버스의 사이즈를 구해야 한다. (검정 영역)
  - 앞서, 브라우저 화면과 캔버스의 비율이 달라서 캔버스를 브라우저 높이에 fit시켰다 
  - 그 결과, 양쪽에 네모를 그리고 싶은데 원래 캔버스 크기 기준으로 그리면 짤려보이기 때문에 캔버스가 줄어든 크기를 고려해서 innerWidth와 innerHight의 높이를 맞춘다. 

<br>

| <img src="https://raw.githubusercontent.com/JaeKP/image_repo/main/img/220615boxes.png" alt="220615boxes" style="zoom:33%;" /> | - 왼쪽 박스 출발 X 좌표: 검정 사각형 좌변 <br />- 왼쪽 박스 도착 X 좌표:  출발 좌표 - 박스 너비 <br />- 오른쪽 박스 출발 X 좌표: 검정 사각형 우변 <br />- 오른쪽 박스 도착 X좌표: 검정 사각형 우변 + 박스 너비 |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

<br>

#### 2) 좌우 흰색 영역 스크롤 애니메이션 처리 

#### (1) sceneInfo배열에 스크롤 애니메이션 관련 데이터 추가

```javascript
const sceneInfo = [
  {
     // 3
    type: "sticky",
    heightNum: 5, 
    scrollHeight: 0,
    objs: {
      container: document.querySelector('#scroll-section-3'),
      canvasCaption: document.querySelector('.canvas-caption'),
      canvas: document.querySelector(".image-blend-canvas"),
      context: document.querySelector(".image-blend-canvas").getContext('2d'),
      imagesPath : [
        "./images/blend-image-1.jpg",
        "./images/blend-image-2.jpg",
      ], 
      images: []
    },
    values: {
      rect1X: [0, 0, {start:0, end:0}],
      rect2X: [0, 0, {start:0, end:0}],
      rectStartY: 0 // 섹션 기준, 캔버스의 y위치 (브라우저 상단 부분과 캔버스와의 거리)
    }
  },
}
```

- `rectStartY`
  - 흰색 박스가 점점 사라지는 애니메이션이 진행된다. 캔버스가 상단에 닿는 타이밍에 박스가 아예 사라진다.
  - 스크롤 애니메이션 출발지점, 도착지점 설정하기 위해서는 섹션이 시작될때, 캔버스의 y위치를 구해야 한다. (브라우저 상단 부분과 캔버스와의 거리)

<br>

```javascript
function playAnimation(){
  const objs = sceneInfo[currentScene].objs;
  const values = sceneInfo[currentScene].values;
  const currentYOffset = yOffset - prevScrollHeight;
  const scrollHeight = sceneInfo[currentScene].scrollHeight
  const scrollRatio =  currentYOffset / scrollHeight  // 현재 scene에서 얼마나 스크롤 되었는가 / 현재 씬의 scrllHeight

  switch (currentScene) {
	// 생략
    case 3:
      const widthRatio = window.innerWidth / objs.canvas.width;
      const heightRatio = window.innerHeight / objs.canvas.height;
      let canvasScaleRatio;

      // 캔버스 화면에 꽉 채우기 
      if (widthRatio <= heightRatio) {
        canvasScaleRatio = heightRatio;
      } else { 
        canvasScaleRatio = widthRatio;
      };
      objs.canvas.style.transform = `scale(${canvasScaleRatio})`;
          
      // 이미지 그려주기 
      objs.context.drawImage(objs.images[0], 0, 0);
          
      // 캔버스 사이즈에 맞춰 innerWidth와 innerHeight 비율 계산
      const recalculatedInnerWidth = document.body.offsetWidth / canvasScaleRatio;
      const recalculatedInnerHeight = window.innerHeight / canvasScaleRatio; 
          
      // 하얀 박스의 너비
      const whiteRectWidth = recalculatedInnerWidth * 0.15;
      // 스크롤 애니메이션: 박스 좌표 계산
      values.rect1X[0] = (objs.canvas.width - recalculatedInnerWidth) / 2;
      values.rect1X[1] = values.rect1X[0] - whiteRectWidth;
      values.rect2X[0] = values.rect1X[0] + recalculatedInnerWidth - whiteRectWidth;
      values.rect2X[1] = values.rect2X[0] + whiteRectWidth; 
          
          
      // 스크롤 애니메이션 출발지점, 도착지점 설정
      // 흰색 박스가 점점 사라지는 애니메이션이 진행된다. 캔버스가 상단에 닿는 타이밍에 박스가 아예 사라진다.
      // 그래서 애니메이션이 시작될때, 캔버스의 y위치를 구해야 한다.
      
      // 처음에 0으로 설정했기때문에, 처음에만 값을 세팅하고 다시 실행하지 않는다. 
      if (!values.rectStartY){ 
          
        // offsetTop: 브라우저기준이 아니라 문서 기준이지만, 기준점을 바꿀 수 있다. 
        // 부모의 포지션이 static이 아니면 부모기준 offsetTop을 잡을 수 있다.
        // 그런데 현재, 캔버스가 scale이 조정이 되어있지만, transform으로 변형된 것을 고려하지 않는다.
        // scale이 조정된 후의 위치를 원한다. 그래서 scale이 조정된 비율만큼 다시 계산을 해야 한다.
        // 그 결과, (원래 캔버스 높이 - 조정된 캔버스 높이) /2 를 offsetTop에 더하면 된다.  
        values.rectStartY = objs.canvas.offsetTop + (objs.canvas.height - objs.canvas.height*canvasScaleRatio) / 2
        
        // start시점 구하기: 윈도우 높이의 절반!
        values.rect1X[2].start = (window.innerHeight / 2) / scrollHeight;
        values.rect2X[2].start = (window.innerHeight / 2) / scrollHeight;          
       
       // 애니메이션이 시작될때 캔버스와 브러우저 상단 사이의 거리 / 현재씬의 스크롤 높이         
       values.rect1X[2].end = values.rectStartY / scrollHeight; 
       values.rect2X[2].end = values.rectStartY / scrollHeight;
     };
        
      // 좌우 흰색 박스 그리기
      objs.context.fillStyle = "white";
      objs.context.fillRect(
          parseInt(calcValues(values.rect1X, currentYOffset)), 0, parseInt(whiteRectWidth), objs.canvas.height
      );
      objs.context.fillRect(
          parseInt(calcValues(values.rect2X, currentYOffset)), 0, parseInt(whiteRectWidth), objs.canvas.height
      );
      break;
  }
};
```
<br>

| <img src="https://raw.githubusercontent.com/JaeKP/image_repo/main/img/220615sectionHeight.png" alt="220615sectionHeight" style="zoom: 33%;" /> | 먼저, 섹션 기준 캔버스가 어디있는지 확인한다. <br />캔버스가 브라우저 상단에 닿으면 애니메이션이 끝나야 하기 때문이다. <br />즉, 섹션 길이기준 캔버스의 높이 비율만큼 스크롤하면 애니메이션이 종료된다. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

- 그러나 현재 캔버스 크기는 `transform: scale`로 크기가 조정되어 있는 상태이다. 
  - 그 결과,  `(원래 캔버스 높이 - 조정된 캔버스 높이) / 2`를 원래 offsetTop에 더하면 된다.

- 출발: 원하는 타이밍으로 지정하면 된다. 
- 도착: 캔버스가 상단에 닿을 때, 효과가 끝난다. 즉 offsetTop만큼 스크롤하면 애니메이션은 종료된다. 

<br>
