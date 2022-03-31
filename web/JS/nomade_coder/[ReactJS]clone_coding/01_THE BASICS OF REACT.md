# THE BASICIS OF REACT

## 1. React JS element 생성

### 1) 기초적인 방법

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <div id="root"></div>
</body>
  <!-- React JS는 어플리 케이션이 아주 interactive하도록 만들어주는 라이브러리 이다.  -->
  <!-- react-dom 은 모든 react element들을 HTML body에 적용할 수 있도록 도와준다.  -->
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script>
    const root = document.getElementById("root");

    // 함수의 인자로 HTML 태그를 입력하면 그 태그를 생성한다. 
    // 함수의 두 번째 인자로 태그의 속성을 기입할 수 있다. 
    // 함수의 세 번째 인자로 태그의 content를 기입할 수 있다. 
    const span = React.createElement(
      "span", 
      {id:"sexy-span"}, 
      "Hello I'm span"
      );

    // react-dom을 활용하여 JS로 생성한 태그를 HTML에 body에 삽입한다. 
    // render(): 사용자에게 보여 준다. (react element를 가지고 HTML로 만들어 배치한다는 것.)
    // 첫 번째 인자: 보여줄 element
    // 두번 째 인자: element를 놓는 위치
    ReactDOM.render(span, root);

  </script>
</html>
```

- 리액트는 JS -> HTML 순서로 프로그래밍을 한다. 
  - 즉, JS가 element를 생성하고 React JS가 그것을 HTML로 번역하는 것이다.
  - 그 결과, React JS는 업데이트 해야 하는 HTML을 업데이트 할 수 있음

 <br>

```javascript
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script>
    const root = document.getElementById("root");
    const h3 = React.createElement("h3", null, "Hello I'm span");

    // element의 속성으로 eventListener를 추가할 수도 있다. 
    const btn = React.createElement(
      "button",
      {
        onClick: () => console.log("im clicked"),
      },
      "CLick me"
    );

    // div태그를 추가로 생성하여 한 번에 2개의 태그를 랜더링한다
    const container = React.createElement("div", null, [h3, btn]);
    ReactDOM.render(container, root);
  </script>
```

<br>

### 2) JSX

> JSX는 자바스크립트의 확장버전, 객체를 표현한다
>
> HTML 이랑 문법 구조가 비슷하다. 

```javascript
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  
  <!-- 브라우저는 JSX문법을 이해하지 못하기 때문에 babel을 사용함으로서 브라우저가 이해할 수 있도록 문법을 자동 변환하여 전달한다.  -->
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");
    const Title = (
      <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
        Hello I'm a title
      </h3>
    );

    const Button = (
      <button
        style={{ backgroundColor: "tomato" }}
        onClick={() => console.log("im clicked")}
      >
        Click me
      </button>
    );

    const container = React.createElement("div", null, [Title, Button]);
    ReactDOM.render(container, root);
  </script>
```

`babel`

- 자바스크립트 변환기 이다. (컴파일러)
- head의 script 태그 내에 어떻게 변환되었는지 확인 할 수 있다. 

<br>

#### (1) 컴포넌트를 다른 컴포넌트 안에 넣기

```javascript
    const root = document.getElementById("root");
    const Title = () => (
      <h3 id="title" onMouseEnter={() => console.log("mouse enter")}>
        Hello I'm a title
      </h3>
    );

    const Button = () => (
      <button
        style={{ backgroundColor: "tomato" }}
        onClick={() => console.log("im clicked")}
      >
        Click me
      </button>
    );

    <!-- 여러 컴포넌트들이 합쳐진 구성을 생성한다. -->
    <!-- 컴포넌트의 첫 글자는 반드시 대문자여야 한다. -->
    <!-- 만약 소문자면 HTML태그로 인식한다. -->
    const Container = (
      <div>
        <Title />
        <Button />
      </div>
    );
    ReactDOM.render(Container, root);
