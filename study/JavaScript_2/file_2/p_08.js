const num = 12;
let n = num ** 2 % 5;

console.log(n); // 4

const numBigInt = BigInt(12);
let nb = numBigInt ** BigInt(2) % BigInt(5);

console.log(nb); // 4

const counter = { num : 1 };
counter.num ++;
console.log(counter.num); // 2

counter["num"] ++;
console.log(counter["num"]); // 3

console.log( typeof null ); // object
console.log( 100 + ture ); // NaN
console.log( 1 + Number("hello")); // NaN
console.log( 1 + Boolean("hello")); // 2