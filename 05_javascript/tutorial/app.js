// 1 =================================================
// alert("Hello World!");
// console.log("Hello World!");
// foo, bar, text
/*
const bar = () => {
    const foo = 1 + 1;
    console.log(foo);
} */
/*
const colorDark = "#000";
if(new Data().getHours() >= 0){
    document.body.style.backgroundColor = colorDark;
}
if(user.setting.darkMode === true){
    document.body.style.backgroundColor = colorDark;
}
*/
// const = 再代入不可
// let = 再代入可能
// var = 再代入可能(主流ではない)
// 2 =================================================
/*
const foo = "bar";
const array = [1, "Hello", foo];

console.log(array[1]); 
*/
/*
const a = "ニャオハ";
const b = "ホゲータ";
const c = "クワッス";

const fistPokemons = [a, b, c];
console.log(fistPokemons[0],fistPokemons[1],fistPokemons[2]);
*/
/*
const questions = [
    "Aaa",
    "Bbb",
    "Ccc",
];

for (let index = 0; index < questions.length; index++) {
    console.log(questions[index]);
}
*/
/*
let isLogin = false;
if(!isLogin){ // && = and  || = or
    alert("ログインしてください")
} else {
    console.log("ログイン成功中");
}
*/
/*
const myMoney = 1000;
let isShipping = false;

if(myMoney >= 500){
    isShipping = true;
}
console.log(isShipping);
*/
/*
if (new DataTransfer().getHours() > 20) {
    document.body.style.backgroundColor = "#000";
}
*/
/*
function changeDarkMonde(obj) {
    if (new Date().getHours() > obj.time) {
        document.body.style.backgroundColor = obj.color;
    }
}

changeDarkMonde({
    time: 11,
    color: "#333",
})
*/
/*
const sonicBoom = () => {
    let damage = 20
    return damage
}
console.log(sonicBoom()); // 20
*/
/*
function metalBurst(lastDamage){
    return lastDamage * 1.5;
}

console.log(metalBurst(10));
*/
/*
function hornDrill(theirHp){
    if (Math.random() <= 0.3){
        return theirHp;
    } else {
        return theirHp = 0;
    }
}

console.log(hornDrill(10));
*/
//const オブジェクト名 = {
//    プロパティ名: 値
//};
/*
const susUser = {
    id: 1,
    userName: "Taro",
    gender: "male",
    like: function() {
        console.log("like");
    },
    post: function() {
        console.log("post");
    }
};
console.log(susUser.id); // 1
*/
/*
const snsUser = {
    id: 1,
    userName: "Taro",
    like: function () { },
    post: function () { },
    followers: ["Yamada", "Suzuki", "Tanaka"],
    followers: ["Yamada", "Suzuki"],
    premium: true,
    darkMode: false,
    posts: null,
}
console.log(snsUser.id); // 1
*/
/*
const pikachu = {
    name: "ピカチュウ",
    level: 18,
    types: ["でんき"],
    skills: ["10万ボルト", "でんこうせっか", "たいあたり"],
    levelUp: function() {
        this.level++;
        if (this.level >= 20) {
            this.skills.push("スパーク");
        }
    }
};
*/
/*
console.log(parseInt("2")); // 2 -> 整数に変換
*/
/*
const myPokemons = ["サンダー", "ホウオウ", "スイクン", "ラティアス", "パルキア"];
myPokemons.push("ミュウツー");
console.log(myPokemons.length); // 6

const oldVersions = ["赤", "緑", "青"];
const newVersions = ["ルビー", "サファイア", "エメラルド"];

console.log(oldVersions.concat(newVersions));
// ["赤", "緑", "青", "ルビー", "サファイア", "エメラルド"]
*/
const button = document.getElementById("button");
const output = document.getElementById("output");

button.addEventListener("click", () => {
    // ピカチュウの名前を 20%の確率で表示する
    let num = Math.floor(Math.random() * 5);
    if (num === 0) {
        output.textContent = "ピカチュウ";
    } else {
        output.textContent = "ざんねん！あと少しで捕まえられたのに！";
    }
    console.log(output.textContent);
});