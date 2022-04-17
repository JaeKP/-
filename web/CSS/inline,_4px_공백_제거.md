# inline, 4px 공백 제거

✏ 참고자료 : https://css-tricks.com/fighting-the-space-between-inline-block-elements/

- display속성이 `inline` or `inline-block` 일 때 ,  요소들 사이에 공백이 생긴다. 
- 이를 없애는 몇가지 트릭이 있다. 

<br>

## 원인



<img src="https://i0.wp.com/css-tricks.com/wp-content/uploads/2012/04/spaces.png?resize=170%2C67" style="zoom:150%">

<br>

```html
<head>
  <style>
    body a {
      display: inline-block;
      padding: 5px;
      background: red;
    }
  </style>
    
</head>
<body>
  <a href="#">One</a>
  <a href="#">Two</a>
  <a href="#">Three</a>
</body> 
```

**문제가 없어보이는데... 공백은 왜 생기는가?**

- 인라인요소의 경우,  개행(줄바꿈)이나 공백은 약 4px의 여백을 가지기 때문이다. 

- 현재 `<a>` 태그들은 개행을 했기 때문에 코드 상으로는 보이지 않는 4px 공백이 존재하는 것이다.  

```	html
<!-- 그래서 이렇게 개행을 하지 않고 코드를 붙이면 공백은 사라진다.-->
<!-- 그런데 코드의 직관성이 너무 떨어진다.-->
<body>
  <a href="#">One</a><a href="#">Two</a><a href="#">Three</a>
</body>
```

<br>

## 해결 방안

### 1. 음수 마진 

```javascript
body a {
  display: inline-block;
  padding: 5px;
  background: red;
  margin-right:-4px
}
```

- 음수마진이란 `margin`속성에 음수 값을 주는 것이다. 
- `bottom/right` 에 음수 마진을 적용한다면, 이 요소 다음에 오는 요소를 끌어당기는 효과가 있다. 

<br>

### 2. float , flex, grid 등

그냥 정렬이 편한 속성을 사용하는 게 좋다.

<br>

---

**`그렇다면, inline block / inline-block 하단 공백은 왜 생길까  `🤔**

인라인 속성으로 표시되는 컨텐츠들은 vertical-align에 따른 기준 선( **base line** )이 존재한다.  

**즉, 인라인 속성의 컨텐츠들은  base line기준으로 배치된다.** 

<br>

영어 소문자의 g, j , p , q , y 와 같은 하행 문자들은 글자가 기준선 밑으로 내려가는 글자들이다.

그 결과, 글자의 아랫 부분을 표현하기 위해 **base line**밑에 약간의 공백을 주게 된다. 이 공백이 앞서 말했던 하단에 생기는 공백이다. 

<br>

특히, 이미지의 경우 이런 일이 빈번하게 발생하는데

- 이미지에 `vertical-align`속성을 'top', 'middle', 'botom'중 지정해주면 해결된다.
  -  인라인 정렬 기준을 base line에서 vertical-align속성으로 변경! 

✏ 관련 문서https://developer.mozilla.org/ko/docs/Web/CSS/vertical-align