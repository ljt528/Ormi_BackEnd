function f(x, y){
    return x + y
}

// 즉시 실행함수, 정의와 동시에 실행되는 함수
(function() {
    console.log('Hello');
});

(x, y) => x + y
let f2 = (x, y) => x + y
// python에서는 lambda의 위상이 재사용하지 않는 함수에서 많이 사용하지만
// JavaScript에서는 화살표 함수가 일반 함수만큼 자주 사용됩니다.
// (화살표 함수의 문법이 나온지 그리 오래되진 않았습니다.)

// 1. 중괄호가 없고 return되는 코드가 1줄이면 return을 생략합니다.
let f3 = (x, y) => x + y

// 2. 중괄호가 생기면 return이 있어야 합니다.
let f4 = (x, y) => {
    let z = x + y
    return z
}

// 3. 전달하는 파라미터가 1개이면 소괄호도 생략할 수 있습니다.
let f5 = x => x + x

// 반지름이 입력되면 원의 넓이를 구하는 화살표 함수를 만들어주세요.
// (가능하면 가장 단축된 방법으로)
let f6 = r => (r ** 2) * Math.PI

// 다음처럼 여러 값이 입력되었을 때, 가장 큰 값과 가장 작은 값, 총합을 출력하는 함수를 만들어주세요.
// 일반함수, 화살표 함수 2개 만들어주세요.
입력 : 함수이름(10, 20, 30, 40)
출력 : [40, 10, 100]

function f7(w, x, y, z){
    max = MAth.max(w, x, y, z)
    min = MAth.min(w, x, y, z)
    sum = w + x + y + z
    return [max, min, sum]
}

let f8 = (w, x, y, z) => {
    max = MAth.max(w, x, y, z)
    min = MAth.min(w, x, y, z)
    sum = w + x + y + z
    return [max, min, sum]
}