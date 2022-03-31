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
- PropTypes로 전달하는 데이터의 defaul는 선택 사항히다 
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
