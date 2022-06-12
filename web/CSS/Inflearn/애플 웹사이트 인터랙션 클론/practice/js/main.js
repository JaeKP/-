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
      },
      values: {
        messageA_opacity_in: [0, 1, {start: 0.1, end: 0.2}], // 투명도: [시작 값, 끝나는 값, {애니메이션이 재생되는 구간}]
        messageA_opacity_out: [1, 0, {start: 0.25, end: 0.3}], 
        messageA_translateY_in: [20, 0, {start: 0.1, end: 0.2}],
        messageA_translateY_out: [0, -20, {start: 0.25, end: 0.3}],

      },
    },
    {
      // 1
      type: "normal",
      // heightNum: 5, 
      scrollHeight: 0,
      objs:{
        container: document.querySelector("#scroll-section-1")
      }
    },
    {
      // 2
      type: "sticky",
      heightNum: 5, // 브라우저 높이의 5배로 scrollHeight를 세팅할 것이다.
      scrollHeight: 0,
      objs:{
        container: document.querySelector("#scroll-section-2")
      }
    },
    {
      // 3
      type: "sticky",
      heightNum: 5, // 브라우저 높이의 5배로 scrollHeight를 세팅할 것이다.
      scrollHeight: 0,
      objs:{
        container: document.querySelector("#scroll-section-3")
      }
    },
  ];

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
        // console.log('0') 
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

        break;

      case 1: 
        // console.log('1') 
        break;

      case 2:
        // console.log('2') 
        break;  

      case 3:
        // console.log('3') 
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
  window.addEventListener("load", setLayout);
  window.addEventListener("resize", setLayout);
})();
