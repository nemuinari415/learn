let mySymbol1 = Symbol();
let mySymbol2 = Symbol();

const obj = {
    [mySymbol1]: '値 1',
    [mySymbol2]() {
        console.log("こんにちわ");
    }
};

console.log( obj[mySymbol1] ); // 値 1
obj[mySymbol2](); // こんにちわ