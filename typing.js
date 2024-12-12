"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var readline = require("readline");
// readlineインターフェースの作成
var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});
// ユーザーに質問
rl.question("入力してください: ", function (answer) {
    console.log("\u5165\u529B\u3055\u308C\u305F\u5185\u5BB9: ".concat(answer));
    rl.close();
});
