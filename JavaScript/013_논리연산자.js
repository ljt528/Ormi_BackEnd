// 논리 연산자(&&, ||, !)
let x = true; // 1
let y = false; // 0

// &&는 곱
// ||는 합
// !는 부정

x && y; // false
x || y; // true
!y; // true
!x; // false
// 실무에서 많이 사용합니다.
!!y;
!!"hello";

!!NaN; // false
!!null; // false
!!undefined; // false

!![]; // true // 이렇게 사용하지 마시고
Number.isNaN({}); // 이렇게 사용하시기를 권해드립니다.
Number.isNaN([]); // 이렇게 사용하시기를 권해드립니다.
// object의 길이를 함께 판단하시면 됩니다.

//////////////////////////////////////////////////

// javascript에서는 아래와 같은 단락평가를 자주 사용합니다.

null && "hello"; // null
"world" && "hello"; // 'hello'

// 단락 평가는 거의 || 를 사용합니다!

// let name = "";
// name = name || "이름이 입력되지 않음";

// let name = "juntae";
// name = name || "이름이 입력되지 않음";

let 로그인여부 = true;
name = 로그인여부 && "이름이 입력되지 않음";

// 보통은 3항 연산자 + 단락평가로 사용합니다.
let 로그인여부 = true;
로그인페이지 = 로그인여부 && "<h1>환영합니다 고객님</h1>";
로그인페이지;

let pw = "";
pw = pw || "패스워드가 입력되지 않았습니다.";
