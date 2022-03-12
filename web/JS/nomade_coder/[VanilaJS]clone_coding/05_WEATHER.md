# WEATHER

### 1) 사용자의 위치 정보 받기

```javascript
function onGeoOk(position){
  const lat = position.coords.latitude;  
  const lon =  position.coords.longitude;
  console.log("You live in", lat, lon);

}

function onGeoError(){
  alert("Can't fint you. No weather for you");

}

// navigator.geolocation.getCurrentPosition(success, error, [options])
// navigator.geolocation.getCurrentPosition는 position(argument)를 그냥 제공해준다. 
// eventListener가 event를 argument로 그냥 제공해주는 것과 비슷한 원리이다. 
navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
```

:pencil2:참고자료: https://developer.mozilla.org/ko/docs/Web/API/Geolocation/getCurrentPosition

<br>

### 2) API를 활용하여 해당 지역의 날씨를 제공

```javascript
const API_KEY = "";


function onGeoOk(position){
  const lat = position.coords.latitude;  
  const lon =  position.coords.longitude;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}`

  // 이제 url을 호출(request)한다.
  // 자바스크립트가 대신 url을 호출한 것!
  fetch(url)
  .then((response)=> response.json())
  .then((data)=> {
    const weather = document.querySelector("#weather span:first-child");
    const city = document.querySelector("#weather span:last-child");
    city.innerText = data.name;
    weather.innerText = `${data.weather[0].main} / ${data.main.temp}`;
  });

}

function onGeoError(){
  alert("Can't fint you. No weather for you");
}

navigator.geolocation.getCurrentPosition(onGeoOk, onGeoError);
```

`https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=[{API key}`

- `lat={lat}`, `lon={lon}`: 유저의 lat, lon 데이터를 반영
- `appid={API key}`: 개발자의 api키를 기입

<br>