```

**`함수형 컴포넌트`**

- ```javascript
  <!-- arrow 함수 ver -->
      const Button = () => (
        <button
          style={{ backgroundColor: "tomato" }}
          onClick={() => console.log("im clicked")}
        >
          Click me
        </button>
      );
  
  ```

- ```javascript
  <!-- 일반 함수 ver--> 
      function Button() {
        return (
          <button
            style={{ backgroundColor: "tomato" }}
            onClick={() => console.log("im clicked")}
          >
            Click me
          </button>
        );
      }
  ```

<br>

## 2. STATE

> 컴포넌트에서 동적인 값을 state(상태)라고 부른다. 
>
> 동적인 데이터를 다룰 때 사용한다. 

<br>

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");
    const Container = () => (
      <div>
        <h3>Total clicks: 0 </h3>
        <button>Click me</button>
      </div>
    );

    // 컴포넌트 ! <Container />
    ReactDOM.render(<Container />, root);
  </script>
```

<br>

### (1) 컴포넌트에 변수를 추가하고 ui에 반영

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");
    let counter = 0;
    function countUp() {
      counter = counter + 1;
      ReactDOM.render(<Container />, root);
    }

    // 중괄호를 활용해 변수를 jsx에 전달한다.
    // 이벤트 = {이벤트가 발생하면 실행되는 함수}
    // 이벤트가 실행되어서 변경된 것을 ui에 반영되려면 컨포넌트가 다시 랜더링 되어야 한다.
    const Container = () => (
      <div>
        <h3>Total clicks: {counter} </h3>
        <button onClick={countUp}>Click me</button>
      </div>
    );

    ReactDOM.render(<Container />, root);
  </script>
```

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");
    let counter = 0;
    function countUp() {
      counter = counter + 1;
      render();
    }

    function render() {
      ReactDOM.render(<Container />, root);
    }

    const Container = () => (
      <div>
        <h3>Total clicks: {counter} </h3>
        <button onClick={countUp}>Click me</button>
      </div>
    );

    render();
  </script>
```

<br>

### 2) 리렌더링을 하는 다른 방법

```javascript
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
    const root = document.getElementById("root");

    // const data = React.useState();
    // console.log(data) => [undefined, f]
    // undifined는 데이터이다.  f는 이 데이터를 바꿀 때 사용하는 함수이다.
    function App() {
      const data = React.useState();
      console.log(data);
      return (
        <div>
          <h3>Total clicks: 0 </h3>
          <button>Click me</button>
        </div>
      );
    }

    ReactDOM.render(<App />, root);
  </script>
```

`함수형 컴포넌트`

