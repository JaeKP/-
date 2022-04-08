# PRACTICE

## 1. To Do List 

### 1) 사용자가 입력한 ToDo를 저장하는 배열생성

```react
import { useState, useEffect } from "react";

// to-do list 만들기

// 함수형 컴포넌트
function App() {
  const [toDo, setToDo] = useState("");
  const [toDos, setToDos] = useState([]);
  const onChange = (event) => setToDo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (toDo === "") {
      return;
    }
    setToDo("");
    // 여러개의 toDo를 저장할 수 있는 배열을 생성한다. 
    // function(cuttentArray){return}와 같다.
    setToDos((currentArray) => [toDo, ...currentArray]);
  };
  console.log(toDos);
  return (
    <div>
      <h1>My To Dos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input
          onChange={onChange}
          value={toDo}
          type="text"
          placeholder="write your to do..."
        />
        <button>Add To Do</button>
      </form>
    </div>
  );
}

export default App;
```

- `event.preventDefault();`
  - submit버튼을 누르면 새로고침되는 것을 막는다. 
  
- `setToDo("");`
  - submit버튼을 누르면 toDo를 입력할 수있는 공간이 비워진다. 
  - setToDo는 toDo 값을 수정하는 함수고 toDo 값은 input의 value와 연결되어 있어서 toDo값을 변경하면 input값도 변경된다. 
  
- ` setToDos((currentArray) => [toDo, ...currentArray]);  };`
  
  - 함수를 보낼 때 react.js는 함수의 첫 번째 argument로 현재 state를 보낸다. 그러면 현재 state를 계산하거나 새로운 state를 만드는데 사용할 수 있게 된다. 
  
  - 현재의 toDO를 받아와서 새로운 toDo의 array로 return하고 있다. 
  
  - ```react
    const food = [1, 2, 3, 4]
    console.log([6, food])     // [6, Array[4]]
    conseole.log([6, ...food]) // [6, 1, 2, 3, 4]
    ```
  

<br>

### 2) array의 item을 변형해서 li로 형식을 바꾼다.

```react
import { useState, useEffect } from "react";

// to-do list 만들기
function App() {
  const [toDo, setToDo] = useState("");
  const [toDos, setToDos] = useState([]);
  const onChange = (event) => setToDo(event.target.value);
  const onSubmit = (event) => {
    event.preventDefault();
    if (toDo === "") {
      return;
    }
    setToDo("");
    setToDos((currentArray) => [toDo, ...currentArray]);
  };
  console.log(toDos);
  return (
    <div>
      <h1>My To Dos ({toDos.length})</h1>
      <form onSubmit={onSubmit}>
        <input
          onChange={onChange}
          value={toDo}
          type="text"
          placeholder="write your to do..."
        />
        <button>Add To Do</button>
      </form>
      <hr />
      {/* 배열을 가지고 있을 때 각각의 element들을 바꿀 수 있게 해준다. */}
      {toDos.map((item, index) => (
        <li key={index}>{item}</li>
      ))}
    </div>
  );
}

export default App;
```

- map은 함수의 첫번째 argumnent는 value로 현재의 item을 가져 올 수 있다.
  - map(item) -> item이나 원하는 어떤 변수명을 넣으면 item자체를 리턴하는 것도 가능하다.
- 두번째 argument는  index(숫자)이다. (리액트는 기본적으로 list에 있는 모든 item을 인식하기 때문에 key를 넣어 고유하게 만들어줘야한다.)
  - 즉, 배열을 만들어 각자 고유의 key를 가지게 한다. 

```react
// [':)',':)',':)',':)',':)',':)']
['there''are', 'you'. 'are', 'how', 'hello!'].map(() => ";)")

// ['THERE', 'ARE', 'YOU', 'ARE', 'HOW', 'HELLO!']
['there''are', 'you'. 'are', 'how', 'hello!'].map((item) => item.toUpperCase())  
```

<br>

## 2. Coin Tracker

