const houseElem = document.querySelector(".house");
const stageElem = document.querySelector('.stage');
const progressElem = document.querySelector(".progress-scroll");

window.addEventListener("scroll", function(){
  const scrollHeight = document.body.offsetHeight - window.innerHeight;
  const scrollRatio = scrollY / scrollHeight;
  const moveScroll = scrollRatio * 980 -490;
  
  // run!
  houseElem.style.transform = `translateZ(${moveScroll}vw)`;

  // progress bar
  progressElem.style.width = `${scrollRatio*100}%`;
  
});

window.addEventListener("mousemove", function({clientX, clientY}){
  const mouseX =  -1 + (clientX / window.innerWidth) * 2;
  const mouseY =  1 - (clientY / window.innerHeight) * 2;
  stageElem.style.transform = `rotateX(${mouseY *3}deg) rotateY(${mouseX *3}deg)`;
});

stageElem.addEventListener("click", function({clientX}){
  let clickX = clientX / window.innerWidth
  if (clickX < 0.07) {
    clickX = 0.07
  }

  if (clickX > 0.85) {
    clickX = 0.85
  }

  const data = {
    clickX,
    speed: Math.random()*0.4 + 0.5
  }
  new Character(data)
});