- ```javascript
      function App() {
        const data = React.useState();
        console.log(data);
        return (
          <div>
            <h3>Total clicks: 0 </h3>
            <button>Click me</button>
          </div>
        )
      };

- ```javascript
     const App = () => {
        const data = React.useState();
        console.log(data);
        return (
          <div>
            <h3>Total clicks: 0 </h3>
            <button>Click me</button>
          </div>
        );
  ```

<br>

#### (1) 데이터를 전달 

**`const [<상태 값 저장 변수>, <상태 값 갱신 함수>] = useState(<상태 초기 값>);`**

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");

    // const data = React.useState();
    // console.log(data) => [undefined, f]
    // undifined는 데이터이다.  f는 이 데이터를 바꿀 때 사용하는 함수이다.

    function App() {
      // const data = React.useState(0); 데이터 초기 값을 0으로 설정
      // const counter = data[0];
      // const modifier = data[1];
      const [counter, modifier] = React.useState(0);
      return (
        <div>
          <h3>Total clicks: {counter} </h3>
          <button>Click me</button>
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
```

<br>

#### (2) 데이터 수정 & 리렌더링

**`React.useState`를 통해 counter와 같은 데이터를 숫자형 데이터로 건네주고, 그 데이터 값을 바꿀 함수도 전해준다.**

**이 함수를 이용해서 데이터를 바꿨을 때, 데이터 값이 바뀌고 컴포넌트도 동시에 리렌더링 된다. (자동!)**

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [counter, setCounter] = React.useState(0);
      const onClick = () => {
        setCounter(counter + 1);
      };
      return (
        <div>
          <h3>Total clicks: {counter} </h3>
          <button onClick={onClick}>Click me</button>
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
```

- onClick 이벤트가 발생할 때마다 함수를 

<br>

### 3) State Function

state를 세팅하는 데는 2가지 방법이 있다.

1) 직접 할당 :`setState(state +1)`
   - 현재 state랑 관련이 없는 값을 새로운 state로 하고싶은 경우
2) 함수를 할당:`setState(state => state +1) `(함수의 첫번째 인자는 현재 state 이다)
   - 현재 state에 조금의 변화를 주어서 새로운 state를 주고 싶은 경우

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [counter, setCounter] = React.useState(0);
      const onClick = () => {
        // setCounter(counter + 1);
        // 현재 state를 기반으로 계산 할 떈 아래와 같이 구현한다.
        setCounter((current) => courrent + 1);
      };
      return (
        <div>
          <h3>Total clicks: {counter} </h3>
          <button onClick={onClick}>Click me</button>
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
```

<br>

### 4) Inputs and State

`주의 사항`

```javascript
  function App() {
      return (
        // jsx는 HTML과 비슷하지만 다른 점은 있다. 
        // 특히, for와 class와 같이 이미 JS에서 사용되고 있는 키워드를 HTML사용 목적으로 사용해서는 안된다. 
        // class => className  for => htmlFor
        <div>
          <h1>Super Converter</h1>
          <label htmlFor="minutes">Minutes</label>
          <input id="minutes" placeholder="Minutes" type="number" />
          <label htmlFor="hours">Hours</label>
          <input id="hours" placeholder="Hours" type="number" />
        </div>
      );
    }
```

<br>

```javascript
  <script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [minutes, setMinutes] = React.useState();
      const onChange = (event) => {
        setMinutes(event.target.value);
      };
      return (
        <div>
          <h1>Super Converter</h1>
          <label htmlFor="minutes">Minutes</label>
          <input
            value={minutes}
            id="minutes"
            placeholder="Minutes"
            type="number"
            onChange={onChange} // onChange 이벤트: 값이 변경될 때마다 함수를 실행시킨다.
          />
          <h4>You want to convert {minutes}</h4>
          <label htmlFor="hours">Hours</label>
          <input id="hours" placeholder="Hours" type="number" />
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
```

- input의 value를 state로 연결해주었다. 
  - 어디서든 input의 value를 수정해줄 수 있다.
  - 외부에서 수정이 가능하다. 
  - 만약 onChange함수가 없다면 데이터를 업데이트 할 수 없을 것이다.
    - input의 value는 default가 0인 state이기때문에 입력창에 0으로 써져있고 수정할 수 가 없는 상태가 될 것이다.  
- onChange 함수는 데이터를 업데이트 해주는 역할을 한다. 
  - input에서 리스닝하는 데이터는 스스로 업데이트한다. 
- return()에 `div`태그를 사용하는 이유 
  - [참고자료](https://velog.io/@lilyoh/React-Fragments-%EC%82%AC%EC%9A%A9%EC%9D%B4%EC%9C%A0-%EB%B0%8F-%EC%82%AC%EC%9A%A9%EB%B2%95)
  - 리액트에서는 하나의 컴포넌트가 여러 개의 엘리먼트들을 반환한다. 그래서 return 문 안에는 반드시 하나의 최상위 태그가 있어야 한다.
  - 이는 리액트가 하나의 컴포넌트만을 리턴할 수 있기 때문이다.


<br>

`시간단위를 변환하는 프로그램`

State를 바탕으로 UI를 구성한다. 

```javascript
<script type="text/babel">
    const root = document.getElementById("root");
    function App() {
      const [amount, setAmount] = React.useState(0);
      const [flipped, setFlipped] = React.useState(false);
      const onChange = (event) => {
        setAmount(event.target.value);
      };
      const reset = () => setAmount(0);
      // !flipped은 filpped의 부정 명제이다.
      const onFlip = () => {
        reset();
        setFlipped((current) => !flipped);
      };
      return (
        <div>
          <div>
            <h1>Super Converter</h1>
            <label htmlFor="minutes">Minutes</label>
            <input
              // flipped된 상태가 아니면 값을 그대로 보여준다.
              // flipped된 상태면 변환된 값을 보여준다.
              value={flipped ? amount * 60 : amount}
              id="minutes"
              placeholder="Minutes"
              type="number"
              onChange={onChange}
              // flipped === true: flipped가 true라면.. (조건문)
              // disabled={flipped === true}
              disabled={flipped}
            />
          </div>

          <div>
            <h4>You want to convert</h4>
            <label htmlFor="hours">Hours</label>
            <input
              // flipped된 상태면 값을 그대로 보여준다.
              // flipped된 상태가 아니면 변환된 값을 보여준다.
              value={flipped ? amount : Math.round(amount / 60)}
              id="hours"
              placeholder="Hours"
              type="number"
              onChange={onChange}
              // flipped === false: flipped가 false라면.. (조건문)
              // disabled={flipped === false}
              disabled={!flipped}
            />
          </div>
          <button onClick={reset}>Reset</button>
          <button onClick={onFlip}>{flipped ? "Turn back" : "Invert"}</button>
        </div>
      );
    }
    ReactDOM.render(<App />, root);
  </script>
```

- flipped는 단순히 true 혹은 false인 변수이다. 
- flip버튼을 누르면, onFlip 함수가 실행되는데 onFlip함수는 현재 값을 받아서 그 반대 값을 내놓는다는 것이다. 

- `disabled={flipped===true}`와 같이 속성을 전달 할 수 있다. 
  - `disabled={flipped}`처럼 간단하게 표현 가능
  - `disabled={!flipped}`처럼 간단하게 표현 가능

- Hours 입장에서 Minutes에 값이 입력 되었을 때는 단위변환이 , Hours에 값을 입력할 때는 그냥 입력한 값이 그대로 보여주어야한다. 
- Minutes 입장에서 Hours에 값이 입력 되었을 때는 단위변환이 , Minutes에 값을 입력할 때는 그냥 입력한 값이 그대로 보여주어야한다. 

<br>
`변환기 선택`

컴포넌트는 그 안에 또다른 컴포넌트를 렌더링 할 수 있다.

```javascript
  <script type="text/babel">
    function MinutesToHours() {...
    }
    function KmToMiles() {
      return <h3>KM 2 M</h3>;
    }
                               
    function App() {
      const [index, setIndex] = React.useState("xx");
      const onSelect = (event) => {
        setIndex(event.target.value);
      };
      return (
        // 컴포넌트는 그 안에 또다른 컴포넌트를 렌더링 할 수 있다.
        // <MinutesToHours/>
        // <KmToMiles/>
        <div>
          <h1>Super Converter</h1>
          <select value={index} onChange={onSelect}>
            <option value="xx">Select your units</option>
            <option value="0">Minutes & Hours</option>
            <option value="1">Km & Miles</option>
          </select>
          <hr />
          {index === "xx" ? "Please Select Yout Units" : null}
          {index === "0" ? <MinutesToHours /> : null}
          {index === "1" ? <KmToMiles /> : null}
        </div>
        // 위의 경우 그냥 if를 적으면 문자로 인식한다. 중괄호 안에 적어야 JS문법으로 인식한다.
      );
    }
    const root = document.getElementById("root");
    ReactDOM.render(<App />, root);
  </script>
```

- 컴포넌트는 그 안에 또 다른 컴포넌트를 렌더링 할 수 있다. 
- state를 변화시킬 때, 모든게 새로고침 된다. (새로운 데이터와 함꼐.. )
- useState의 두번째 인자인 modifier함수를 실행하면 해당 컴포넌트가 리렌더링 된다.
  - props이 수정
  - state 수정
  - 부모 컴포넌트가 리렌더링 될 때

<br>
