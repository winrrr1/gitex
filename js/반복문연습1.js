// 1 ~10 찍기

for(let i=0; i<5; i++){
    console.log(i);
}

console.log("--------------------------------");

for(let i=1; i<=5; i++){
    console.log(i);
}

console.log("--------------------------------");

// 합
let tot = 0;
for(let i=0; i<=10; i++){
    tot= tot + i
}
console.log(tot)

console.log("--------------------------------");

// 홀짝
for (let i=1; i<= 10; i++) {
    if (i%2 == 0) {
        console.log(`${i}는 짝`);
    } else {
        console.log(`${i}는 홀`);
    }
}

console.log("--------------------------------");

// //구구단
// for(let i=2;i<=9;i++){
//     for(let j=1;j<=9;j++){
//          console.log(`${i}X${j} = ${i*j}`)
//     }
// }

// //구구단
// for(let i=2;i<=9;i++){
//     let line = ''; // 각 줄의 결과를 저장할 변수
//     for(let j=1;j<=9;j++){
//         line += `${i}x${j}=${i * j} `; // 결과를 줄에 추가
//     }
//     console.log(line); // 줄 바꿈 후 결과를 출력
// }

// 구구단
for (let i = 2; i <= 9; i++) {
    for (let j = 1; j <= 9; j++) {
        process.stdout.write(`${i}x${j}=${i * j} `); // 결과를 가로로 출력
    }
    process.stdout.write('\n'); // 각 단이 끝난 후 줄 바꿈
}

console.log("--------------------------------");

// 별짓기
for (let i=5; i>0; i--) {
    let ro= ' ';
    for (let j = 0; j<i; j++) {
        ro += '* ';
    }
    console.log(ro);
}

console.log("--------------------------------");

// 배열을 반복문으로 돌리기 1
let arr=['apple',' banana',' candy']
for (let i=0;i<arr.length;i++){
    process.stdout.write(arr[i]); // 가로로 쓸때 
}

console.log("\n-----반복문1완료--------------------");

// 배열을 반복문으로 돌리기 2
let arr1=['apple','banana','candy']
for (let i in arr1 ){
    console.log(arr1[i]);
}

console.log("-----반복문2완료--------------------");

// 배열을 반복문으로 돌리기 3
let arr2=['apple','banana','candy']
for (let obj of arr2 ){
    console.log(obj);
}
console.log("-----반복문3완료--------------------");