```react
import { useState, useEffect } from "react";

// Coin Tracker 만들기
function App() {
  // 로딩을 위한 state
  const [loading, setLoading] = useState(true);
  useEffect(() => {
    fetch("https://api.coinpaprika.com/v1/tickers")
      .then((response) => response.json()) // json으로 변환
      .then((json) => {
        setCoins(json); // json 값을 setCoins해준다. (coins라는 변수에 코인들의 array가 담겨있다)
        setLoading(false); // 데이터를 얻어오면 로딩 종료!
      });
  }, []);
  // api => json 를 통해 얻은 데이터를 우리의 컴포넌트에 보여준다.
  // 해당 데이터를 State에 넣는다.
  // 코인 리스트를 잠시 갖기 위한 state
  const [conis, setCoins] = useState([]);
  return (
    <div>
      <h1>The Coin! {loading ? "" : `(${conis.length})`}</h1>
      {loading ? (
        <strong>Loading...</strong>
      ) : (
        <ul>
          {/* 코인 API에는 이미 key(ID)가 있으므로 안 가져와도 된다. */}
          {conis.map((coin) => (
            <li>
              {coin.name} ({coin.symbol}) : {coin.quotes.USD.price} USD
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
```

- Api로 받은 데이터를 json으로 전환 후 State에 저장한다. 
- 해당 State 변수를 map함수를 이용하여 UI에 보여준다. 

<br>

## 3. Movie App

### 1) API를 통해 영화 raw 데이터를 받고 이를 가공하여 화면에 출력한다. 

```react
import { useState, useEffect } from "react";

function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    fetch(
      "https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year"
    )
      .then((response) => response.json())
      .then((json) => {
        setMovies(json.data.movies);
        setLoading(false);
      });
  }, []);
  return (
    <div>
      {loading ? (
        <h1>Loading...</h1>
      ) : (
        <div>
          {movies.map((movie) => (
            <div key={movie.id}>
              {/* 영화 이미지 */}
              <img src={movie.medium_cover_image} />
              {/* 영화 제목 */}
              <h2>{movie.title}</h2>
              {/* 영화 소개 */}
              <p>{movie.summary}</p>
              <ul>
                {movie.genres.map((g) => (
                  <li key={g}>{g}</li>  // key={g} -> 따로 정해진 key가 없기 때문에 g를 가져와 key로 사용한다. 
                ))}
              </ul>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;

```

- `movies.map()`은 state로부터 받은 data를 보여주는 것 뿐이다. 
  - API로부터 data를 받은 State를 각각의 movie에 접근해서 그 값을 변환한다. 

<br>

### 2) Prop와 Component 활용

```react
// App.js

import { useState, useEffect } from "react";
import Movie from "./components/Movie";

function App() {
  const [loading, setLoading] = useState(true);
  const [movies, setMovies] = useState([]);
  useEffect(() => {
    fetch(
      "https://yts.mx/api/v2/list_movies.json?minimum_rating=9&sort_by=year"
    )
      .then((response) => response.json())
      .then((json) => {
        setMovies(json.data.movies);
        setLoading(false);
      });
  }, []);
  return (
    <div>
      {loading ? (
        <h1>Loading...</h1>
      ) : (
        <div>
          {/* prop으로써 component로 넘겨서 사용한다. */}
          {/* key는 map안에서 component들을 render할 때 사용하는 것이다. */}
          {movies.map((movie) => (
            <Movie
              key={movie.id}
              coverImg={movie.medium_cover_image}
              title={movie.title}
              summary={movie.summary}
              genres={movie.genres}
            />
          ))}
        </div>
      )}
    </div>
  );
}
export default App;

```

- API로 받은 데이터를 State에 저장한다. 
- State를 Props로!

<br>

```react
// Movie.js

import PropTypes from "prop-types";

// props 오브젝트
// 무비 컴포넌트가 medium_cover_image, title, summary, genres와 같은 정보를 부모컴포넌트로부터 받아온다.
function Movie({ coverImg, title, summary, genres }) {
  return (
    <div>
      <div>
        <img src={coverImg} />
        <h2>{title}</h2>
        <p>{summary}</p>
        <ul>
          {genres.map((g) => (
            <li key={g}>{g}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

// 무비 컴포넌트의 prop 타입을 정의한다.
Movie.propTypes = {
  coverImg: PropTypes.string.isRequired,
  title: PropTypes.string.isRequired,
  summary: PropTypes.string.isRequired,
  genres: PropTypes.arrayOf(PropTypes.string).isRequired,
};

export default Movie;
```

- App.js를 통해 받은 Props를 이용하여 ui에 데이터를 보여준다. 

<br>

#### (1) router

> 라우팅은 사용자가 요청한 URL에 따라 해당 URL에 맞는 페이지를 보여주는 것이다.

```bash
npm i react-router-dom@5.3.0
```

```react
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
```

그래서 페이지 별로 파일을 만들고, 

