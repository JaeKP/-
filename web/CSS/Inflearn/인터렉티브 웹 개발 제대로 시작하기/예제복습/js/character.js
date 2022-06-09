function Character({clickX, speed}){
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

  this.mainElem.style.left = `${clickX* 100}%`;
  stageElem.appendChild(this.mainElem);
  
  this.lastScroll = 0; 
  this.running = false;
  
  this.runSpeed = speed;
  this.xPos = clickX * 100;
  this.direction;
  this.refId;

  this.init();
};

Character.prototype = {
  prototype: Character,
  init: function(){
    const Self = this;

    window.addEventListener("scroll", function(){
      clearTimeout(Self.running)
      if (!Self.running) {Self.mainElem.classList.add("running")}

      if (Self.lastScroll < scrollY){
        Self.mainElem.setAttribute("data-direction", "forward");
        Self.lastScroll = scrollY;
        Self.running = true;
      } else {
        Self.mainElem.setAttribute("data-direction", "backward");
        Self.lastScroll = scrollY;
        Self.running = true;
      };

      Self.running = this.setTimeout(function(){
        Self.running = false;
        Self.mainElem.classList.remove("running")
      }, 500);
    });

    window.addEventListener("keydown", function(event){
      if (!Self.running) {Self.mainElem.classList.add("running")}

      if (event.keyCode === 37){
        Self.mainElem.setAttribute("data-direction", "left")
        Self.running = true;
        Self.direction = "left";
        Self.run();
      } else if (event.keyCode === 39) {
        Self.mainElem.setAttribute("data-direction", "right")
        Self.running = true;
        Self.direction = "right";
        Self.run();
      };
    })

    window.addEventListener("keyup", function(){
      Self.running = false;
      Self.mainElem.classList.remove("running");
    })
  },
  run: function(){
    const Self = this;
    if (Self.direction  === "left") {
      Self.xPos -= Self.runSpeed;
    } else if (Self.direction === "right") {
      Self.xPos += Self.runSpeed;
    };

    if (Self.xPos < 2) {
      Self.xPos = 2
    };

    if (Self.xPos > 88) {
      Self.xPos = 88
    };

    Self.mainElem.style.left = `${Self.xPos}%`;
  }
};