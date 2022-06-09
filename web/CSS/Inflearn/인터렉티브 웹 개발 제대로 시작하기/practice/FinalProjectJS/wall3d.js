// 즉시 실행 함수
(function () {
  const houseElem = document.querySelector(".house");
  const barElem = document.querySelector(".progress-bar");
  const stageElem = document.querySelector(".stage");
  const selectCharacterElem = document.querySelector(".select-character")
  const mousePos = { x: 0, y: 0 };

  // 문서 전체 높이 - 브라우저 화면 높이: 실제 스크롤 영역
  // pageYOffset / maxScrollValue: 스크롤을 얼마나 했는지 비율을 알 수 있다.
  let maxScrollValue;
  function resizeHandler() {
    maxScrollValue = document.body.offsetHeight - window.innerHeight;
  }

  // 스크롤하면 house의 z값이 이동한다.
  // 스크롤하면 프로그레스바가 채워진다.
  window.addEventListener("scroll", function () {
    const scrollPer = pageYOffset / maxScrollValue;
    const zMove = scrollPer * 980 - 490;
    houseElem.style.transform = `translateZ(${zMove}vw)`;

    // progress bar
    barElem.style.width = `${scrollPer * 100}%`;
  });

  // 윈도우 사이즈가 변경될때마다, maxScrollValue가 갱신되어야 한다.
  window.addEventListener("resize", resizeHandler);

  // 마우스의 움직임에 따라 시야가 움직인다. (stage를 회전)
  window.addEventListener("mousemove", function ({ clientX, clientY }) {
    // 왼쪽 상단이 0, 0이 아닌 중간이 0, 0이 되도록 값을 재계산한다.
    mousePos.x = -1 + (clientX / window.innerWidth) * 2;
    mousePos.y = 1 - (clientY / window.innerHeight) * 2;
    stageElem.style.transform = `rotateX(${mousePos.y*5}deg) rotateY(${mousePos.x*5}deg)`;
  });

  // 클릭한 곳에 일분이 캐릭터가 생긴다.
  stageElem.addEventListener('click', function(event){
    // 여러 속성을 전달하기 위해 객체에 넣어서 전달한다. 
    new Character({
      xPos: event.clientX / window.innerWidth * 100,
      speed: Math.random()*0.4 + 0.2
    })
  });

  // 캐릭터 변경
  selectCharacterElem.addEventListener("click", function(event){
    const value = event.target.getAttribute("data-char")
    document.body.setAttribute("data-char", value)
  });

  // 문서가 로드되면 resizeHandler 함수 호출
  resizeHandler();
})();
