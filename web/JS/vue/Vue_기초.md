# Vue_기초

> Front-End Development
>
> HTML, CSS 그리고 Java Script를 활용해서 데이터를 볼 수 있게 만들어 준다.
>
> 이 작업을 통해 사용자(User)는 데이터와 상호작용(Interaction)할 수 있다. 

### 1) SPA

Single Page Application(단일 페이지 애플리케이션): 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 애플리케이션

- 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성한다. 

  - 처음 페이지를 받은 이후부터는 서버로부터 새로운 전체 페이지를 불러오는 것이 아닌, 현재 페이지 중 필요한 부분만 동적으로 다시 작성한다.

- 연속되는 페이지 간의 사용자 경험(UX)을 향상

  ​	모바일 사용량이 증가하고 있는 현재. 트래픽 감소와 속도, 반응성의 향상은 매우 중요하기 때문이다.

- 동작 원리의 일부가 CSR(Client SIde Rendering)의 구조를 따른다. 

<br>

#### (1) SPA 등장배경

- 과거 웹사이트들은 요청에 따라 매번 새로운 페이지를 응답하는 방식이었다. (MPA: Multi Page Application)
- 스마트폰이 등장하면서 모바일 최적화의 필요성이 대두된다. 
  - 모바일 네이티브 앱과 같은 형태의 웹 페이지가 필요해졌다.
- 1개의 웹 페이지에서 여러 동작이 이루어지며 모바일 앱과 비슷한 형태의 사용자 경험을 제공한다.

<br>

#### (2) CSR

>  Client Side Rendering

- 서버에서 화면을 구성하는 SSR방식과 달리 클라이언트에서 화면을 구성한다. (즉, 하나의 html과 많~은 JS로 제공한다. )
- 최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고 이후 클라이언트에서는 필요한 데이터만 요청해 JS만 DOM을 렌더링하는 방식이다.
- 즉, 처음에 뼈대만 받고 브라우저에서 동적으로 DOM을 그린다. 
- **SPA가 사용하는 렌더링 방식이다.**

| 장점                                                         | 단점                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 서버와 클라이언트간 트래픽이 감소한다.<br />웹 애플리케이션에 필요한 모든 정적 리소스를 최초에 한 번 다운로드 후 필요한 데이터만 갱신한다.<br /> (바뀌는 데이터만 JSON으로 보내면되니까! ) | SSR에 비해 전체 페이지 최종 렌더링 시점이 느리다.            |
| 사용자 경험(UX) 향상<br />전체 페이지를 다시 렌더링하지 않고 변경되는 부분만을 갱신하기 때문이다. | SEO에 어려움이 있다. (최초 문서에 데이터 마크업이 없기 때문이다. ) <br /> |

<br>

`SSR`

> Server Side Rendering

- 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식이다. (Server가 html 완성본을 넘긴다. )
- JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식이다. 

| 장점                                                         | 단점                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 초기 구동 속도가 빠르다. <br />클라이언트가 빠르게 컨텐츠를 볼 수 있다. | 모든 요청마다 새로운 페이지를 구성하여 전달한다. <br />반복되는 전체 새로고침이 많아 사용자 경험이 떨어진다.<br />상대적으로 트래픽이 많아 서버의 부담이 클 수 있다. |
| SEO에 적합하다. <br />DOM에 이미 모든 데이터가 작성되어있기 때문이다. |                                                              |



**즉, 결국 실제로 사용자가 보는 것은 html 태그로서 만들어야 한다. **

**누가 그 html을 만드냐에 따라 방법이 나뉘는 것이다. (실제로 브라우저에 그려질, 랜더링 될 HTML을 누가 만드는 건지)**

<br>

#### (3) SEO 대응

> SEO (Search Engine Optimization) 검색 엔진 최적화
>
> 웹 페이지 검색엔진이 자료를 수집하고 순위를 매기는 방식에 맞게 웹 페이지를 구성해서 검색 결과의 상위에 노출될 수 있도록 하는 작업이다.

