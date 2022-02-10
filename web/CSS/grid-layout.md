# Grid Layout

> 그리드란 그래픽 디자인에서 격자는 내용을 구성하는 데 사용되는 일련의 교차하는 직선 또는 곡선으로 구성된 구조이다.  
>
> 출처: 위키백과

- `flex`는 메인 축이 어디냐(수직 or 수평)에 따라 그 메인축을 중심으로 레이아웃을 구성할 수 있다. 
-  `grid`는 수직 , 수평을 한 번에 고려할 수 있는 레이아웃이다. 

<br>

## 1. Grid Layout 기초

<br

<img src="https://cdn.discordapp.com/attachments/911915398335717420/940616538376011806/-2.jpg" style="zoom:70%">

<br>

```html
<!-- 그리드 속성 생성 -->
.container {
  display: grid;
}
```

<br>

```html
<!-- 그리드 row, column 정의 (대략적인 구조 설정) -->
.container {
  display: grid;
  grid-template-row:850px 850px;
  grid-template-columns: 700px 700px 700px 700px;
}

```

row와 column을 설정할 때 px과 같은 크기 단위를 사용할 수 있다.

하지만 px과 같은 고정적인 크기 단위는 사용자의 화면사이즈에 따라 웹사이트 요소가 변하는 반응형 웹사이트를 만드는 데 적절하지 않다. 



### fraction

> fraction은 
