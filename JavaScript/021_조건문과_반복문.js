if (condition){
    console.log('hello')
}

if (false) {
    console.log('hello1');
} else if (false) {
    console.log('hello2');
} else if (true) {
    console.log('hello3');
} else {
    console.log('hello4');
}

if (true) console.log("중괄호를 생략했습니다.");

// if로 썼을 때보다 가독성이 좋아지는 효과가 있습니다.
switch (10) {
    case 1:
      // 값1에 대한 실행 코드
      console.log(1)
      break;
    case 2:
      // 값2에 대한 실행 코드
      console.log(2)
      break;
    default:
      // 모든 case에 해당하지 않을 때 실행될 코드
      console.log('default')
      break;
}


switch (new Date().getDay()) {
    case 1:
      document.write('월요일입니다.');
      break;
    case 2:
      document.write('화요일입니다.');
      break;
    case 3:
      document.write('수요일입니다.');
      break;
    case 4:
      document.write('목요일입니다.');
      break;
    case 5:
      document.write('금요일입니다.');
      break;
    default:
      document.write('금금요일입니다. 주말이 뭐죠?');
      break;
}


switch (new Date().getDay()) {
    case 1:
      console.log('월요일입니다.');
      break;
    case 2:
      console.log('화요일입니다.');
      break;
    case 3:
      console.log('수요일입니다.');
      break;
    case 4:
      console.log('목요일입니다.');
      break;
    case 5:
      console.log('금요일입니다.');
      break;
    case 6:
    case 7:
      console.log('주말입니다.');
      break;
}

// 많이 사용합니다.
switch (new Date().getDay()) {
    case 1:
    case 2:
    case 3:
    case 4:
    case 5:
        console.log('평일입니다.');
        break;
    case 6:
    case 7:
        console.log('주말입니다.');
        break;
}



for (let i = 0; i < 10; i++) {

}

for (let i = 0; i < 10; i += 2) {

}


// 무한반복
for (;;){

}


for (const key in [10, 20, 30]) {
    console.log(key)
}

for (const key in {'one':1, 'two':2}) {
    console.log(key)
}


// 나온지 얼마 안된 코드
for (const i of [10, 20, 30]) {
    console.log(i)
}



while (condition) {
    
}

let x = 0
while (x < 10) {
    console.log(x)
    // x += 1
    ++x
}