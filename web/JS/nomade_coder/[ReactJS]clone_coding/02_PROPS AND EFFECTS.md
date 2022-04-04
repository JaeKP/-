# PROPS AND REACT APP

## 1. PROPS

> 속성을 나타내는 데이터이다. (컴포넌트의 환경을 설정)
> props는 부모 컴포넌트가 자식 컴포넌트에 값을 전달할 때 사용하는 것이다. (읽기 전용이다. )

<br>

**`state와의 비교`**

- state: 컴포넌트 자기 자신이 가지고 있는 값이다. 변화가 필요할 경우 setState()함수를 통해 값을 변경해줄 수 있다.
  -  자신이 states를 수정할 수 있다. 컴포넌트 내부의 동적 데이터이다. 
- props:  컴포넌트에서 컴포넌트로 전달하는 데이터이다. 해당 컴포넌트를 불러와 사용하는 부모 컴포넌트에서만 설정 가능
  - 속성을 나타내는 데이터
  -  자신은 props를 읽기 전용으로만 사용할 수 있다.

<br>

## 1) 기본

```javascript
  <script type="text/babel">
    // props는 이 Btm이 전달 받는 유일한 인자이다.
    // props의 특정 키의 이름을 사용해서 {key1,key2}로  바로 넣을 수 있다.
    function Btn(props) {
      return (
        <button
          style={{
            backgroundColor: "tomato",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: 10,
            fontSize: props.big ? 18 : 16,
          }}
        >
          {props.text}
        </button>
      );
    }

    function App() {
      return (
        // 함수형 컨포넌트를 불러내는 것!
        // props는 오브젝트이다. 아래의 속성을 모두 갖는다.
        // props 오브젝트는 text라는 키를 갖고 있는 상태가 된다.
        <div>
          <Btn text="Save Changes" big={true} />
          <Btn text="Continue" big={false} />
        </div>
      );
    }
    const root = document.getElementById("root");
    ReactDOM.render(<App />, root);
  </script>
```

- **props에 접근할 수 있는 방법은 이 컴포넌트 함수의 첫 번째 인자 안에서만 가능하다.** 

<br>

## 2) Memo

```javascript
  <script type="text/babel">
    function Btn({ text, onClick }) {
      return (
        <button
          onClick={onClick}
          style={{
            backgroundColor: "tomato",
            color: "white",
            padding: "10px 20px",
            border: 0,
            borderRadius: 10,
          }}
        >
          {text}
        </button>
      );
    }

    const MemorizedBtn = React.memo(Btn);

    // 만약 부모 컴포넌트의 state에 변경이 있다면 모든 자식 컴포넌트 또한 re-render될 것이다.
    // 아래와 같은 경우에는 자식 컴포넌트가 클릭될때마다 changeValue함수를 발생시켜 부모 컴포넌트의 state에 변경이 되고 다같이 re-render 될 것이다. 
    // 만약, props로 전달하는 값이 변하지 않을 시, 해당 자식 컴포넌트의 re-rendering을 방지하기 위해서 React.memo() 메서드를 사용하여 성능을 개선할 수 있다.
    function App() {
      const [value, setValue] = React.useState("Save Changes");
      const changeValue = () => setValue("Revert Changes");
      return (
        // 이 곳에 적는 props는 단지 props일 뿐이다.
        // 함수 컴포넌트에 전달하지 않는다면, 실제 HTML 태그 안에 들어가지 않는다.
        <div>
          <MemorizedBtn text={value} onClick={changeValue} />
          <MemorizedBtn text="Continue" />
        </div>
      );
    }
    const root = document.getElementById("root");
    ReactDOM.render(<App />, root);
  </script>
```

<br>

### 3) Prop Type

> 어떤 타입의 Prop를 받고 있는지 체크해준다. 

```javascript
  <script type="text/babel">
    // default값을 설정할 수도 있다.
    function Btn({ text, fontSize = 10 }) {...
    }

    // 리액트에게 prop의 타입에 대해 설명해준다.
    // prop이름: 타입
    // required: 해당 속성이 무조건 존재한다는 의미.
    Btn.propTypes = {
      text: PropTypes.string.required,
      fontSize: PropTypes.number.required,
    };
                                           
    function App() {
      return (
        <div>
          <Btn text="Save Changes" fontSize={18} />
          <Btn text="Continue" />
        </div>
      );
    }
    const root = document.getElementById("root");
    ReactDOM.render(<App />, root);
    }
```

- props로 전달할 데이터의 종류와 타입은 PropTypes라는 패키지로 지정할 수 있다
- PropTypes로 전달하는 데이터의 default는 선택 사항이다 
- 반드시 보내야 할 데이터의 속성 같은 경우 `isRequired`를 붙인다.

<br>

## 2. React App

```bash
npx create-react-app my-app
cd my-app
npm start
```

- 컴포넌트 당 1개의 .js 파일을 가질 수 있다. 
  -  모듈화가 가능하다
  -  컴포넌트별 스타일은 .module.css 파일을 생성 + import 하여 사용

- Adding a CSS Modules Stylesheet (React에서 CSS Module 사용하기)
  - 이 프로젝트는 [name].module.css 파일 명명 규칙을 사용하여 일반 스타일시트와 함께 CSS 모듈을 지원합니다. CSS 모듈을 사용하면 이름 충돌에 대한 걱정 없이 다른 파일에서 동일한 CSS 클래스 이름을 사용할 수 있습니다.
  - https://create-react-app.dev/docs/adding-a-css-modules-stylesheet/

<br>

### 1) useEffect

