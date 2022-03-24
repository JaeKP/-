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

```html
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

```html
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

<br>

#### (1) 컴포넌트를 다른 컴포넌트 안에 넣기

```html
  <script src="https://unpkg.com/react@17.0.2/umd/react.production.min.js"></script>
  <script src="https://unpkg.com/react-dom@17.0.2/umd/react-dom.production.min.js"></script>
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <script type="text/babel">
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

    // 여러 컴포넌트들이 합쳐진 구성을 생성한다.
    // 컴포넌트의 첫 글자는 반드시 대문자여야 한다.
    // 만약 소문자면 HTML태그로 인식한다.
    const Container = (
      <div>
        <Title />
        <Button />
      </div>
    );
    ReactDOM.render(Container, root);
  </script>
```

<br>
