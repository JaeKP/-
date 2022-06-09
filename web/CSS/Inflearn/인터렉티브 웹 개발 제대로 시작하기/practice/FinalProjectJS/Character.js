// 생성자 함수
function Character(info){
  this.mainElem = document.createElement("div");
  this.mainElem.classList.add("character");
  this.mainElem.innerHTML = ''
  + '<div class="character-face-con character-head">'
      + '<div class="character-face character-head-face face-front"></div>'
      + '<div class="character-face character-head-face face-back"></div>'
  + '</div>'
  + '<div class="character-face-con character-torso">'
      + '<div class="character-face character-torso-face face-front"></div>'
      + '<div class="character-face character-torso-face face-back"></div>'
  + '</div>'
  + '<div class="character-face-con character-arm character-arm-right">'
      + '<div class="character-face character-arm-face face-front"></div>'
      + '<div class="character-face character-arm-face face-back"></div>'
  + '</div>'
  + '<div class="character-face-con character-arm character-arm-left">'
      + '<div class="character-face character-arm-face face-front"></div>'
      + '<div class="character-face character-arm-face face-back"></div>'
  + '</div>'
  + '<div class="character-face-con character-leg character-leg-right">'
      + '<div class="character-face character-leg-face face-front"></div>'
      + '<div class="character-face character-leg-face face-back"></div>'
  + '</div>'
  + '<div class="character-face-con character-leg character-leg-left">'
      + '<div class="character-face character-leg-face face-front"></div>'
      + '<div class="character-face character-leg-face face-back"></div>'
  + '</div>';
  this.mainElem.style.left = `${info.xPos}%`

  document.querySelector(".stage").appendChild(this.mainElem);

  // 스크롤 중인지 아닌지
  this.scrollState = false;

  // 마지막 스크롤 위치 
  this.lastScrollTop = 0;

  // 캐릭터 이동관련 속성
  this.xPos = info.xPos      // 캐릭터 위치
  this.speed = info.speed;          // 이동 속도
  this.direction;     // 이동 방향
  this.runningState = false; // 좌우 이동 중인지 
  this.refId;

  this.init()
};

Character.prototype = {
  constructor: Character,
  init: function(){
    const Self = this;
    window.addEventListener("scroll", function(){
      clearTimeout(Self.scrollState);
      
      if (!Self.scrollState) {
        Self.mainElem.classList.add("running");
      }
      
      // 스크롤이 멈추면 실행된다. (clearTimeout때문에..) 
      // 변수에 할당한 이유는 스크롤 중 running클래스를 추가하는 것이 계속 반복되는 것을 막기 위함이다.
      // 추가적인 스크롤 이벤트가 발생하기 전에, scrollState에 값을 부여해서 위의 조건을 만족시키지 않게 한다.  
      Self.scrollState = setTimeout(function(){
        Self.scrollState = false;
        Self.mainElem.classList.remove("running");
      }, 100);
      
      // 마지막 스크롤 위치와 현재 스크롤위치를 비교하여 스크롤을 올린 것인지 내린 것인지 확인한다.
      if (Self.lastScrollTop > pageYOffset){
        // 이전 스크롤 위치가 크다면: 스크롤 올림
        Self.mainElem.setAttribute("data-direction", "backward");
      } else {
        // 현재 스크롤 위치가 크다면: 스크롤 내림
        Self.mainElem.setAttribute("data-direction", "forward");
      }

      Self.lastScrollTop = pageYOffset;
    });

    // 왼쪽, 오른쪽 키를 누르면 이동한다. 
    // 캐릭터의 위치를 정하는 것은 left값이다. (생성자 함수의 info.xPos)
    // 키를 누르면 runningState가 true가 되고, 키를 떼면 runningState가 false가 된다. 
    window.addEventListener("keydown", function(event){
      if (Self.runningState) return;

      if (event.keyCode == 37) {
        //왼쪽
        Self.direction = "left";
        Self.mainElem.setAttribute("data-direction", "left");
        Self.mainElem.classList.add("running");
        Self.run();
        Self.runningState = true;
      } else if (event.keyCode == 39) {
        // 오른쪽
        Self.direction = "right";
        Self.mainElem.setAttribute("data-direction", "right");
        Self.mainElem.classList.add("running")
        Self.run();
        Self.runningState = true;
      }
    });

    window.addEventListener("keyup", function(){
      Self.mainElem.classList.remove("running");
      cancelAnimationFrame(Self.refId);
      Self.runningState = false;

    })
  }, 
  run: function(){
    const Self = this;
    if (Self.direction == 'left') {
      Self.xPos -= Self.speed
    } else if (Self.direction == 'right'){
      Self.xPos += Self.speed
    }

    // 움직임 범위 제한
    if (Self.xPos < 2) {
      Self.xPos = 2;
    } 
    if (Self.xPos > 88) {
      Self.xPos = 88;
    }
    Self.mainElem.style.left = `${Self.xPos}%`

    // context가 바뀌어서 Self에서의 this가 달라진다. => bind사용으로 묶는다. 
    Self.refId = requestAnimationFrame(Self.run.bind(Self))
  }


}