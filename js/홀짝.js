// 홀짝
let n=1;
if(n%2 == 0 ){
    console.log("짝")
}else{
    console.log("짝")
}

// 성적 프로그램
let score=100;
if( score >= 90 && score <= 100 ){
    console.log("A 학점")
}else if (score >= 80 && score <90){
    console.log("B 학점")
}else{
    console.log("C 학점")
}

// 키오스크 만들기 
// 1번 누르면 짜장면, 2번 짬뽕, 3번 볶음밥 4번 탕수육

let menu = 9;

switch (menu) {
    case 1:
        console.log("짜 선택")
        break;
    case 2:
        console.log("짬 선택")
        break;
    case 3:
        console.log("볶음밥 선택")
        break;
    case 4:
        console.log("탕수육 선택")
        break;
    default:
        console.log("4가지 중에 선택하세요!")
        break;
    
}
// 1번 누르면 입금 , 2번누르면 출금, 3번 누르면 이체 확인, 4번 누르면 종료, 5번~  4번까지중에 선택하세요. 
let send = 3;

switch (send) {
    case 1:
        console.log("입금")
        break;
    case 2:
        console.log("출금")
        break;
    case 3:
        console.log("이체확인")
        break;
    case 4:
        console.log("종료")
        break;
    default:
        console.log("1 ~ 4 번 중에 선택하세요!")
        break;
}
