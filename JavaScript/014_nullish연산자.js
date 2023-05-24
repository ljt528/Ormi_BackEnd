// https://ko.javascript.info/nullish-coalescing-operator
// 나온지 얼마 되지 않았습니다!!
// IE는 지원하지 않았습니다.

// 중간에 하나라도 값이 들어있다면 그 값을 출력합니다.
let firstname = null;
let lastname = null;
let nickname = "licat";

firstname ?? lastname ?? nickname ?? "익명의 사용자";

let a = null;
let b = 10;
let c = null;

a ?? 100; // if null이냐? 그렇다면 100을 넣겠다!
a ?? b; // null이면 10을 넣겠다.
a ?? b ?? c; // => (a ?? b) ?? c 앞쪽에서 값을 가져서 뒤는 의미가 없어짐

//nullish 연산자와 단락평가의 차이점
let height = 0;
height || 100; // 100
height ?? 100; // 0

// || : 0, null, undefined, '', NaN
// ?? : null, undefined
