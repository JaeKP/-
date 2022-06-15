// 즉시 호출 함수
(() => {

  let yOffset = 0; // window.scrollY를 저장하는 변수
  let prevScrollHeight = 0; // 현재 스크롤 위치(yOffset)보다 이전에 위치한 스크롤 섹션들의 스크롤 높이의 합
  let currentScene = 0; // 현재 활성화된 scene (scroll-section)
  let enterNewScene = false; // 새로운 scene이 시작된 순간 true가 되는 변수

  // 스크롤 구간에 대한 정보를 저장하는 배열
  const sceneInfo = [
    {
      // 0
      type: "sticky",
      heightNum: 5, // 브라우저 높이의 5배로 scrollHeight를 세팅할 것이다.
      scrollHeight: 0,
      objs: {
        container: document.querySelector("#scroll-section-0"),
        messageA: document.querySelector("#scroll-section-0 .main-message.a"),
        messageB: document.querySelector("#scroll-section-0 .main-message.b"),
        messageC: document.querySelector("#scroll-section-0 .main-message.c"),
        messageD: document.querySelector("#scroll-section-0 .main-message.d"),
        canvas: document.querySelector("#video-canvas-0"),
        context: document.querySelector("#video-canvas-0").getContext('2d'),
        videoImages: [], // 이미지 배열
      },
      values: {
        messageA_opacity_in: [0, 1, {start: 0.1, end: 0.2}], // 투명도: [시작 값, 끝나는 값, {애니메이션이 재생되는 구간}]
        messageA_opacity_out: [1, 0, {start: 0.25, end: 0.3}], 
        messageA_translateY_in: [20, 0, {start: 0.1, end: 0.2}],
        messageA_translateY_out: [0, -20, {start: 0.25, end: 0.3}],

        messageB_opacity_in: [0, 1, { start: 0.3, end: 0.4 }],
        messageB_opacity_out: [1, 0, { start: 0.45, end: 0.5 }],
        messageB_translateY_in: [20, 0, { start: 0.3, end: 0.4 }],
        messageB_translateY_out: [0, -20, { start: 0.45, end: 0.5 }],

        messageC_opacity_in: [0, 1, { start: 0.5, end: 0.6 }],
        messageC_opacity_out: [1, 0, { start: 0.65, end: 0.7 }],
        messageC_translateY_in: [20, 0, { start: 0.5, end: 0.6 }],
        messageC_translateY_out: [0, -20, { start: 0.65, end: 0.7 }],

        messageD_opacity_in: [0, 1, { start: 0.7, end: 0.8 }],
        messageD_opacity_out: [1, 0, { start: 0.85, end: 0.9 }],
        messageD_translateY_in: [20, 0, { start: 0.7, end: 0.8 }],
        messageD_translateY_out: [0, -20, { start: 0.85, end: 0.9 }],

        videoImageCount : 300,
        imageSequence: [0, 299],
        canvas_opacity: [1, 0, {start: 0.9, end: 1}]
      }
    },
    {
      // 1
      type: "normal",
      // heightNum: 5, 
      scrollHeight: 0,
      objs: {
        container: document.querySelector('#scroll-section-1'),
        content: document.querySelector('#scroll-section-1 .description')
      }
    },
    {
      // 2
      type: "sticky",
      heightNum: 5, // 브라우저 높이의 5배로 scrollHeight를 세팅할 것이다.
      scrollHeight: 0,
      objs:{
        container: document.querySelector("#scroll-section-2"),
        messageA: document.querySelector('#scroll-section-2 .a'),
        messageB: document.querySelector('#scroll-section-2 .b'),
        messageC: document.querySelector('#scroll-section-2 .c'),
        pinB: document.querySelector('#scroll-section-2 .b .pin'),
        pinC: document.querySelector('#scroll-section-2 .c .pin'),
        canvas: document.querySelector("#video-canvas-1"),
        context: document.querySelector("#video-canvas-1").getContext('2d'),
        videoImages: [], // 이미지 배열
      },
      values: {
        messageA_opacity_in: [0, 1, { start: 0.15, end: 0.2 }],
        messageA_opacity_out: [1, 0, { start: 0.3, end: 0.35 }],
        messageA_translateY_in: [20, 0, { start: 0.15, end: 0.2 }],
        messageA_translateY_out: [0, -20, { start: 0.3, end: 0.35 }],

        messageB_opacity_in: [0, 1, { start: 0.5, end: 0.55 }],
        messageB_opacity_out: [1, 0, { start: 0.58, end: 0.63 }],
        messageB_translateY_in: [30, 0, { start: 0.5, end: 0.55 }],
        messageB_translateY_out: [0, -20, { start: 0.58, end: 0.63 }],

        messageC_opacity_in: [0, 1, { start: 0.72, end: 0.77 }],
        messageC_translateY_out: [0, -20, { start: 0.85, end: 0.9 }],
        messageC_translateY_in: [30, 0, { start: 0.72, end: 0.77 }],
        messageC_opacity_out: [1, 0, { start: 0.85, end: 0.9 }],

        pinB_opacity_in: [0, 1, { start: 0.5, end: 0.55 }],
        pinB_opacity_out: [1, 0, { start: 0.58, end: 0.63 }],
        pinB_scaleY: [0.5, 1, { start: 0.5, end: 0.55 }],

        pinC_opacity_in: [0, 1, { start: 0.72, end: 0.77 }],
        pinC_opacity_out: [1, 0, { start: 0.85, end: 0.9 }],
        pinC_scaleY: [0.5, 1, { start: 0.72, end: 0.77 }],

        videoImageCount : 960,
        imageSequence: [0, 959],
        canvas_opacity_in: [0, 1  , {start: 0, end: 0.1}],
        canvas_opacity_out: [1, 0, {start: 0.9, end: 1}],
      }
    },
    {
      // 3
      type: "sticky",
      heightNum: 5, // 브라우저 높이의 5배로 scrollHeight를 세팅할 것이다.
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
        rectStartY: 0
      }
    },
  ];

  // 이미지 저장. 
  function setCanvasImage(){
    let imgElem;
    for (let i = 0; i < sceneInfo[0].values.videoImageCount ; i++){
      imgElem = new Image();
      imgElem.src = `./video/001/IMG_${6726 + i}.JPG`;
      sceneInfo[0].objs.videoImages.push(imgElem);
    };

    let imgElem2;
    for (let i = 0; i < sceneInfo[2].values.videoImageCount ; i++){
      imgElem2 = new Image();
      imgElem2.src = `./video/002/IMG_${7027 + i}.JPG`;
      sceneInfo[2].objs.videoImages.push(imgElem2);
    };

    let imgElem3;
    for (let i = 0; i < sceneInfo[3].objs.imagesPath.length; i++) {
      imgElem3 = new Image();
      imgElem3.src = sceneInfo[3].objs.imagesPath[i];
      sceneInfo[3].objs.images.push(imgElem3);
    };
  }



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
    sceneInfo[2].objs.canvas.style.transform = `translate3d(-50%, -50%, 0) scale(${heightRatio})`;
  };
  
  function calcValues(values, currentYOffset){   // value:변경할 요소, currentYOffset: 각 세션에서 얼마만큼의 스크롤 되었는가
    let rv;

    const scrollHeight = sceneInfo[currentScene].scrollHeight
    const scrollRatio = currentYOffset / scrollHeight; // 현재 씬에서 스크롤된 범위를 비율로 저장하는 변수
  
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


  // 애니메이션 구현과 관련된 함수
  function playAnimation(){
    const objs = sceneInfo[currentScene].objs;
    const values = sceneInfo[currentScene].values;
    const currentYOffset = yOffset - prevScrollHeight;
    const scrollHeight = sceneInfo[currentScene].scrollHeight
    const scrollRatio =  currentYOffset / scrollHeight  // 현재 scene에서 얼마나 스크롤 되었는가 / 현재 씬의 scrllHeight

    switch (currentScene) {
      case 0 :
        // canvas에 그린다. 
        let sequence = Math.round(calcValues(values.imageSequence, currentYOffset));
        objs.context.drawImage(objs.videoImages[sequence], 0, 0);

        // canvas 투명도
        objs.canvas.style.opacity = calcValues(values.canvas_opacity, currentYOffset);
        
        // 문구
        if (scrollRatio <= 0.22) {
          // in
          const messageA_opacity_in = calcValues(values.messageA_opacity_in, currentYOffset);
          const messageA_translateY_in = calcValues(values.messageA_translateY_in, currentYOffset);
          objs.messageA.style.opacity = messageA_opacity_in;
          objs.messageA.style.transform = `translateY(${messageA_translateY_in}%)`
        } else {
          // out
          const messageA_opacity_out = calcValues(values.messageA_opacity_out, currentYOffset);
          const messageA_translateY_out = calcValues(values.messageA_translateY_out, currentYOffset);
          objs.messageA.style.opacity = messageA_opacity_out;
          objs.messageA.style.transform = `translateY(${messageA_translateY_out}%)`
        };

        if (scrollRatio <= 0.42) {
          // in
          objs.messageB.style.opacity = calcValues(values.messageB_opacity_in, currentYOffset);
          objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_in, currentYOffset)}%, 0)`;
        } else {
          // out
          objs.messageB.style.opacity = calcValues(values.messageB_opacity_out, currentYOffset);
          objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_out, currentYOffset)}%, 0)`;
        };

        if (scrollRatio <= 0.62) {
          // in
          objs.messageC.style.opacity = calcValues(values.messageC_opacity_in, currentYOffset);
          objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_in, currentYOffset)}%, 0)`;
        } else {
          // out
          objs.messageC.style.opacity = calcValues(values.messageC_opacity_out, currentYOffset);
          objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_out, currentYOffset)}%, 0)`;
        };

        if (scrollRatio <= 0.82) {
          // in
          objs.messageD.style.opacity = calcValues(values.messageD_opacity_in, currentYOffset);
          objs.messageD.style.transform = `translate3d(0, ${calcValues(values.messageD_translateY_in, currentYOffset)}%, 0)`;
        } else {
          // out
          objs.messageD.style.opacity = calcValues(values.messageD_opacity_out, currentYOffset);
          objs.messageD.style.transform = `translate3d(0, ${calcValues(values.messageD_translateY_out, currentYOffset)}%, 0)`;
        };

        break;

      case 2:
        // console.log('2') 

        // canvas에 그린다. 
        let sequence2 = Math.round(calcValues(values.imageSequence, currentYOffset));
        objs.context.drawImage(objs.videoImages[sequence2], 0, 0);

        // canvas 투명도
        if (scrollRatio <= 0.5) {
          // in 
          objs.canvas.style.opacity = calcValues(values.canvas_opacity_in, currentYOffset);
        } else {
          // out
          objs.canvas.style.opacity = calcValues(values.canvas_opacity_out, currentYOffset);
        }

        if (scrollRatio <= 0.25) {
          // in
          objs.messageA.style.opacity = calcValues(values.messageA_opacity_in, currentYOffset);
          objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_in, currentYOffset)}%, 0)`;
        } else {
          // out
          objs.messageA.style.opacity = calcValues(values.messageA_opacity_out, currentYOffset);
          objs.messageA.style.transform = `translate3d(0, ${calcValues(values.messageA_translateY_out, currentYOffset)}%, 0)`;
        };

        if (scrollRatio <= 0.57) {
          // in
          objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_in, currentYOffset)}%, 0)`;
          objs.messageB.style.opacity = calcValues(values.messageB_opacity_in, currentYOffset);
          objs.pinB.style.transform = `scaleY(${calcValues(values.pinB_scaleY, currentYOffset)})`;
        } else {
          // out
          objs.messageB.style.transform = `translate3d(0, ${calcValues(values.messageB_translateY_out, currentYOffset)}%, 0)`;
          objs.messageB.style.opacity = calcValues(values.messageB_opacity_out, currentYOffset);
          objs.pinB.style.transform = `scaleY(${calcValues(values.pinB_scaleY, currentYOffset)})`;
        };

        if (scrollRatio <= 0.83) {
          // in
          objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_in, currentYOffset)}%, 0)`;
          objs.messageC.style.opacity = calcValues(values.messageC_opacity_in, currentYOffset);
          objs.pinC.style.transform = `scaleY(${calcValues(values.pinC_scaleY, currentYOffset)})`;
        } else {
          // out
          objs.messageC.style.transform = `translate3d(0, ${calcValues(values.messageC_translateY_out, currentYOffset)}%, 0)`;
          objs.messageC.style.opacity = calcValues(values.messageC_opacity_out, currentYOffset);
          objs.pinC.style.transform = `scaleY(${calcValues(values.pinC_scaleY, currentYOffset)})`;
        };
        
        break;  

      case 3:
        // console.log('3');
        // 가로 / 세로 모두 꽉 차게 하기 위해 크기를 세팅한다. (계산)
        // 실제 브라우저 비율과 캔버스의 비율이 달라서 캔버스 사이즈를 억지로 피트시킨다. 
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

        objs.canvas.style.transform = `scale(${canvasScaleRatio})`;


        // 이미지 그려주기 
        objs.context.drawImage(objs.images[0], 0, 0);

        // 캔버스 사이즈에 맞춰 innerWidth와 innerHeight 비율 계산
        // 크롬의 경우, 스크롤바가 영역을 차지 하기 때문에, innerWidth에서 스크롤바를 제외한 폭을 구해야 한다.  
        // const recalculatedInnerWidth = window.innerWidth / canvasScaleRatio;
        const recalculatedInnerWidth = document.body.offsetWidth / canvasScaleRatio;
        const recalculatedInnerHeight = window.innerHeight / canvasScaleRatio; // 해당 예제에서는:  objs.canvas.height

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
        
        
        // 스크롤 애니메이션 출발지점, 도착지점 설정: 흰색 박스가 점점 사라지는 애니메이션이 진행된다. 캔버스가 상단에 닿는 타이밍에 박스가 아예 사라진다.
        // 그래서 애니메이션이 시작될때, 캔버스의 y위치를 구해야 한다. 

        // 처음에 0으로 설정했기때문에, 처음에만 값을 세팅하고 다시 실행하지 않는다. 
        if (!values.rectStartY){
          // values.rectStartY = objs.canvas.getBoundingClientRect().top;
          // offsetTop: 브라우저기준이 아니라 문서 기준이지만, 기준점을 바꿀 수 있다. 
          // 부모의 포지션이 static이 아니면 부모기준 offsetTop을 잡을 수 있다.
          // 그런데 현재, 캔버스가 scale이 조정이 되어있지만, transform으로 변형된 것을 고려하지 않는다.
          // scale이 조정된 후의 위치를 원한다. 그래서 scale이 조정된 비율만큼 다시 계산을 해야 한다.
          // 그 결과, (원래 캔버스 높이 - 조정된 캔버스 높이) /2 를 offsetTop에 더하면 된다. 
          values.rectStartY = objs.canvas.offsetTop + (objs.canvas.height - objs.canvas.height*canvasScaleRatio) / 2

          // start시점 구하기: 윈도우 높이의 절반!
          values.rect1X[2].start = (window.innerHeight / 2) / scrollHeight; 
          values.rect2X[2].start = (window.innerHeight / 2) / scrollHeight;          

          // 애니메이션이 시작될때 캔버스와 브러우저 상단 사이의 거리 / 현재씬의 높이
          values.rect1X[2].end = values.rectStartY / scrollHeight; 
          values.rect2X[2].end = values.rectStartY / scrollHeight; 
        }
        
        
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
  
  // 현재 스크롤하는 곳이 몇번째 섹션인지 확인한다. (현재 활성시킬 scene을 결정한다. )
  function scrollLoop(){
    enterNewScene = false;
    prevScrollHeight = 0;
    for (let i = 0 ; i < currentScene; i++) {
      prevScrollHeight += sceneInfo[i].scrollHeight;
    };
    
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
    
    if (enterNewScene) return; 
    playAnimation(); // 씬이 바뀌는 순간에는 이상한 값이 들어가기 때문에 playAnimation을 막는다. 
  };
  
  window.addEventListener("scroll", () => {
    yOffset = window.scrollY
    scrollLoop();
  });

  //load: DOM객체이외에도 모든 이미지나 미디어 파일이 로드되면 실행된다.  
  //DOMContentLoaded: DOM 객체가 로드되면 실행된다.
  window.addEventListener("load", ()=> {
    setLayout();
    sceneInfo[0].objs.context.drawImage(sceneInfo[0].objs.videoImages[0], 0, 0);
    sceneInfo[2].objs.context.drawImage(sceneInfo[2].objs.videoImages[0], 0, 0);
  });
  window.addEventListener("resize", setLayout);
  setCanvasImage();
})();