- Vue.js 또는 React 등의 SPA 프레임 워크는 SSR을 지원하는 SEO 대응 기술이 이미 존재한다.
  SEO 대응이 필요한 페이지에 대해서는 선별적 SEO 대응이 가능하다.
- 혹은 추가로 별도의 프레임워크를 사용하기도 한다.
  - Nuxt.js: Vue.js 응용 프로그램을 만들기 위한 프레임 워크이다. SSR을 지원한다. 
  - Next.js: React 응용 프로그램을 만들기 위한 프레임워크이다. SSR을 지원한다. 

<br>

### 2) Vanila JS 와 Vue.js

| Vanila JS                                                    | Vue.js                                                       |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| DB의 변경사항을 DOM에 반영하려면 <br />모든 요소를 선택하여 이벤트를 등록하고 값을 변경해야 한다. | DOM과 Data가 연결되어 있다.<br />Data를 변경하면 이에 연결된 DOM은 알아서 변경한다. <br />DOM이 Data의 변경에 반응(react)한다! |
|                                                              | 개발자가 신경써야할 것은 오직 Data에 대한 관리이다. <br />Developer EXP가 향상된다. |

<br>

## 2. Vue.js 

<img src="https://012.vuejs.org/images/mvvm.png" alt="mvvm" style="zoom:50%;" />

<br>