**가끔은 우리가 특정 코드의 실행을 제한하고 싶어한다.** 

**=> 원래 새로운 데이터가 들어올 때마다 refresh 하지만 이를 막아야 할 때도 있다.** 

- state를 변화시킬 때 component를 재실행 시키는 것을 방어하는 것을 의미한다. 
- UI관점으로 보면, 새로운 데이터가 들어올 때 마다 자동으로 새로고침 되는 것은 좋지만, 어떤 코드들은 계속 실행되면 안 될 수도 있기 때문에 useEffect를 사용함으로서 코드를 언제실행할 시 선택할 수 있는 것이다. 

> 예를들어 state를 변경할 때 모든 code 들을 항상 다시 실행되는데, 
>
> 첫 번째 render에만 코드가 실행되고 다른 state변화에는 실행되지 않도록 만들 수 없을까? 
>
> (한번만 받아도 될 정보가 계속 리렌더링 되어 불려지는 것을 방지한다. )



`useEffect` 두 개의 인자를 가지는 함수이다. 

- 첫번째 인자는 우리가 딱 한번만 실행하고 싶어하는 코드이다.
- 두번째 인자는 배열이다. 
  - 빈배열로 두면 코드를 단 한 번 실행한다. 
  - 리스트의 값이 변할 때만 실행된다. 

```javascript
// useEffect 추가
import { useState, useEffect } from "react";

function App() {
  const [counter, setValue] = useState(0);
  const onClick = () => setValue((prev) => prev + 1);
  console.log("call an api");
  console.log("i run all the time");

  // console.log("CALL THE API....")는 State가 변경되어도 다시 실행되지 않는다.
  // 무슨 일이 일어나도 코드는 처음에 renderr가 되는 단 한번만 실행된다.
  useEffect(() => {
    console.log("CALL THE API....");
  }, []);

  return (
    <div>
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}
export default App;
```

<br>

#### `usememo`와의 차이점 (from. 댓글창)

참고 자료: https://ko.reactjs.org/docs/hooks-reference.html#usememo

참고 자료: https://ko.reactjs.org/docs/hooks-reference.html#usememo 

- useMemo의 경우 "생성"함수에 관련된 기능이다. 생성자 함수가 고비용(처리 시간이 오래 걸리는 등)인 경우 렌더링마다 계산하는 것은 처리 시간이 오래 걸리므로 값을 기억해놓고 의존성이 변경되었을 경우에만 다시 계산해주는 기능!

- useEffect의 경우는 api 호출, 타이머 등 렌더링 과정에서 한 번만 호출해도 될 기능이 렌더링마다 실행되거나, 호출과정에서 렌더링에 영향을 끼칠 수 있는 것을 모아서 따로 처리하기 위한 기능입!

**둘의 결정적인 차이는 useEffect는 해당 컴포넌트의 렌더링이 완료된 후에 실행되지만, useMemo는 렌더링 중에 실행되는 차이가 있다.**

<br>

```javascript
// useEffect 추가
import { useState, useEffect } from "react";

function App() {
  const [counter, setValue] = useState(0);
  const [keyword, setKeyword] = useState("");
  const onClick = () => setValue((prev) => prev + 1);
  const onChange = (event) => setKeyword(event.target.value);

  // component가 생성될 때, 단 한 번 실행된다.
  useEffect(() => {
    console.log("I run only once.");
  }, []);

  // 생성 시, counter가 업데이트 때 마다 다시 실행된다.
  useEffect(() => {
    console.log("I run when 'counter' changes.");
  }, [counter]);

  // 생성 시 , keyword가 길이가 5보다 길 때 다시 실행된다.
  useEffect(() => {
    if (keyword !== "" && keyword.length > 5) {
      console.log("I run when 'keyword' changes.");
    }
  }, [keyword]);

  // 생성 시,  keyword, counter 둘 중 하나만 업데이트 되어도 다시 실행된다. 
  useEffect(() => {
    console.log("I run when keyword & counter change");
  }, [keyword, counter]);
  
  return (
    <div>
      <input
        value={keyword}
        onChange={onChange}
        type="text"
        placeholder="Search here..."
      />
      <h1>{counter}</h1>
      <button onClick={onClick}>click me</button>
    </div>
  );
}
export default App;
```

<br>

#### (1) Cleanup

참고자료: https://ko.reactjs.org/docs/hooks-effect.html#effects-with-cleanup 

참고자료: https://simsimjae.tistory.com/401

```javascript
import { useState, useEffect } from "react";

function Hello() {
  useEffect(function () {
    console.log("hi :)");
    // clean-up function
    // component가 사라지거나 destroy될 때 실행될 함수
    return function () {
      console.log("bye :(");
    };
  }, []);
  
  // ====================================
  function byFn() {
    console.log("bye :(");
  }
  function hiFn() {
    console.log("created :)");
    return byFn;
  }
  useEffect(hiFn, []);

  // ====================================
  useEffect(() => {
    console.log("hi :)");
    return () => console.log("bye :(");
  }, []);
  return <h1>Hello</h1>;
}
  // ====================================

function App() {
  const [showing, setShowing] = useState(false);
  const onClick = () => setShowing((prev) => !prev);
  return (
    <div>
      {/* Hello 컴포넌트를 hide 할 때 컴포넌트가 스크린에서 지워진다. */}
      {/* show를 누르면 컴포넌트가 다시 생성되므로 useEffect도 실행된다. */}
      {showing ? <Hello /> : null}
      <button onClick={onClick}>{showing ? "Hide" : "Show"}</button>
    </div>
  );
}
export default App;
```

<br>
