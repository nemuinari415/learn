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
function hornDrill(theirHp){
    if (Math.random() <= 0.3){
        return theirHp;
    } else {
        return theirHp = 0;
    }
}

console.log(hornDrill(10));