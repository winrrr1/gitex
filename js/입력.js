const repl = require('repl');

repl.start({
    prompt: "입력하세요> ",
    eval: (command, context, filename, callback) => {
        let number = Number(command.trim()); // trim을 사용하여 공백을 제거합니다.
        
        if (isNaN(number)) {
            console.log("유효한 숫자가 아닙니다.");
        } else {
            console.log(`입력된 숫자: ${number}`);
        }

        callback(); // callback을 호출하여 REPL 프롬프트를 반환합니다.
    }
});