[공식문서](https://012.vuejs.org/guide/)

>  Technically, Vue.js is focused on the [ViewModel](https://012.vuejs.org/guide/#ViewModel) layer of the MVVM pattern. It connects the [View](https://012.vuejs.org/guide/#View) and the [Model](https://012.vuejs.org/guide/#Model) via two way data bindings. Actual DOM manipulations and output formatting are abstracted away into [Directives](https://012.vuejs.org/guide/#Directives) and [Filters](https://012.vuejs.org/guide/#Filters).

기술적으로 Vue.js는 MVVM 패턴(Model, View, ViewModel로 구성된 애플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴이다.)의 ViewModel계층에 초점을 맞춘다.**vue는 view와 model을 양방향 데이터를 통해 연결한다. 실제 DOM조작과 출력 포맷은 directive와 filter로 추상화된다.** 

즉, Vue는 DOM(HTML)과 data(JSON)의 중재자와 같은 역할을 한다.

<br>

### 1) MVVM 

#### (1) Model

- Vue에서 Model은 JS의 Object === {key:value}이다. 
- Model은 Vue Instance 내부에서 data라는 이름으로 존재한다.
- 이 data가 바뀌면 View(DOM)이 반응한다. (자바스크립트 객체가 바뀌면 자동으로 반영!)

<br>

#### (2) View

- Vue에서 View는 DOM(HTML)이다.
- Data의 변화에 따라 바뀌는 대상이다.

<br>

#### (3) ViewModel

- Vue에서 ViewModel은 모든 VueInstance이다.
- View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리한다.
- ViewModel을 활용해 Data를 얼마만큼 잘 처리해서 보여줄 것인지(DOM)를 고민하는 것이다.

<br>

### 2) 공식문서 따라하기 

[공식문서](https://kr.vuejs.org/v2/guide/#Vue-js%EA%B0%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80%EC%9A%94)

Data가 변화하면 DOM이 변경된다. Data로직을 작성 => DOM 작성

```vue
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vue Quick Start</title>
  </head>
  <body>
    <!-- 1. 선언적 렌더링: 이제는 데이터를 선언만 하면 알아서 연결된 태그가 바뀐다! 
    데이터만 조절하면 알아서 화면이 변경된다. -->
    <h2>선언적 렌더링</h2>
    <div id="app1">{{ message }}</div>

    <!-- 2. 엘리멘트 속성 바인딩: 디렉티브 사용 -->
    <h2>Element 속성 바인딩</h2>
    <div id="app2" v-bind:title="message">내 위에 잠시 마우스를 올리면 동적으로 바인딩 된 title을 볼 수 있습니다!</div>

    <!-- 3. 조건 -->
    <h2>조건</h2>
    <div id="app3">
      <p v-if="seen">보인다</p>
    </div>
      
    <!-- 4. 반복 -->
    <h2>반복</h2>
    <div id="app4">
      <ol>
        <li v-for="todo in todos">{{ todo.text }}</li>
      </ol>
    </div>

    <!-- 5. 사용자 입력 핸들링 -->
    <h2>사용자 입력 핸들링</h2>
    <div id="app5">
      <p>{{ message }}</p>
      <input v-model="message" type="text" />
      <button v-on:click="reverseMessage">거꾸로</button>
    </div>

    <!-- Vue CDN -->
    <script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>

    <script>
      // 1. 선언적 렌더링: vue 인스턴스 생성 (VM)
      // el: 어떤 html과 bind되는가.
      // data: Model
      new Vue({
        el: "#app1",
        data: {
          message: "안녕",
        },
      });

      // 2. 엘리먼트 속성 바인딩
      new Vue({
        el: "#app2",
        data: {
          message: `이 페이지는 ${new Date()}에 로드되었다!`,
        },
      });

      // 3. 조건
      new Vue({
        el: "#app3",
        data: {
          seen: true,
        },
      });

      // 4. 반복
      new Vue({
        el: "#app4",
        data: {
          todos: [
            { text: "js복습" },
            { text: "react복습" },
            { text: "vue복습" },
          ],
        },
      });

      // 5. 사용자 입력 핸들링
      const app5 = new Vue({
        el: "#app5",
        data: {
          message: "안녕하세요",
        },
        // 화살표로 정의하면 안된다.
        methods: {
          reverseMessage: function () {
            this.message = this.message.split("").reverse().join("");
          },
        },
      });
    </script>
  </body>
</html>

```

<br>

## 3. Vue.js의 기초 문법 (공식 문서 정리!)

### 1) Vue instance

[공식문서](https://kr.vuejs.org/v2/guide/instance.html)

모든 Vue 앱은 `Vue` 함수로 새 **Vue 인스턴스**를 만드는 것부터 시작한다.

```react
var vm = new Vue({
  // 옵션
})
```

Vue 인스턴스를 생성할 때는 **options 객체**를 전달해야 한다. 전체 옵션 목록은 [API reference](https://kr.vuejs.org/v2/api/#%EC%98%B5%EC%85%98-%EB%8D%B0%EC%9D%B4%ED%84%B0)에서 확인할 수 있다.

<br>

#### (1) el

- **타입:** `string | Element`

- **제한:** `new`를 이용한 인스턴스 생성때만 사용된다.

- **상세:**

  Vue 인스턴스에 마운트(연결) 할 기존 DOM 엘리먼트 필요하다. CSS 선택자 문자열 또는 실제 HTMLElement 이어야 한다.

  인스턴스가 마운트 된 이후, 그 엘리먼트는 `vm.$el`로 액세스 할 수 있다.

  인스턴스화 할 때 옵션을 사용할 수 있는 경우 인스턴스는 즉시 컴파일을 시작한다. 그렇지 않으면 컴파일을 수동으로 하기 위해 `vm.$mount()`를 명시적으로 호출해야한다.

<br>

#### (2) data

```
var data = { a: 1 }

// 직접 객체 생성
var vm = new Vue({
  data: data
})
vm.a // => 1
vm.$data === data // => true

// Vue.extend()에서 반드시 함수를 사용해야 합니다.
var Component = Vue.extend({
  data: function () {
    return { a: 1 }
  }
})
```

- **타입:** `Object | Function`

- **제한:** 컴포넌트에서 사용될 때만 `함수`를 승인한다.

- **상세:**

  Vue 인스턴스의 데이터 객체이다.(Vue 인스턴스의 상태 데이터를 정의하는 곳이다.) Vue는 속성을 getter/setter로 재귀적으로 변환해 “반응형”으로 만든다. 

  **template에서 interpolation을 통해 접근이 가능하다. directive에서도 사용이 가능하다. Vue 객체 내 다른 함수에서 this 키워드로 접근이 가능하다.** 

  **객체는 반드시 기본 객체이어야 한다**: 브라우저 API 객체 및 프로토타입 속성과 같은 기본 객체는 무시된다. 데이터는 데이터일 뿐이며 객체 자체의 상태를 유지하는 동작은 관찰하지 않는 것이 좋다.

  일단 관찰되어지면, 루트 데이터 객체에 반응형 속성을 추가할 수 없다. 따라서 인스턴스 생성 이전에 모든 루트 수준의 반응형 속성을 미리 선언해야 한다.

  인스턴스가 생성된 이후 원래 데이터 객체는 `vm.$data`로 접근할 수 있다. Vue 인스턴스는 데이터 객체에 있는 모든 속성을 프록시하므로 `vm.a`는 `vm.$data.a`와 동일하다. 

  `_` 또는 `$`로 시작하는 속성은 Vue의 내부 속성 및 API 메소드와 충돌할 수 있으므로 Vue 인스턴스에서 **프록시 되지 않는다**. `vm.$data._property`로 접근 해야 한다.

  **컴포넌트**를 정의할 때 `data`는 데이터를 반환하는 함수로 선언해야한다. `data`를 위해 일반 객체를 사용하면 생성된 모든 인스턴스에서 동일한 객체가 **참조로 공유**된다. `data` 함수를 제공함으로써 새로운 인스턴스가 생성될 때마다 호출하여 초기 데이터의 새 복사본을 반환할 수 있다.

  필요한 경우, `vm.$data`를 `JSON.parse(JSON.stringify(...))`를 통해 전달함으로써 원본 객체의 복사본을 얻을 수 있다.

<br>

```
data: vm => ({ a: vm.myProp })
```

__화살표 함수를 `data`에서 사용하면 안된다.__ (예를 들어, `data: () => { return { a: this.myProp }}`) 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에 `this`는 예상과 달리 Vue 인스턴스가 아니며, `this.myProp`는 정의되지 않는다.



`this`

- Vue 함수 객체 내에서 vue 인스턴스를 가리킨다.
- 단, 화살표함수를 사용하면 안되는 경우 (생성 시 객체로 bind되기 때문이다.) => data, method 정의 등

<br>

#### (3) methods

```javascript
const vm = new Vue({ 
    data: { a: 1 },  
    methods: {
        plus: function () {  
            this.a++    
        }  
    }})

vm.plus()
vm.a // 2
```

- **타입:** `{ [key: string]: Function }`

- **상세:**

  Vue 인스턴스에 추가할 메소드입니다. VM 인스턴스를 통해 직접 접근하거나 디렉티브 표현식에서 사용할 수 있습니다. 모든 메소드는 자동으로 `this` 컨텍스트를 Vue 인스턴스에 바인딩합니다. **( template에서 interpolation을 통해 접근이 가능하다. directive에서도 사용이 가능하다. Vue 객체 내 다른 함수에서 this 키워드로 접근이 가능하다. )** 

  **화살표 함수를 메소드를 정의하는데 사용하면 안된다.** 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에 `this`는 Vue 인스턴스가 아니며 `this.a`는 정의되지 않는다.

<br>

#### (4) computed

[공식 문서](https://kr.vuejs.org/v2/guide/computed.html)

```javascript
var vm = new Vue({
  data: { a: 1 },
  computed: {
    // get만 가능합니다.
    aDouble: function () {
      return this.a * 2
    },
    // get과 set 입니다.
    // computed 속성은 기본적으로 getter 함수만 가지고 있지만, 필요한 경우 setter 함수를 만들어 쓸 수 있다.
    aPlus: {
      get: function () {
        return this.a + 1
      },
      set: function (v) {
        this.a = v - 1
      }
    }
  }
}) 
vm.aPlus   // => 2
vm.aPlus = 3
vm.a       // => 2
vm.aDouble // => 4
```

- **타입:** `{ [key: string]: Function | { get: Function, set: Function } }`

- **상세:**

  Vue 인스턴스에 추가되는 계산된 속성(데이터를 기반으로한 계산된 속성이다.)이다. 

  모든 getter와 setter는 자동으로 `this` 컨텍스트를 Vue 인스턴스에 바인딩 한다.

  **함수의 형태로 정의하지만 함수가 아닌 함수의 반환 값이 바인딩 된다. 반드시 반환 값이 있어야 한다.** 

  __계산된 속성을 정의 할 때 화살표 함수를 사용하면 안된다.__ 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에 `this`는 Vue 인스턴스가 아니며 `this.a`는 정의되지 않는다.

  ```javascript
  computed: {
    aDouble: vm => vm.a * 2
  }
  ```

  계산된 속성은 캐시 되며 의존하고 있는 반응형 속성이 변경되는 경우 다시 평가된다. **즉, 종속된 데이터가 변경될 때만 함수를 실행한다.**

  특정한 의존성이 인스턴스의 범위를 벗어나는 경우(반응형이지 않은 경우)에 계산된 속성은 갱신되지 않는다. **어떠한 데이터에도 의존하지 않는 computed 속성의 경우 절대로 업데이트 되지 않는다.** 

  대부분의 상황에서 `cache: false`를 사용하는 것은 이상적인 방법이 아니다. 가능할 때마다 외부 데이터를 반응형 시스템 안으로 가져오는 것이 훨씬 좋다. 예를 들어, 계산된 속성이 윈도우 크기에 의존하는 경우 이 정보를 `data` 에 저장한 다음 `resize` 이벤트를 사용하여 데이터를 최신 상태로 유지할 수 있다. 

<br>

`computed vs methods`

표현식에서 메소드를 호출하여 같은 결과를 얻을 수도 있습니다.

```html
<p>뒤집힌 메시지: "{{ reversedMessage() }}"</p>
```

<br>

```javascript
const vm = new Vue({
  el: '#example',
  data: {
    message: '안녕하세요'
  },
  computed: {
    // 계산된 getter
    reversedMessage: function () {
      // `this` 는 vm 인스턴스를 가리킨다.
      return this.message.split('').reverse().join('')
    }
  }
})
```

```javascript
methods: {
  reversedMessage: function () {
    return this.message.split('').reverse().join('')
  }
}
```

- computed 속성 대신 메소드와 같은 함수를 정의할 수도 있습니다. 최종 결과에 대해 두 가지 접근 방식은 서로 동일하다. 
- 차이점은 **computed 속성은 종속 대상을 따라 저장(캐싱)된다는 것 이다.**
  -  computed 속성은 해당 속성이 종속된 대상이 변경될 때만 함수를 실행합니다. 
  - 즉 `message`가 변경되지 않는 한, computed 속성인 `reversedMessage`를 여러 번 요청해도 계산을 다시 하지 않고 계산되어 있던 결과를 즉시 반환합니다.
- 이에 비해 메소드를 호출하면 렌더링을 다시 할 때마다 **항상** 함수를 실행한다. (즉, 캐싱을 원하지 않는 경우 메소드를 사용하면 된다.)

<br>

또한 `Date.now()`처럼 아무 곳에도 의존하지 않는 computed 속성의 경우 절대로 업데이트되지 않는다는 뜻이다.

```javascript
computed: {
  now: function () {
    return Date.now()
  }
}
```

<br>

#### (5) watch

[공식문서](https://kr.vuejs.org/v2/guide/computed.html#watch-%EC%86%8D%EC%84%B1)

```javascript
const vm = new Vue({
  data: {
    a: 1,
    b: 2,
    c: 3,
    d: 4,
    e: {
      f: {
        g: 5
      }
    }
  },
  watch: {
   
    // 함수
    a: function (val, oldVal) {
      console.log('new: %s, old: %s', val, oldVal)
    },
    
    // 문자열 메소드 이름
    b: 'someMethod',
    
    // 깊은 감시자 (Objects 내부의 중첩된 값 변경을 감지하려면 deep: true를 해야 한다. Array 변이를 수신하기 위해 그렇게 할 필요는 없다.)
    c: {
      handler: function (val, oldVal) { /* 생략 */ },
      deep: true
    },
    
    // 콜백은 관찰이 시작된 직후 호출된다. (immediate: true를 전달하면 표현식의 현재 값으로 즉시 콜백을 호출합니다.)
    d: {
      handler: 'someMethod',
      immediate: true
    },
      
    // 배열
    e: [
      'handle1',
      function handle2 (val, oldVal) { /* 생략 */ },
      {
        handler: function handle3 (val, oldVal) { /* 생략 */ },
        /* 생략 */
      }
    ],
      
    // watch vm.e.f's value: {g: 5}
    'e.f': function (val, oldVal) { /* 생략 */ }
  }
})

// 데이터 a가 변경되면 해당 함수가 자동으로 실행된다.
vm.a = 2 // => new: 2, old: 1
```

- **타입:** `{ [key: string]: string | Function | Object | Array}`

- **상세:**

  데이터를 감시하고 데이터에 변화가 일어났을 때 실행되는 함수이다.

  대부분의 경우 computed 속성이 더 적합하지만 사용자가 만든 감시자가 필요한 경우가 있습니다. 그래서 Vue는 `watch` 옵션을 통해 데이터 변경에 반응하는 보다 일반적인 방법을 제공한다. **이는 데이터 변경에 대한 응답으로 비동기식 또는 시간이 많이 소요되는 조작을 수행하려는 경우에 가장 유용하다.**

  키가 표시되는 표현식이고 값이 콜백입니다. 값은 메서드 이름이 문자열이거나 추가 옵션이 포함된 Object가 될 수도 있습니다. Vue 인스턴스는 인스턴스 생성시 객체의 각 항목에 대해 `$watch()`를 호출한다.

  __화살표 함수를 감시자에 사용하면 안된다.__ (예를 들어, `searchQuery: newValue => this.updateAutocomplete(newValue)`) 화살표 함수가 부모 컨텍스트를 바인딩하기 때문에 `this`는 Vue 인스턴스가 아니며 `this.updateAutocomplete`는 정의되지 않습니다.

<br>

`computed vs watch`

| computed                                                     | watch                                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 특정 데이터를 직접적으로 사용/ 가공하여 다른 값을 만들 때 사용한다. | 특정 데이터의 변화 상황에 맞춰 다른 data 등이 바뀌어야 할 때 주로 사용한다. |
| 속성은 계산해야 하는 목표 데이터를 정의하는 방식이다.<br /> `선언형 프로그래밍` 방식이다. <br />(계산해야 하는 목표 데이터를 정의) | 감시할 데이터를 지정하고 그 데이터가 바뀌면 특정함수를 실행하는 방식이다. <br />`명령형 프로그래밍`방식이다.<br />(데이터가 바뀌면 특정 함수를 실행해!) |
| 특정 값이 변동하면 해당 값을 다시 계산해서 보여준다. <br />  | 특정 값이 변공하면 다른 작업을 한다. <br />특정 대상이 변경되었을 때 콜백 함수를 실행시키기 위한 트리거이다. |

```html
<div id="demo">{{ fullName }}</div>
```

```javascript
const vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar',
    fullName: 'Foo Bar'
  },
  watch: {
    firstName: function (val) {
      this.fullName = val + ' ' + this.lastName
    },
    lastName: function (val) {
      this.fullName = this.firstName + ' ' + val
    }
  }
})
```

```javascript
const vm = new Vue({
  el: '#demo',
  data: {
    firstName: 'Foo',
    lastName: 'Bar'
  },
  computed: {
    fullName: function () {
      return this.firstName + ' ' + this.lastName
    }
  }
})
```

다른 데이터 기반으로 변경할 필요가 있는 데이터가 있는 경우 선언형 프로그래밍인 computed를 사용하는 것을 권장한다.  (react의 useMemo)

watch는 데이터 변경에 따른 비동기 작업을 할때 ! (react의 useEffect)

<br>

#### (6) filters

#### (7) 라이프사이클 훅

<img src="https://kr.vuejs.org/images/lifecycle.png" alt="lifeCycleHook" style="zoom:50%;" />



### 2) templates 문법





